"""
Eval runner for rules-file evaluation.

Runs predefined eval tasks with and without a rules file as system context,
scores the outputs using an LLM-as-judge, and generates a PR comment with
the results.

Usage:
    python scoring/eval_rules.py --trials 3 --output comment.md
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import anthropic

DEFAULT_MODEL = "claude-sonnet-4-20250514"
EVALS_DIR = Path(__file__).resolve().parent.parent / "evals"
RULES_FILE = Path(__file__).resolve().parent.parent / "sample-project" / "CLAUDE.md"


def load_eval_tasks(evals_dir):
    """Discover and load all eval task directories under evals_dir."""
    tasks = []
    evals_path = Path(evals_dir)
    for task_dir in sorted(evals_path.iterdir()):
        criteria_file = task_dir / "criteria.json"
        if not task_dir.is_dir() or not criteria_file.exists():
            continue
        instruction = (task_dir / "instruction.md").read_text()
        context = ""
        context_file = task_dir / "context.md"
        if context_file.exists():
            context = context_file.read_text()
        criteria = json.loads(criteria_file.read_text())
        tasks.append({
            "name": criteria.get("task_name", task_dir.name),
            "dir": task_dir.name,
            "instruction": instruction,
            "context": context,
            "criteria": criteria,
        })
    return tasks


def build_prompt(task):
    """Assemble the user message from instruction and context."""
    parts = [task["instruction"].strip()]
    if task["context"].strip():
        parts.append(f"\n\n---\n\n{task['context'].strip()}")
    return "\n".join(parts)


def run_task(client, model, user_prompt, system_prompt, n):
    """Call the Anthropic API n times and return the list of outputs."""
    outputs = []
    for _ in range(n):
        messages = [{"role": "user", "content": user_prompt}]
        kwargs = {"model": model, "max_tokens": 1024, "messages": messages}
        if system_prompt:
            kwargs["system"] = system_prompt
        for attempt in range(2):
            try:
                response = client.messages.create(**kwargs)
                break
            except anthropic.APIError as e:
                if attempt == 0:
                    print(f"Warning: API error on attempt 1, retrying: {e}",
                          file=sys.stderr)
                    time.sleep(1)
                else:
                    print(f"Warning: API error on attempt 2, skipping trial: {e}",
                          file=sys.stderr)
                    response = None
        if response is None:
            continue
        text = "".join(
            block.text for block in response.content if block.type == "text"
        )
        outputs.append(text)
    return outputs


def score_output(client, model, output, criteria):
    """Use LLM-as-judge to score a single output against criteria."""
    rubric_lines = []
    for c in criteria["criteria"]:
        rubric_lines.append(f"### {c['name']}")
        rubric_lines.append(c["description"])
        for score_val, desc in sorted(c["scores"].items()):
            rubric_lines.append(f"  {score_val}: {desc}")
    rubric = "\n".join(rubric_lines)

    criterion_names = [c["name"] for c in criteria["criteria"]]

    judge_prompt = f"""You are an eval judge. Score the following output against the rubric below.

For each criterion, assign a score (use only the exact integer values defined in the rubric).
Return ONLY a JSON object mapping criterion name to integer score. No explanation.

Example response format:
{json.dumps({name: 0 for name in criterion_names})}

## Rubric

{rubric}

## Output to score

{output}"""

    response = None
    for attempt in range(2):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=256,
                temperature=0,
                messages=[{"role": "user", "content": judge_prompt}],
            )
            break
        except anthropic.APIError as e:
            if attempt == 0:
                print(f"Warning: API error on attempt 1 (scoring), retrying: {e}",
                      file=sys.stderr)
                time.sleep(1)
            else:
                print(f"Warning: API error on attempt 2 (scoring), returning zeros: {e}",
                      file=sys.stderr)

    if response is None:
        return {name: 0 for name in criterion_names}

    text = "".join(
        block.text for block in response.content if block.type == "text"
    )
    # Extract JSON from response (handle markdown code blocks)
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]  # remove opening ```json
        text = text.rsplit("```", 1)[0]  # remove closing ```
    try:
        return json.loads(text.strip())
    except json.JSONDecodeError as e:
        print(f"Warning: failed to parse judge response as JSON: {e}", file=sys.stderr)
        return {name: 0 for name in criterion_names}


def run_eval(evals_dir, rules_file, trials, model):
    """Run all eval tasks with and without rules, return structured results."""
    client = anthropic.Anthropic()

    rules_text = None
    if rules_file and Path(rules_file).exists():
        rules_text = Path(rules_file).read_text().strip()

    tasks = load_eval_tasks(evals_dir)
    if not tasks:
        print("No eval tasks found in", evals_dir, file=sys.stderr)
        sys.exit(1)

    results = []
    for task in tasks:
        task_trials = trials or task["criteria"].get("trials", 3)
        user_prompt = build_prompt(task)
        criterion_names = [c["name"] for c in task["criteria"]["criteria"]]

        print(f"Running: {task['name']} ({task_trials} trials per condition)",
              file=sys.stderr)

        # Run without rules
        print("  without rules...", file=sys.stderr)
        without_outputs = run_task(client, model, user_prompt, None, task_trials)
        without_scores = []
        for output in without_outputs:
            scores = score_output(client, model, output, task["criteria"])
            without_scores.append(scores)

        # Run with rules
        with_outputs = []
        with_scores = []
        if rules_text:
            print("  with rules...", file=sys.stderr)
            with_outputs = run_task(
                client, model, user_prompt, rules_text, task_trials,
            )
            for output in with_outputs:
                scores = score_output(client, model, output, task["criteria"])
                with_scores.append(scores)

        max_per_criterion = {
            c["name"]: max(int(k) for k in c["scores"])
            for c in task["criteria"]["criteria"]
        }
        results.append({
            "task_name": task["name"],
            "criterion_names": criterion_names,
            "trials": task_trials,
            "max_per_criterion": max_per_criterion,
            "without_outputs": without_outputs,
            "without_scores": without_scores,
            "with_outputs": with_outputs,
            "with_scores": with_scores,
        })

    return results


def avg_scores(score_list, criterion_names):
    """Compute average score per criterion across trials."""
    if not score_list:
        return {name: 0.0 for name in criterion_names}
    avgs = {}
    for name in criterion_names:
        values = [s.get(name, 0) for s in score_list]
        avgs[name] = sum(values) / len(values)
    return avgs


def format_comment(results, has_rules):
    """Generate the PR comment markdown."""
    lines = ["## Eval Scorecard — Your Rules File\n"]

    all_deltas = {}

    for i, r in enumerate(results, 1):
        names = r["criterion_names"]
        max_per_criterion = r["max_per_criterion"]
        trials = r["trials"]
        max_total = sum(max_per_criterion[name] for name in names)

        without_avg = avg_scores(r["without_scores"], names)

        # Header
        lines.append(f"**Task {i}: {r['task_name']}** ({trials} trials each)\n")

        # Table header
        header_cols = ["Condition"] + [n.replace("_", " ").title() for n in names] + ["Avg Total"]
        lines.append("| " + " | ".join(header_cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(header_cols)) + " |")

        # Without row
        without_total = sum(without_avg.values())
        without_cells = ["Without rules"]
        for name in names:
            without_cells.append(f"{without_avg[name]:.1f}")
        without_cells.append(f"{without_total:.1f} / {max_total}")
        lines.append("| " + " | ".join(without_cells) + " |")

        if has_rules and r["with_scores"]:
            with_avg = avg_scores(r["with_scores"], names)
            with_total = sum(with_avg.values())

            # With row
            with_cells = ["With your rules"]
            for name in names:
                with_cells.append(f"{with_avg[name]:.1f}")
            with_cells.append(f"{with_total:.1f} / {max_total}")
            lines.append("| " + " | ".join(with_cells) + " |")

            # Delta row
            delta_cells = ["**Delta**"]
            for name in names:
                d = with_avg[name] - without_avg[name]
                all_deltas[name.replace("_", " ").title()] = d
                if abs(d) >= 0.5:
                    delta_cells.append(f"**{d:+.1f}**")
                else:
                    delta_cells.append(f"{d:+.1f}")
            total_delta = with_total - without_total
            if abs(total_delta) >= 0.5:
                delta_cells.append(f"**{total_delta:+.1f}**")
            else:
                delta_cells.append(f"{total_delta:+.1f}")
            lines.append("| " + " | ".join(delta_cells) + " |")

        lines.append("")

    # Summary insights
    if has_rules and all_deltas:
        positive = {k: v for k, v in all_deltas.items() if v > 0.3}
        zero = {k: v for k, v in all_deltas.items() if abs(v) <= 0.3}
        overall = sum(all_deltas.values())

        lines.append("> ")
        if positive:
            best = sorted(positive, key=positive.get, reverse=True)
            parts = [f"**{k}** ({positive[k]:+.1f})" for k in best[:3]]
            lines.append(f"> Your rules file helped most with {', '.join(parts)}.")
        if zero:
            unchanged = list(zero.keys())[:3]
            lines.append(
                f"> It didn't change **{'**, **'.join(unchanged)}** "
                "— the model already handles those well."
            )
        lines.append(f"> Overall delta: **{overall:+.1f} points** across all tasks.")
        lines.append("")
    elif not has_rules:
        lines.append(
            "> No rules file found at `sample-project/CLAUDE.md`. "
            "These are baseline-only scores.\n"
            "> Create a rules file and push it to see the with/without comparison.\n"
        )

    # Raw outputs
    lines.append("<details><summary>Raw outputs (click to expand)</summary>\n")
    for i, r in enumerate(results, 1):
        for j, output in enumerate(r["without_outputs"], 1):
            lines.append(f"### Task {i}, Trial {j} (without rules)\n")
            for line in output.strip().split("\n"):
                lines.append(f"> {line}")
            lines.append("")
        for j, output in enumerate(r["with_outputs"], 1):
            lines.append(f"### Task {i}, Trial {j} (with rules)\n")
            for line in output.strip().split("\n"):
                lines.append(f"> {line}")
            lines.append("")
    lines.append("</details>")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Run rules-file eval")
    parser.add_argument(
        "--trials", type=int, default=None,
        help="Number of trials per condition (overrides criteria.json)",
    )
    parser.add_argument(
        "--output", type=str, default="-",
        help="Output file for the comment markdown (- for stdout)",
    )
    parser.add_argument(
        "--evals-dir", type=str, default=str(EVALS_DIR),
        help="Directory containing eval tasks",
    )
    parser.add_argument(
        "--rules-file", type=str, default=str(RULES_FILE),
        help="Path to the rules file (CLAUDE.md)",
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        print(
            "Error: ANTHROPIC_API_KEY is not set.\n\n"
            "To run this eval, you need an Anthropic API key:\n"
            "  1. Get a key at https://console.anthropic.com/\n"
            "  2. Export it:  export ANTHROPIC_API_KEY=sk-ant-...\n"
            "  3. Or add it as a GitHub repository secret named ANTHROPIC_API_KEY\n",
            file=sys.stderr,
        )
        sys.exit(1)

    model = os.environ.get("EVAL_MODEL", DEFAULT_MODEL)
    has_rules = Path(args.rules_file).exists()

    results = run_eval(args.evals_dir, args.rules_file, args.trials, model)
    comment = format_comment(results, has_rules)

    if args.output == "-":
        print(comment)
    else:
        Path(args.output).write_text(comment)
        print(f"Comment written to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()

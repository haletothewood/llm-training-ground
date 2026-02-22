# Automated Rules-File Eval

This Action runs an automated eval when you open a PR that includes a rules file
(`sample-project/CLAUDE.md`). It sends predefined tasks to an LLM **with** and
**without** your rules file as system context, scores the outputs, and posts the
results as a PR comment.

## Setup

1. **Fork** this repo
2. Go to your fork's **Settings > Secrets and variables > Actions**
3. Add a repository secret named `ANTHROPIC_API_KEY` with your Anthropic API key
4. Create `sample-project/CLAUDE.md` with your project rules
5. Open a PR — the eval Action triggers automatically

## Reading the results

The Action posts a scorecard as a PR comment with:

- **Without rules**: Baseline scores (no rules file)
- **With your rules**: Scores with your rules file as system context
- **Delta**: The difference — positive means your rules helped

Each criterion is scored 0–2 across multiple trials. Look for criteria where your
rules file makes the biggest difference, and criteria where the model already does
well without help.

## Adding new eval tasks

Each eval task is a directory under `evals/` with three files:

```
evals/my-new-task/
├── instruction.md     # The prompt sent to the LLM
├── criteria.json      # Scoring rubric (what to evaluate)
└── context.md         # Fixed context included with the prompt
```

The runner discovers all directories under `evals/` that contain a `criteria.json`.
No code changes needed — just add a directory.

See `evals/code-review-summary/` for an example of the format.

This follows the same principle as [Tessl's Harbor format](https://tessl.io/blog/how-to-evaluate-ai-agents-an-introduction-to-harbor/):
evals are data, not hardcoded logic.

## Running locally

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python scoring/eval_rules.py --trials 3 --output comment.md
```

Use `--trials 1` for a quick check. Output goes to stdout with `--output -`.

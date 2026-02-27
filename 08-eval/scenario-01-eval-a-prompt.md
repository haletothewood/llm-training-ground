# Scenario 01 — Eval a Prompt

**Requires:** any chat interface

## Goal
Measure whether a refined prompt produces better output than a simple one, using a
rubric and multiple trials.

## Background

Module 01 taught that precise prompts beat vague ones — but you never measured the
delta. You compared two outputs side by side and decided the precise one "looked better."
This scenario quantifies "better" with a rubric, and runs multiple trials so variance
doesn't fool you.

---

## Part A — Define the task and input

The task: generate a code review summary from a diff.

Here's a concrete diff to use — the `filter_by_priority` bug in
`sample-project/tasks.py` (lines 30–34):

```diff
--- a/sample-project/tasks.py
+++ b/sample-project/tasks.py
@@ -29,6 +29,4 @@ def filter_by_status(tasks, status):
 def filter_by_priority(tasks, priority):
-    # BUG: uses >= instead of ==, so "low" returns everything,
-    # "medium" returns medium + high, and only "high" works correctly.
-    # The symptom: GET /tasks?priority=medium returns too many results.
-    target = PRIORITY_ORDER.get(priority, -1)
-    return [t for t in tasks if PRIORITY_ORDER.get(t["priority"], -1) >= target]
+    return [t for t in tasks if t["priority"] == priority]
```

Alternatively: use a real diff from your own work. A `git diff` from a recent commit
works well.

---

## Part B — Write two prompts

**Prompt A** — minimal:

```
Summarise this code change.

<diff>
(paste the diff from Part A here)
</diff>
```

**Prompt B** — detailed:

```
You are reviewing a pull request. Given the diff below, write a code review summary.

Requirements:
- Start with a one-sentence description of what changed and why
- List any risks this change introduces (edge cases, breaking changes, performance)
- Suggest one test case that would verify the fix works correctly
- Keep the total summary under 150 words

<diff>
(paste the diff from Part A here)
</diff>
```

---

## Part C — Define scoring criteria

Score each output on this rubric:

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| **Accuracy** | Misidentifies what changed or why | Identifies the change but misses the root cause | Correctly identifies what changed, why it was wrong, and what the fix does |
| **Actionability** | No useful information for a reviewer | Mentions what to look for but vaguely | Specific risks, edge cases, or test suggestions a reviewer could act on |
| **Conciseness** | Rambling, padded, or includes irrelevant detail | Mostly focused but some filler | Every sentence adds information, no padding |
| **Risk awareness** | No mention of risks or edge cases | Mentions risks in general terms | Identifies specific risks (e.g., invalid priority values, missing keys) |

Total possible: **8 points** per output.

Modify this rubric if you're using your own diff — the criteria should match what
"good" means for your specific task.

---

## Part D — Run the trials

Run each prompt 3–5 times. Use a **fresh session** for each trial (new conversation,
no prior context). Score each output immediately after reading it — don't batch the
scoring.

Record your results:

**Prompt A — minimal:**

| Trial | Accuracy (0–2) | Actionability (0–2) | Conciseness (0–2) | Risk awareness (0–2) | Total |
|-------|-----------------|---------------------|--------------------|-----------------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| Avg | | | | | |

**Prompt B — detailed:**

| Trial | Accuracy (0–2) | Actionability (0–2) | Conciseness (0–2) | Risk awareness (0–2) | Total |
|-------|-----------------|---------------------|--------------------|-----------------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| Avg | | | | | |

### Option 1 — Fresh chat sessions (any tool)

Open a new conversation in whatever LLM you use (ChatGPT, Claude, Gemini, Cursor chat,
etc.). Paste the prompt. Score the output. Close the session and start a new one for the
next trial. The key is that each trial starts with zero prior context.

### Option 2 — CLI one-liners

If your tool has a non-interactive mode, use it to avoid manual session management:

```bash
# Claude Code
claude -p "your prompt here"

# Or any CLI wrapper you prefer
```

Run it multiple times — each invocation is a fresh session with no memory of prior runs.

### Option 3 — Python script for repeatable runs

For full automation, create `eval_prompt.py`. You'll need your `ANTHROPIC_API_KEY`
set in your environment:

```python
"""
Run a prompt multiple times and print each result for manual scoring.
Requires: pip install anthropic
"""

import sys
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from environment
MODEL = "claude-sonnet-4-20250514"

DIFF = """
--- a/sample-project/tasks.py
+++ b/sample-project/tasks.py
@@ -29,6 +29,4 @@ def filter_by_status(tasks, status):
 def filter_by_priority(tasks, priority):
-    # BUG: uses >= instead of ==, so "low" returns everything,
-    # "medium" returns medium + high, and only "high" works correctly.
-    # The symptom: GET /tasks?priority=medium returns too many results.
-    target = PRIORITY_ORDER.get(priority, -1)
-    return [t for t in tasks if PRIORITY_ORDER.get(t["priority"], -1) >= target]
+    return [t for t in tasks if t["priority"] == priority]
"""

PROMPT_A = f"Summarise this code change.\n\n<diff>\n{DIFF}\n</diff>"

PROMPT_B = f"""You are reviewing a pull request. Given the diff below, write a code review summary.

Requirements:
- Start with a one-sentence description of what changed and why
- List any risks this change introduces (edge cases, breaking changes, performance)
- Suggest one test case that would verify the fix works correctly
- Keep the total summary under 150 words

<diff>
{DIFF}
</diff>"""

def run_trials(prompt, label, n=3):
    print(f"\n{'='*60}")
    print(f"  {label} — {n} trials")
    print(f"{'='*60}")
    for i in range(n):
        message = client.messages.create(
            model=MODEL,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}],
        )
        print(f"\n--- Trial {i+1} ---")
        print(message.content[0].text)
        print()

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    run_trials(PROMPT_A, "Prompt A (minimal)", n)
    run_trials(PROMPT_B, "Prompt B (detailed)", n)
```

Run it:

```bash
python eval_prompt.py 5    # 5 trials each
```

The script is a convenience, not a requirement. If you prefer running trials by hand in
a chat UI, that works just as well — the eval is in the scoring, not the automation.

---

## Part E — Interpret the results

Calculate the average score for each prompt. Then answer:

1. **What's the delta?** Prompt B average minus Prompt A average.
2. **Was the delta consistent?** Did Prompt B win every trial, or were there reversals?
3. **Which criterion showed the biggest difference?** This tells you what the detailed
   prompt actually improved.
4. **Did any Prompt A trial beat the best Prompt B trial?** If so, what does that tell
   you about single-run evaluation?

---

## What to notice

- **Variance across trials of the same prompt.** The same prompt doesn't produce the
  same score every time. This is why single-run evaluation is unreliable — the result
  you saw in Module 01 might have been an outlier.
- **Difficulty of scoring.** Was it hard to decide between a 1 and a 2? That's a signal
  the criterion needs sharper definition.
- **Did defining the rubric change your understanding of "good"?** Most people discover
  that the act of writing criteria is more valuable than the scores themselves.

---

## Challenge

Take a prompt you actually use at work. Write a rubric with 3–4 criteria. Run 5 trials.
Modify the prompt to address the weakest criterion. Run 5 more trials. Did the change
help?

This is the eval loop: change → measure → iterate.

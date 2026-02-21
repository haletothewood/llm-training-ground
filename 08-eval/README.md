# Module 08 — Eval

## By the end of this module you'll be able to

- Design a with/without eval that compares output quality against a baseline
- Define scoring criteria beyond "that looks good" — specific, observable, graduated
- Run multiple trials to handle non-determinism and interpret the results
- Use the eval loop: change, measure, iterate

---

## Why this module exists

Module 07 wrote rules files and automation scripts, but never measured whether they
helped. You tested your rules file by running one task, eyeballing the result, and
deciding it "seemed better." That's not measurement — that's vibes.

Without a baseline, you can't know whether a rules file is helping, redundant, or
actively confusing the model. Without multiple trials, you can't distinguish a real
improvement from the randomness you observed in Module 00 Scenario 02. This module
makes improvement quantifiable.

## Key concepts

### What is an eval

A repeatable test that produces a score on a rubric. Not binary pass/fail — graduated
scores (0/1/2) across multiple criteria. Run multiple times to account for
non-determinism (you saw this in Module 00 Scenario 02: the same prompt doesn't always
produce the same output). An eval turns "did it work?" into "what's the pass rate over
N trials?"

### The with/without baseline

Run the same task with and without the thing you're evaluating. This produces three
possible outcomes:

1. **With > without** — the thing helps. Keep it.
2. **Both high** — the thing is redundant. The model already does this well. Remove it.
3. **With < without** — the thing is confusing the model. This is the outcome you'd
   never discover without a baseline, and the most valuable finding an eval can produce.

### Scoring criteria

"Good" is not a criterion. Neither is "helpful" or "accurate" without a definition.
Useful criteria are specific (what exactly are you looking for?), observable (could two
people agree on the score?), and graduated (0 = absent, 1 = partial, 2 = fully
present). Defining the rubric is the hardest and most valuable part of eval design —
it forces you to articulate what "good" actually means for your task.

### Statistical thinking

A single run proves nothing. Module 00 showed that the same prompt produces different
outputs each time. Evals operationalise that insight: you don't ask "did it work?" but
"what's the pass rate over N trials?" Three trials is the minimum; five is better.
Variance across trials of the same prompt is itself useful data.

### The eval loop

Change the prompt (or skill, or rules file) → run the eval → measure → iterate. This
is the same feedback loop as Module 07's weekly review, but applied to a single prompt
with quantitative measurement instead of qualitative reflection.

## Scenarios in this module

- [Scenario 01 — Eval a Prompt](./scenario-01-eval-a-prompt.md)
- [Scenario 02 — Eval a Skill](./scenario-02-eval-a-skill.md)
- [Scenario 03 — Tessl Task Evals](./scenario-03-tessl.md) (optional — advanced)

## Before you move on

You're done when you can answer "does this change make the output better?" with
evidence instead of intuition.

# Module 08 — Solutions

Module 08 produces data (scores, deltas, rubrics) rather than single correct answers.
These calibration points help you check whether your results are in a reasonable range.

---

## Scenario 01 — Eval a Prompt

### Expected ranges

- **Prompt A (minimal):** typical total 2–5 out of 8. Usually scores well on accuracy
  (models are good at reading diffs) but low on actionability and risk awareness.
- **Prompt B (detailed):** typical total 5–7 out of 8. The format constraints and
  explicit requirements push scores up on most criteria.
- **Expected delta:** 2–4 points. If your delta is smaller, your rubric may be too easy
  (everything scores 2). If it's larger, Prompt A may have been unusually bad — check
  whether your trials were truly fresh sessions.

### Common patterns

| Pattern | What it means |
|---------|---------------|
| Rubric is too easy — everything scores 6+ | Your criteria aren't discriminating enough. Add sharper distinctions between 1 and 2. |
| High variance within one prompt | Normal. Non-determinism means ±1-2 points across trials is expected. This is why single-run evaluation is unreliable. |
| Accuracy is high for both prompts | Models are generally good at reading diffs. The delta usually shows up in structure, risk awareness, and conciseness — the things the detailed prompt explicitly requests. |
| Prompt A occasionally beats Prompt B | Happens in ~10-20% of trials. This is why you need multiple runs — a single comparison could have led you to the wrong conclusion. |

### Rubric calibration

If you found scoring difficult, that's the point. The most common issue: criteria that
sound different but measure the same thing (e.g., "accuracy" and "correctness").
Merge overlapping criteria and make each one measure a distinct dimension.

---

## Scenario 02 — Eval a Skill

### The baseline surprise

The most common finding: the baseline is better than expected. Models default to
reasonable conventions for popular frameworks (pytest over unittest, sensible file
locations, descriptive test names). This means:

- **Rules that restate best practices** (use pytest, write descriptive names) typically
  show near-zero delta. The model already does this.
- **Rules that specify project-specific conventions** (file location, naming patterns
  unique to this project) show the most consistent positive delta.
- **"Do not" rules** (don't create new files, don't add docstrings) often show the
  highest delta — preventing specific unwanted behaviour is where rules files earn
  their keep.

### A healthy result

A healthy eval result for a rules file typically shows:

- At least one criterion with a clear positive delta (the rules file is doing something)
- At least one criterion with near-zero delta (some rules are redundant)
- A revised rules file that's shorter than the original

If every criterion shows a large positive delta, your baseline task may have been too
hard or too unusual. If every criterion shows zero delta, the rules file may not be
testing the right task.

---

## Scenario 03 — Tessl Task Evals

### Calibration points

- **Auto-generated scenarios** typically cover 60–80% of the cases you'd write manually.
  They're good at testing explicit rules and less good at testing implicit conventions.
- **Pass rates of 70–90%** are typical for a well-written skill. 100% is suspicious —
  either the scenarios are too easy or the scoring is too lenient.
- **1–2 negative deltas out of 10 scenarios** is normal. These are usually caused by
  rules that are too specific, causing the model to follow the letter of the rule at
  the expense of overall quality.
- **Zero-delta scenarios** are the most actionable finding — they identify rules you
  can safely remove to make the skill shorter and more focused.

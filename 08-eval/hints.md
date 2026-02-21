# Module 08 — Hints

## Scenario 01 — Eval a Prompt

The hardest part is the rubric, not the trials. If you're stuck defining criteria: run
each prompt once, compare the two outputs side by side, and ask yourself "what
specifically is better about this one?" Those specifics are your criteria.

Three trials is the minimum for spotting variance. Five is better. If you only run two,
a single outlier can flip your conclusion.

Score each output immediately after reading it. If you batch the scoring (read all
outputs, then score), you'll unconsciously compare them to each other instead of to the
rubric.

---

## Scenario 02 — Eval a Skill

The most common surprise: the baseline is already good. Models default to reasonable
conventions for popular frameworks. If your rules file restates things the model already
does, the delta will be near zero — and that's a useful finding, not a failure.

Make sure the rules file is genuinely absent for baseline runs. Rename it to `.bak` —
don't just close the file. Some tools scan the project directory automatically.

```bash
# Adapt the path to your tool's rules file:
mv CLAUDE.md CLAUDE.md.bak                  # baseline runs
mv CLAUDE.md.bak CLAUDE.md                  # "with" runs
```

If you can't tell with and without apart, that's a result. It means the rules file
isn't changing behaviour for this task. Either the task isn't the right test, or the
rules aren't doing what you think.

---

## Scenario 03 — Tessl Task Evals

If you don't have Tessl access, Part A (understanding the methodology) and Part D
(the Harbor eval format) still teach the core concepts. The open-source format means you
can structure your own evals the same way even without the tool.

The auto-generated scenarios are a starting point, not the final word. If important cases
are missing, add your own — the tool will run them alongside the generated ones.

---

## General

Good eval criteria are:

- **Observable** — could two people independently agree on the score?
- **Specific** — "accurate" is too vague; "correctly identifies the root cause" is specific
- **Independent** — each criterion measures something different
- **Graduated** — 0/1/2, not just yes/no. Binary scoring loses too much information.

If you can't score the same output the same way on two readings, the criterion is too
subjective. Sharpen it until you can.

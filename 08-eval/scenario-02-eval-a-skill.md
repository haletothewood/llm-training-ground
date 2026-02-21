# Scenario 02 — Eval a Skill

## Goal
Measure whether a project rules file actually improves output, or whether the model
already handles the task well without it.

## Background

In Module 07 Scenario 01, you tested a rules file by running one task with it in place
and deciding the output "seemed good." That's a sample size of one with no baseline.
You don't know if the output would have been just as good without the rules file.

This scenario adds both: a baseline (without the rules file) and multiple trials to
handle variance.

---

## Part A — Choose what to evaluate

Pick one:

1. **The rules file you wrote in Module 07 Scenario 01** (`CLAUDE.md`, `.cursor/rules`,
   `copilot-instructions.md`, etc.). If you still have it, use it.
2. **A custom skill from Module 03.** If you wrote a slash command or tool, evaluate that.
3. **The minimal rules file below** — if you don't have one from a previous module, use
   this for `sample-project/`. Save it as whatever your tool reads (`CLAUDE.md`,
   `.cursor/rules/project.md`, etc.):

```markdown
# Project rules

Flask REST API for task management.

## Tech stack
- Python 3.11, Flask, pytest

## Conventions
- Tests go in `tests/`. Mirror the source file name: `tests/test_tasks.py`
- Use pytest fixtures, not setUp/tearDown
- Use `datetime.now(timezone.utc)` not `datetime.utcnow()`

## Do not
- Create new files unless asked
- Add docstrings to functions that don't already have them
- Use unittest or mock.patch — use pytest and monkeypatch
```

---

## Part B — Define the task and scoring criteria

Pick a task the rules file should influence. For the `sample-project/` rules file above,
a good task is: **"Write a test for the `create_task` function in
`sample-project/tasks.py`."**

Score each output on this rubric:

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| **Uses pytest** | Uses unittest or no testing framework | Uses pytest but with unittest patterns (e.g., `self.assert*`) | Clean pytest with assertions, fixtures if appropriate |
| **File location** | Test in wrong directory or unnamed sensibly | Reasonable location but doesn't match convention | In `tests/test_tasks.py` matching the convention |
| **Naming convention** | No clear naming pattern | Descriptive but inconsistent with project style | `test_<function>_<scenario>` pattern |
| **Test quality** | Tests don't verify meaningful behaviour | Tests verify basic behaviour only | Tests cover normal case and at least one edge case |

Total possible: **8 points** per output.

If you're evaluating a different rules file, modify the rubric to match what your rules
should influence.

---

## Part C — Run with and without

### Without (baseline)

Remove the rules file so the model has no project-level instructions. Rename it rather
than deleting — you'll need it back:

```bash
# Adapt the filename to your tool:
mv sample-project/CLAUDE.md sample-project/CLAUDE.md.bak
# or: mv sample-project/.cursor/rules/project.md sample-project/.cursor/rules/project.md.bak
```

Run 3 trials in fresh sessions. Open the project in your AI tool, paste the task prompt,
score the output, and start a new session for each trial.

Task prompt:
```
Write a test for the create_task function in tasks.py.
```

Record:

**Without rules file (baseline):**

| Trial | Uses pytest (0–2) | File location (0–2) | Naming (0–2) | Test quality (0–2) | Total |
|-------|-------------------|---------------------|--------------|---------------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| Avg | | | | | |

### With rules file

Restore the rules file:

```bash
mv sample-project/CLAUDE.md.bak sample-project/CLAUDE.md
```

Run 3 trials in fresh sessions with the rules file in place. Score each immediately.

**With rules file:**

| Trial | Uses pytest (0–2) | File location (0–2) | Naming (0–2) | Test quality (0–2) | Total |
|-------|-------------------|---------------------|--------------|---------------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| Avg | | | | | |

---

## Part D — Interpret the delta

Calculate: **with average** minus **without average** = **delta**.

Three outcomes and what they mean:

### High delta (with >> without)
The rules file is earning its keep. Look at which criteria improved most — those are
the rules that matter. The rest might be dead weight.

### Near-zero delta (with ≈ without)
The model already does this well without your rules. This is the most common surprise.
Modern models default to reasonable conventions for common frameworks. A rules file
that restates best practices the model already follows is redundant — it adds tokens
to every session without changing behaviour.

### Negative delta (with < without)
The rules file is confusing the model. This sounds unlikely but happens more often
than you'd expect: overly specific rules can cause the model to focus on following
instructions literally instead of writing good code. This outcome is the one you'd
never discover without a baseline — and the most valuable finding an eval can produce.

---

## What to notice

- **Was the baseline surprisingly good?** Most people overestimate how much the model
  needs their rules file. If baseline scores are 6–7 out of 8, the rules file is
  solving a problem that barely exists.
- **Did any specific rule have a visible effect?** Look at individual criteria. A rule
  about pytest might score 2/2 with and without — the model uses pytest by default.
  A rule about file location might show the only improvement.
- **How would you revise the rules file based on this data?**

---

## Challenge

Revise the rules file based on your data:

1. **Remove** rules with zero delta — they're adding tokens without changing behaviour
2. **Strengthen** rules tied to the highest-delta criteria
3. **Add** rules for criteria where both conditions scored low
4. Re-run the eval with the revised rules file

Did the revision improve the score? Did removing redundant rules hurt anything?

This is the eval loop applied to infrastructure: change → measure → iterate. The same
loop you'd use to improve a prompt, but applied to the thing that shapes every prompt
in the project.

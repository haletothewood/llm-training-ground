# Scenario 03 — Tessl Task Evals

> **Optional — advanced.** This scenario is for developers who want to automate the
> eval process from Scenarios 01–02 using tooling. Scenarios 01 and 02 are sufficient
> for understanding and applying evals. If you don't have Tessl, Parts A and D still
> teach the concepts and the open-source eval format.

## Goal
Use Tessl's Task Evals to automate the with/without comparison process from Scenarios
01–02.

## Background

Scenarios 01–02 worked, but they were slow. You ran each prompt manually, scored each
output by hand, and recorded results in a table. That's fine for learning the method —
but it doesn't scale to evaluating a rules file across dozens of scenarios, or
re-running evals every time you change a skill.

Tessl's Task Evals automate this: analyse a skill → generate test scenarios →
run with and without → score → report the delta.

---

## Part A — Understand what Tessl evaluates

Tessl's methodology mirrors what you did manually:

1. **Analyse the skill** — read the rules file or skill definition
2. **Generate scenarios** — create tasks the skill should influence
3. **Run with and without** — execute each scenario with the skill present and absent
4. **Score** — evaluate output quality in both conditions
5. **Report** — show per-scenario and aggregate deltas

The results produce four outcome categories:

| With skill | Without skill | Interpretation |
|------------|---------------|----------------|
| High | Low | Skill helps — keep it |
| High | High | Skill is redundant — model already handles this |
| Low | Low | Both fail — the task is hard regardless of the skill |
| Low | High | Skill hurts — it's confusing the model |

This is the same framework from Scenario 02 Part D, but applied systematically across
many scenarios instead of one.

---

## Part B — Run a Task Eval

If you have Tessl installed, evaluate one of:

- The `CLAUDE.md` from Module 07
- A custom skill from Module 03
- A workflow skill you use at work

Follow the Tessl documentation for setup and configuration. The key steps:

1. Point Tessl at the skill or rules file you want to evaluate
2. Let it generate test scenarios (or provide your own)
3. Run the eval — it will execute each scenario with and without the skill
4. Review the report

If you don't have Tessl, skip to Part D — the open-source eval format lets you
understand the structure without the tool.

---

## Part C — Interpret and act

Look at the report and answer:

1. **Which scenarios showed the biggest positive delta?** These are the tasks your skill
   helps most with. What do they have in common?
2. **Which scenarios showed zero delta?** These are tasks the model handles well without
   help. Do the corresponding rules need to exist?
3. **Any negative deltas?** These are the most interesting results — tasks where your
   skill made things worse. What's the rule doing that confuses the model?
4. **What's the overall pass rate?** Not every scenario needs to pass. A skill with a
   70% pass rate that solves real problems is better than a skill with 95% that only
   covers things the model already does well.

Use the results to revise the skill. Remove rules tied to zero-delta scenarios.
Investigate and fix rules tied to negative deltas. Re-run the eval after revisions.

---

## Part D — The Harbor eval format

Tessl's eval format (Harbor) is open source. Understanding it is useful even if you
don't use Tessl, because it shows what a structured, repeatable eval looks like.

A Harbor eval has three files:

### `instruction.md`
The task to perform — what you'd paste into a chat session:

```markdown
Fix the filter_by_priority function in sample-project/tasks.py.

The function currently uses >= comparison on priority order values, which means
filtering by "medium" returns medium AND high priority tasks. It should return
only tasks matching the exact priority level requested.
```

### `task.toml`
Metadata about the eval — what it tests, how many trials to run:

```toml
version = "1.0"

[task]
name = "fix-filter-by-priority"
description = "Fix the priority comparison operator in filter_by_priority"

[task.settings]
trials = 5
timeout = 120
```

### `tests/test.sh`
The scoring script — an automated rubric:

```bash
#!/bin/bash
set -e

cd sample-project

# Test 1: filter_by_priority uses == not >=
grep -q 'def filter_by_priority' tasks.py
# Check the function body uses direct equality, not PRIORITY_ORDER comparison
python3 -c "
import ast, inspect
import tasks
source = inspect.getsource(tasks.filter_by_priority)
assert '>=' not in source, 'Still uses >= comparison'
print('PASS: uses equality comparison')
"

# Test 2: filtering by "medium" returns only medium tasks
python3 -c "
from tasks import filter_by_priority, create_task
tasks = [
    create_task('a', priority='low'),
    create_task('b', priority='medium'),
    create_task('c', priority='high'),
]
result = filter_by_priority(tasks, 'medium')
assert len(result) == 1, f'Expected 1 task, got {len(result)}'
assert result[0]['priority'] == 'medium'
print('PASS: medium filter returns only medium tasks')
"

# Test 3: filtering by "low" returns only low tasks
python3 -c "
from tasks import filter_by_priority, create_task
tasks = [
    create_task('a', priority='low'),
    create_task('b', priority='medium'),
    create_task('c', priority='high'),
]
result = filter_by_priority(tasks, 'low')
assert len(result) == 1, f'Expected 1 task, got {len(result)}'
assert result[0]['priority'] == 'low'
print('PASS: low filter returns only low tasks')
"
```

### Interpreting results statistically

A single run of this eval might pass or fail — that's not meaningful on its own. What
matters is the **pass rate over N trials**. If the fix passes 4 out of 5 trials, that's
an 80% pass rate. Run it with and without a skill, and compare:

- **With skill:** 4/5 pass (80%)
- **Without skill:** 2/5 pass (40%)
- **Delta:** +40 percentage points — the skill helps

This is the same principle from Scenarios 01–02, just automated.

---

## What to notice

- **Auto-generated scenarios vs what you'd write.** Did the tool test things you
  wouldn't have thought of? Did it miss things you consider important?
- **Surprising negative deltas.** If a well-intentioned rule made output worse, that's
  the most valuable finding — and the one you'd never get from manual testing.
- **Pass rate vs manual intuition.** If you evaluated this skill manually in Scenario 02,
  how does the automated assessment compare to your gut feeling?

---

## Reflection questions

1. Based on the eval results, how would you change your Module 07 rules file?
2. What's the minimum number of trials you'd trust for making a decision?
3. If you could only eval one skill or prompt in your workflow, which one would it be
   and why?

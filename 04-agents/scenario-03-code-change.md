# Scenario 03 — Agentic Code Change

**Requires:** Claude Code, Cursor, or similar AI coding tool

## Goal
Give an agent a code modification task and practice supervising it effectively.

## Setup
Use Claude Code (or equivalent) in a project with version control. Make sure you're
on a branch — not main — before starting. Always.

```bash
git checkout -b agent-experiment
```

If you don't have a project with suitable code, use `sample-project/` from this repo.
The `app.py` file has several endpoints that accept user input with no validation —
a good target for this exercise.

---

## The task: add input validation

Pick a function in your project that takes user-facing input (form data, API parameters,
CLI arguments). Then:

```
Read [file/function name]. This function takes user input but has no validation.

Please add input validation that:
- Checks for required fields (infer which ones are required from context)
- Validates types where appropriate
- Returns a clear error if validation fails

Before making any changes, show me what you plan to add and where.
```

The "show me your plan first" instruction is critical. Never skip it for code changes.

---

## Review the plan

When the agent shows you its plan, check:
- Is it touching only the file you specified?
- Does the validation logic make sense?
- Is the error format consistent with the rest of the codebase?

If anything looks wrong, say so before it makes changes.

---

## Approve and apply

```
That looks good. Go ahead and make the changes.
```

Or:

```
Before applying: the error format should match what's used in [other file] — consistent
with the existing pattern. Apply with that adjustment.
```

---

## After the change

```
Review what you just changed. Run any existing tests if they exist. Tell me if the
change introduces any edge cases I should be aware of.
```

---

## What to notice

- Did the agent stay within the scope you set?
- Did the "plan first" step catch anything you'd have wanted to change?
- Did the agent run tests on its own, or did you have to ask?
- What would have gone wrong if you'd said "just do it" without reviewing the plan?

---

## Scope discipline

The most common agent mistake is scope creep — the model notices related things and
"helpfully" changes them too. Train yourself to add this to any code change prompt:

```
Only modify the files explicitly mentioned. Do not refactor, rename, or improve anything
outside the immediate task scope.
```

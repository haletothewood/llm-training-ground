# Scenario 02 — Multi-Step Investigation

## Goal
Use an agent to investigate an unknown problem — where you don't know what files to look
at or what the root cause is before you start.

## Setup
Use Claude Code, Cursor, or any agent-capable tool in a project where you have a bug,
a failing test, or something that just "doesn't work" and you haven't diagnosed it yet.
If you don't have a real bug handy, use `sample-project/` from this repo — it has a
real bug in `tasks.py` waiting to be found. Jump to Part B for the prompt.

---

## Part A — With a real bug

Pick something in your project that's broken or behaving unexpectedly. Describe the
symptom, not the cause:

```
[Describe the symptom here — e.g. "The /api/users endpoint returns a 500 error when
the email field contains a + character."]

Please investigate. Start by identifying which files are likely involved based on the
project structure, then look at the relevant code and tell me what you think is
causing this. Don't fix it yet — just diagnose.
```

The "don't fix it yet" constraint is important. You want the diagnosis first so you
can validate it before the agent makes changes.

---

## Part B — Seeded investigation (sample-project/)

Navigate to `sample-project/` in this repo, then ask:

```
There is a bug in this project. The symptom: when you filter tasks by priority using
GET /tasks?priority=high, you get back more tasks than expected — tasks of other
priorities appear in the results.

Investigate. Start by identifying which files handle the filtering logic, then read
the relevant code and explain what you think is causing this. Don't fix it yet —
just diagnose and show me the exact line responsible.
```

Once the agent has diagnosed it, continue with:

```
Now propose a one-line fix. Don't apply it yet.
```

Then, if the proposal looks right:

```
Apply the fix.
```

This three-step pattern — diagnose, propose, apply — is the safest approach for any
non-trivial bug fix. Run the tests in `tests/test_tasks.py` after to confirm.

---

## What to notice

- Did the agent identify the correct root cause?
- Did it explore more files than necessary, or stay focused?
- How did it handle uncertainty? ("I think the issue is X" vs "The issue is definitely X")

---

## The diagnosis-then-fix pattern

For any non-trivial change, this is the recommended pattern:

1. **Diagnose:** "Investigate and tell me what's wrong — don't fix yet."
2. **Propose:** "Now propose a fix, but don't apply it."
3. **Fix:** "Apply the fix."

This gives you a checkpoint at each stage and prevents the agent from going down a
wrong path and making a lot of changes you then have to undo.

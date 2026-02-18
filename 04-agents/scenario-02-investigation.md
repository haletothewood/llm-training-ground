# Scenario 02 — Multi-Step Investigation

## Goal
Use an agent to investigate an unknown problem — where you don't know what files to look
at or what the root cause is before you start.

## Setup
Use Claude Code in a project where you have a bug, a failing test, or something that
just "doesn't work" and you haven't diagnosed it yet. If you don't have a real bug handy,
use the seeded one in Part B.

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

## Part B — Seeded investigation scenario

If you don't have a real bug, create one. Add this file to a project:

**`utils/sanitize.py`**
```python
import re

def sanitize_username(username):
    # Remove anything that isn't alphanumeric or underscore
    cleaned = re.sub(r'[^\w]', '', username)
    # Ensure it starts with a letter
    if cleaned[0].isdigit():
        cleaned = 'user_' + cleaned
    return cleaned
```

Then ask:

```
There's a bug in utils/sanitize.py. The function crashes in some cases but not others.
Investigate: read the file, reason about what inputs would cause a failure, and explain
the bug without running the code.
```

(Hint: what happens if `username` is an empty string?)

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

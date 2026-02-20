# Module 04 — Solutions

---

## Scenario 01 — Simple Agent Task

### What a good project brief looks like (sample-project/)

After the agent reads `README.md`, `requirements.txt`, `app.py`, `tasks.py`, and
`storage.py`:

> **Project:** A minimal HTTP task management API — create, read, update, and delete
> tasks with persistence to a local JSON file.
>
> **Stack:** Python 3, Flask 3.0.3
>
> **Main components:**
> - `app.py` — Flask routes defining the HTTP interface (GET, POST, PUT, DELETE on /tasks)
> - `tasks.py` — Business logic: creating tasks, filtering by status/priority, sorting
> - `storage.py` — File persistence layer: reads/writes tasks to `tasks.json` using stdlib json
> - `tests/test_tasks.py` — Unit tests for the business logic in tasks.py
>
> **Entry point:** `app.py` — run with `python app.py`, starts Flask dev server on port 5000

**What to notice:** The agent read 5 files to produce this. It correctly separated the
HTTP layer from business logic from persistence, rather than just listing filenames.
It inferred purpose from reading the code, not from guessing.

### Variation — constrained to 5 files

If you asked for the brief reading no more than 5 files, a good agent explicitly flags
what it couldn't determine:

> **Project:** Task management REST API (Python/Flask)
> *(Based on README.md, app.py, tasks.py, storage.py — did not read tests due to constraint)*
>
> **Could not determine:** Whether tests are passing; whether there are any known bugs
> or limitations documented; whether there is a CI configuration or deployment setup.

**What to notice:** This is the right behaviour — explicit about its uncertainty rather
than guessing. If an agent doesn't flag its uncertainty, that's a warning sign.

---

## Scenario 02 — Multi-Step Investigation (the filter_by_priority bug)

### What good diagnosis looks like

Prompt: filter by priority returns too many results. Diagnose without fixing.

> "I've identified the bug. In `tasks.py` at line 27, `filter_by_priority` uses `>=`
> instead of `==` when comparing against `PRIORITY_ORDER` values:
>
> ```python
> return [t for t in tasks if PRIORITY_ORDER.get(t["priority"], -1) >= target]
> ```
>
> `PRIORITY_ORDER` maps `low → 0`, `medium → 1`, `high → 2`. When you filter for
> `priority=high` (target=2), the condition `>= 2` is satisfied only by 'high' tasks —
> but when you filter for `priority=medium` (target=1), the condition `>= 1` matches
> both medium and high tasks. And `priority=low` (target=0) matches everything.
>
> The symptom you described — filtering by 'high' returning more tasks than expected —
> would only appear when there are tasks of other priorities in the list.
>
> The fix is one character: change `>=` to `==`."

**What to notice:**
- The agent identified the specific line and explained *why* the behaviour is wrong
- It reasoned about the symptom under specific conditions (only visible when mixed priorities exist)
- It didn't fix anything — you asked it not to, and it complied

### What poor diagnosis looks like (red flag)

> "The bug might be in the database query filtering logic. Check your SQL WHERE clause
> or ORM filter method."

This is wrong — the project uses no database, and the agent clearly didn't read the
files before answering. If you see this, the agent didn't use its tools.

---

## Scenario 03 — Agentic Code Change

### What a good plan looks like (before applying)

Prompt: add validation to the POST /tasks endpoint in app.py.

> "Here's my plan before making changes:
>
> **File:** `app.py` only
>
> **Changes to `create_task()` route:**
> 1. Check that `data` is not None (handle missing Content-Type header)
> 2. Check that `title` is present and is a non-empty string
> 3. Check that `priority`, if provided, is one of `{"low", "medium", "high"}`
> 4. Check that `status`, if provided, is one of `{"open", "in_progress", "done"}`
> 5. Return a 400 response with a descriptive message for any validation failure
>
> **What I won't touch:** `tasks.py`, `storage.py`, `tests/` — out of scope.
>
> **Error format:** `{"error": "validation failed", "detail": "<specific message>"}` —
> consistent with the 404 format already used in `delete_task()`.
>
> Does this look right, or should I adjust the error format or allowed values?"

**What to notice:**
- The agent named the exact file it will change and explicitly listed what it won't touch
- It inferred the error format from the existing codebase (consistency)
- It asked for confirmation before proceeding
- If you'd said "just do it", you'd have missed the opportunity to catch anything wrong in this plan

### What scope creep looks like (and how to stop it)

> "I've added validation to `create_task()` and while I was there I also:
> - Refactored `filter_by_priority` to use a comprehension
> - Added type hints to all functions in `tasks.py`
> - Renamed `get_task_by_id` to `find_task`..."

This is scope creep. Stop it by being explicit in every code change prompt:

```
Only modify app.py. Do not refactor, rename, or improve anything outside the immediate task.
```

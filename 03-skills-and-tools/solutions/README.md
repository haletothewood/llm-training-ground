# Module 03 — Solutions

---

## Scenario 01 — Asking the Model to Use a Tool

### Part A: Without tools

> "I don't have access to your project's files. To find out what Python packages you're
> using, you can look at your `requirements.txt`, `Pipfile`, or `pyproject.toml` file."

Or the hallucinated version:

> "Based on common Python web projects, you're likely using Flask, SQLAlchemy, requests,
> and pytest as your main dependencies."

Neither is useful. The first can't help. The second made up an answer.

### Part B: With tool access (sample-project/)

After reading `requirements.txt`:

> | Package | Version | Purpose |
> |---------|---------|---------|
> | flask | 3.0.3 | Web framework — handles HTTP routing and request/response |

**What to notice:** One package, correct version, inferred purpose from the package name.
The model didn't guess — it read the actual file and reported what it found.

### Part C: Directed tool use

A more explicit prompt:

> "Read the file `requirements.txt` in the current directory. List each package and its
> pinned version. For any package you recognise as a testing or development dependency,
> label it as 'dev'."

Response:

> "`flask==3.0.3` — production dependency (web framework)"

**Key insight:** Tool-enabled prompts are task descriptions, not questions. "What are
the dependencies?" → "Read requirements.txt and produce a table." The model stopped
guessing and started doing.

---

## Scenario 02 — Combining Tools

### Multi-tool task: dependencies → vulnerability search → summary table

Example of what a good multi-tool response looks like when you ask the model to:
1. Read `requirements.txt`
2. Check known vulnerabilities
3. Write a summary

A representative output:

> **Dependency audit — sample-project**
>
> | Package | Version | Known CVEs | Notes |
> |---------|---------|-----------|-------|
> | flask | 3.0.3 | None found | Current stable release |
>
> No vulnerabilities found in current dependency set. Flask 3.0.3 was released in
> February 2024 and is the current recommended version.
>
> *Note: I searched PyPI safety data and the CVE database. For a production audit,
> also run `pip audit` locally to check against the current Advisory Database.*

**What to notice:**
- The model chained tools (file read → web search → write) autonomously
- It appropriately noted the limitation of its search ("also run `pip audit`")
- The output is in the format you requested, not just a prose answer

---

## Scenario 03 — Using a Skill

### What /commit produces

After staging a change to `tasks.py` (fixing the `filter_by_priority` bug):

```
Fix priority filtering to match exact level instead of minimum threshold

The filter_by_priority function was using >= comparison against the
PRIORITY_ORDER numeric values, which caused "high" to return all tasks,
"medium" to return medium+high, and only "low" to return the correct subset.

Changed to == to match exact priority level.
```

**What to notice:** The message describes the *behaviour that was wrong* (>= caused
over-matching) not just the mechanical change (changed >= to ==). The `/commit` skill
checked the diff and inferred context — you didn't have to write any of that.

### Custom skill — /summarise-pr

After creating the skill file and running `/summarise-pr` on a small branch:

> ## What changed
> Added input validation to the task creation endpoint. The `POST /tasks` route now
> checks that `title` is present and non-empty, `priority` is one of the allowed values,
> and `status` is valid before persisting the task.
>
> ## Why
> The endpoint previously accepted any payload silently, storing tasks with null titles
> or invalid priority values that broke the filtering logic downstream.
>
> ## How to test
> - POST a task with no `title` field — expect 400
> - POST a task with `priority: "urgent"` — expect 400
> - POST a valid task — expect 201 with the created task
> - GET /tasks?priority=high after creating tasks — confirm only high-priority tasks appear

**What to notice:** Skills excel when the task is consistent. They break down when the
task varies significantly between invocations — a PR description for a refactor looks
very different from one for a hotfix.

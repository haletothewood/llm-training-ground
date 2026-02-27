# Task Manager — Sample Project

A small task management API built with Python and Flask.

Use this project as the target codebase for exercises in Modules 03–05. It is
intentionally small so you can understand the whole thing in a few minutes, and
intentionally imperfect so there are real things to investigate, fix, and extend.

## What it does

- Create, read, update, and delete tasks
- Filter tasks by status or priority
- Persist tasks to a local JSON file between restarts

## Project structure

```
sample-project/
├── app.py          # Flask routes (HTTP layer)
├── tasks.py        # Business logic (create, filter, sort)
├── storage.py      # Read/write tasks to disk
├── requirements.txt
└── tests/
    └── test_tasks.py
```

## Running it

```bash
pip install -r requirements.txt
python app.py
```

The server starts on `http://localhost:5000`.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/tasks` | List all tasks |
| GET | `/tasks?status=open` | Filter by status |
| GET | `/tasks?priority=high` | Filter by priority |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/<id>` | Update a task |
| DELETE | `/tasks/<id>` | Delete a task |

## Example request

```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Write tests", "priority": "high", "status": "open"}'
```

## Teaching targets

The following issues are **intentional** — placed here to give exercises something real to work with:

- `filter_by_priority` in `tasks.py` uses `>=` instead of `==` — used in Module 04 Scenario 02
- Missing input validation in `app.py` endpoints — used in Module 04 Scenario 03
- `VALID_STATUSES` and `VALID_PRIORITIES` constants in `tasks.py` are provided for learners to use when adding validation
- One failing test in `tests/test_tasks.py` that proves the priority bug exists

**Security note:** `debug=True` in `app.py` enables Flask's Werkzeug debugger, which allows arbitrary code execution via the browser. Never use `debug=True` in production.

## Notes for module exercises

- **Module 03** — ask the model to read `requirements.txt` and list dependencies
- **Module 04 Scenario 01** — use this as the project to brief
- **Module 04 Scenario 02** — there is a real bug in here; see if the agent can find it
- **Module 04 Scenario 03** — `app.py` has endpoints that accept user input with no validation

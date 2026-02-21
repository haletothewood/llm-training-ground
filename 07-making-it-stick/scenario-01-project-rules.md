# Scenario 01 — Project Rules

## Goal
Write a rules file for a real project that makes the AI follow your standards without
being reminded.

## Background

Every AI coding tool has a mechanism for persistent project-level instructions:
- **Claude Code** reads `CLAUDE.md` from the project root
- **Cursor** reads files in `.cursor/rules/`
- **GitHub Copilot** reads `.github/copilot-instructions.md`

The file names differ but the underlying idea is the same: persistent context that the
AI reads at the start of every session. Instead of re-explaining "we use pytest not
unittest" or "this project uses Flask not Django" each time, you write it once and it
applies automatically.

A good rules file is like a good `.editorconfig` — it removes an entire category of
friction without anyone having to think about it.

---

## Part A — Discover what you repeat

Open your recent AI chat history (or recall from memory). What instructions did you give
more than once? Think about:

- Language or framework preferences ("use Python 3.11+", "this is a React project")
- Testing conventions ("use pytest", "don't mock the database")
- Style rules ("no type hints on existing code", "use snake_case everywhere")
- Things the model gets wrong by default ("don't add comments to every line",
  "don't create new files unless I ask")
- Project-specific context ("the API is in `src/api/`, the tests are in `tests/`")

List at least 5 instructions you've given more than once. These are your candidate rules.

---

## Part B — Write the rules file

Using `sample-project/` (or your own project), create a `CLAUDE.md` file in the project
root. If you use a different tool, create its equivalent.

Include these sections:

1. **Project description** — one or two sentences about what this project does
2. **Tech stack** — languages, frameworks, key libraries
3. **Coding conventions** — the rules from Part A that apply to this project
4. **What NOT to do** — things the model should avoid (often the most useful section)

Keep it under 40 lines. A rules file that's too long gets the same treatment as a prompt
that's too long — the model starts averaging across it rather than following each rule
precisely.

Example structure:

```markdown
# Project rules

This is a Flask REST API for managing a bookshop inventory.

## Tech stack
- Python 3.11, Flask, SQLAlchemy, pytest
- SQLite for dev, PostgreSQL for prod

## Conventions
- All routes go in `src/routes/`. One file per resource.
- Tests mirror the source structure: `tests/routes/test_books.py`
- Use pytest fixtures, not setUp/tearDown
- No type hints on existing code — only add them to new functions

## Do not
- Create new files without being asked
- Add docstrings to functions that don't already have them
- Use `unittest` or `mock.patch` — use pytest fixtures and monkeypatch
- Suggest database migrations — flag the need and let me handle it
```

---

## Part C — Test it

Start a fresh session with the rules file in place. Give the agent a task that would
normally require one of your repeated instructions. For example:

- If you added a rule about test style, ask it to write a test
- If you added a rule about not creating files, ask it to "add a feature" and see
  whether it creates new files or modifies existing ones
- If you added a framework preference, ask a question that could go either way

Don't mention the rules. The point is to see whether the rules file changed the default
behaviour.

---

## What to notice

- Did the rules file change the quality of the first response?
- Did it prevent a mistake you've seen before?
- What's the difference between a rule that works and one the model ignores?
- Is the rules file more useful for preventing bad defaults or for establishing
  project context?

---

## Challenge

Add a rule that's *too specific*. For example:

- "Always name test files `test_*.py` and put exactly 3 assertions per test"
- "Every function must be under 10 lines"
- "Always use list comprehensions instead of for loops"

Give the model a task where that rule conflicts with good judgment. See where it follows
the rule rigidly vs where it uses judgment. Where's the line between useful constraint
and micromanagement?

This is worth exploring because the same tension shows up in real team style guides:
rules that are too vague get ignored, rules that are too specific create worse code than
no rules at all.

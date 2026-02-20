# Scenario 01 — Asking the Model to Use a Tool

## Goal
Understand how tool use changes the nature of what you ask for — and what you get back.

## Prerequisites
For this scenario you need an LLM setup that has at least one tool available. Options:
- **Claude Code** (has file read, bash, web fetch, and more)
- **ChatGPT with Code Interpreter** enabled
- **Any API setup** with a tool like `read_file` or `web_search` configured

If you don't have tool access yet, read through the scenarios and return after completing
module 04 or 05 — you'll have a working setup by then.

---

## Part A — The flat answer (no tools)

In a standard chat (no tools), ask:

```
What Python packages are listed as dependencies in my project?
```

The model will tell you it can't see your files. Or it will hallucinate an answer.
Either way: not useful.

---

## Part B — With file access (Claude Code or equivalent)

In a tool-enabled environment, navigate to the `sample-project/` directory in this repo
(or any project of your own) and ask:

```
What Python packages are listed as dependencies in this project?
Summarise them in a table: Package | Version | Purpose (infer purpose from the package name).
```

What happened? Did the model:
1. Identify the right file (`requirements.txt`, `pyproject.toml`, `setup.py`)?
2. Read it?
3. Produce the table?

---

## Part C — Directing the tool use

Sometimes you need to be more explicit about which tool to use and why:

```
Read the file requirements.txt in the current directory.
List each package and its pinned version.
For any package you recognise as a testing or development dependency, label it as "dev".
```

---

## What to notice

- When you have tools available, how does your prompt style change?
- Did the model choose the right tool without you specifying it?
- Did it make any mistakes in reading or interpreting the file?

---

## Key insight

Tool-enabled prompts are task descriptions, not questions. "What are the dependencies?"
(question) → "Read the requirements file and produce a table" (task). The model is no
longer guessing — it's doing.

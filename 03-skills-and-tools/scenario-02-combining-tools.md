# Scenario 02 — Combining Tools in One Task

**Requires:** Claude Code, Cursor, or similar AI coding tool

## Goal
Prompt the model to use multiple tools in sequence to complete a task that no single tool
could handle alone.

## Setup
Use Claude Code or any multi-tool environment. Navigate to a code project directory.

---

## The scenario

You want to understand whether a project's dependencies have any known security issues,
without running a tool like `pip audit` or `npm audit` yourself. You want the model to:

1. Read the dependency file
2. Search for any known vulnerabilities in the top packages
3. Summarise what it found

---

## Prompt

```
I want a quick security overview of this project's dependencies. Please:

1. Read the dependency file (requirements.txt, package.json, or equivalent — find it first)
2. Identify the 5 most prominent packages
3. For each one, check if there are any widely-known vulnerabilities (search if needed)
4. Give me a summary table: Package | Version | Known Issues (or "None found")

Be clear about what you were and weren't able to verify.
```

---

## What to notice

- Did the model chain the tool calls (read → search → summarise) without you specifying
  the order explicitly?
- Did it communicate uncertainty appropriately ("I couldn't verify" vs "there are no issues")?
- How long did the multi-tool task take vs a single-shot prompt?

---

## Variation — Add a write step

Extend the prompt:

```
After the table, write the summary as a markdown section called "## Dependency Security Notes"
and append it to a new file called SECURITY_NOTES.md.
```

Did the model create the file correctly?

---

## Key insight

Multi-tool tasks succeed or fail based on how well you describe the *goal*, not the *steps*.
The model figures out the steps. Your job is to make the goal unambiguous.

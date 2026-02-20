# Scenario 01 — Simple Agent Task

## Goal
Give an agent a bounded, multi-step task and observe how it plans and executes.

## Setup
Use Claude Code or any agent-capable setup. Navigate to a real project directory.
If you don't have one handy, use `sample-project/` from this repo — it's a small
Flask task manager with a clear structure, a few components, and a README.

---

## The task

```
Explore the structure of this project and give me a project brief: what does this
codebase appear to do, what are the main components, and what tech stack is it using?

Don't ask me questions — explore the files and infer the answers. Structure your
response as:

**Project:** [one-line description]
**Stack:** [languages, frameworks, major dependencies]
**Main components:** [bullet list of key directories/modules and what each does]
**Entry point:** [where execution starts, if you can find it]
```

---

## What to notice

- How many files did the agent read before answering?
- Did it read the right files (README, package.json/requirements.txt, main entry point)?
- Did it make any wrong inferences? Why?
- How different is this from just asking "what does this project do?" without tool access?

---

## Variation — constrained exploration

```
Without reading more than 5 files, give me the best project brief you can.
Be explicit about what you couldn't determine due to the constraint.
```

This teaches you something about what the agent prioritises when forced to choose.

---

## Reflection questions

1. Did the agent tell you what it was doing as it went, or just give you the final answer?
2. Would you have preferred more or less narration of its steps?
3. What would you add to the prompt to get a more useful brief for your specific use case?

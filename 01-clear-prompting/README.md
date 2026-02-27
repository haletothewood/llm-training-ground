# Module 01 — Clear Prompting

## By the end of this module you'll be able to

- Look at any prompt you wrote and identify: what context is missing, what the expected output format is, and whether it's asking for one thing or many
- Write a bug-fix prompt that gets a usable result in one shot without back-and-forth
- Use format instructions to get output you can act on directly (JSON, table, list, code)

---

## The core problem

Most people get mediocre results from LLMs not because the model is bad, but because the prompt is vague. The model can only work with what you give it.

## Key concepts

### Specificity
A prompt like "write me something about dogs" gives the model nowhere to go. A prompt like "write a 3-sentence summary of why border collies are better suited to active households than bulldogs" has a clear scope, audience, and purpose.

### Context
The model has no memory of you between sessions. It doesn't know your codebase, your team, your constraints. You have to supply that context explicitly.

### Format instructions
If you want a list, ask for a list. If you want JSON, say so. If you want short, say short. Don't leave output format to chance.

### One task at a time
Chaining five questions into one message often produces a muddled answer. Ask one thing, get the answer, then continue.

## Scenarios in this module

- [Scenario 01 — Vague vs Precise](./scenario-01-vague-vs-precise.md)
- [Scenario 02 — Context Setting](./scenario-02-context-setting.md)
- [Scenario 03 — Format Control](./scenario-03-format-control.md)

## A note on trust

Better prompts make errors easier to catch — a precise prompt produces a precise output,
and a wrong precise output is more obviously wrong than a wrong vague one. But precision
doesn't prevent errors; it just makes them more visible. Pair this module with Module 06's
verification habits, especially for any output you plan to act on directly.

## Before you move on

You're ready for module 02 when you can look at a prompt you wrote and identify: what context is missing, what the expected output format is, and whether it's asking for one thing or many.

---
*Last verified: February 2025 · Claude Sonnet 4*

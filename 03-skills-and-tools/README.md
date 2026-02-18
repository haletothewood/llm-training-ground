# Module 03 — Skills & Tools

## From answering to acting

Modules 01 and 02 were about getting better *text* out of an LLM. This module is about
getting the LLM to *do things*: read files, run code, search the web, call APIs.

## What are tools?

Tools (sometimes called "function calling" or "actions") are capabilities you give the
model to interact with the world outside the conversation. Instead of just writing an
answer, the model can:
- Read a file and answer questions about its content
- Execute code and report the result
- Search the web and synthesise what it finds
- Call an API and use the response

The model decides *when* to use a tool based on your prompt. Your job is to frame the
task in a way that makes the right tool use obvious.

## What are skills?

In Claude Code specifically, skills are reusable prompt templates invoked with a `/command`
syntax (e.g. `/commit`, `/review-pr`). They're a layer on top of tools — a shortcut for
common, well-defined tasks.

More broadly, "skill" refers to a predefined, named capability you can invoke — as opposed
to a free-form prompt.

## The mental shift

With tools, you stop asking "what should the answer be" and start asking "what should the
model *do* to arrive at the answer". You're prompting an agent, not a chatbot.

## Scenarios in this module

- [Scenario 01 — Asking the model to use a tool](./scenario-01-using-a-tool.md)
- [Scenario 02 — Combining tools in one task](./scenario-02-combining-tools.md)
- [Scenario 03 — Using a skill (Claude Code)](./scenario-03-using-a-skill.md)

## Before you move on

You're ready for module 04 when you can describe a task in terms of "what the model needs
to do" rather than "what answer you want it to give".

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

"Skill" is a general term for a predefined, named capability you can invoke — as opposed
to a free-form prompt. Different tools implement this concept differently:

- **Claude Code** — skills are `/commands` (e.g. `/commit`, `/review-pr`): reusable prompt
  templates stored in `~/.claude/skills/` or `.claude/skills/` and invoked by name.
- **Cursor** — the closest equivalent is [Rules](https://docs.cursor.com/context/rules):
  markdown files in `.cursor/rules/` that inject persistent instructions or context into
  every session (or conditionally, based on file type or trigger). Less "invoke by name",
  more "always active for this project".
- **GitHub Copilot (VS Code)** — [Custom Instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot):
  a `.github/copilot-instructions.md` file that provides persistent context to every
  Copilot chat in the workspace.

Scenario 03 in this module walks through the Claude Code implementation specifically.
The underlying principle — standardising a repeatable prompt into a reusable template —
applies in all three tools.

## The mental shift

With tools, you stop asking "what should the answer be" and start asking "what should the
model *do* to arrive at the answer". You're prompting an agent, not a chatbot.

## Scenarios in this module

- [Scenario 01 — Asking the model to use a tool](./scenario-01-using-a-tool.md)
- [Scenario 02 — Combining tools in one task](./scenario-02-combining-tools.md)
- [Scenario 03 — Using a skill (Claude Code)](./scenario-03-using-a-skill.md)

## A note on trust

Tool actions have real-world consequences — reading files is benign, but writing files,
calling APIs, or modifying state is not. Before you let the model act, ask yourself:
is this action reversible? Module 06 covers the reversibility heuristic in detail — it's
the primary filter for deciding how much autonomy to grant at each step.

## Before you move on

You're ready for module 04 when you can describe a task in terms of "what the model needs
to do" rather than "what answer you want it to give".

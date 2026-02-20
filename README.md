# LLM Training Ground

A hands-on learning path for getting comfortable with large language models — from basic prompting through to agents and MCP servers.

## Who this is for

Anyone who wants to move beyond "just chatting" with an AI and start using it as a genuinely powerful tool. Each module builds on the last, but you can jump around if you already have experience.

## Modules

| # | Module | What you'll learn |
|---|--------|-------------------|
| 00 | [How LLMs Work](./00-how-llms-work/) | **Start here** — token prediction, context windows, no memory, hallucination mechanics |
| 01 | [Clear Prompting](./01-clear-prompting/) | How to write prompts that get consistent, useful results |
| 02 | [Pro Prompts](./02-pro-prompts/) | Advanced techniques: few-shot, chain-of-thought, role prompting |
| 03 | [Skills & Tools](./03-skills-and-tools/) | Giving the LLM tools to act, not just answer |
| 04 | [Agents](./04-agents/) | Multi-step, autonomous task completion |
| 05 | [MCP Servers](./05-mcp-servers/) | Extending LLMs with external context and capabilities |
| 06 | [Critical Judgment](./06-critical-judgment/) | When to trust output, when to reset, and when not to use AI |

## Getting started

**First:** read [SETUP.md](./SETUP.md) — it covers which tools you need, how to install
Claude Code, and what the "Ctrl+Shift+V" instruction in some scenarios means.

## How to use this repo

Each module contains:
- **`README.md`** — concept overview and key ideas
- **`scenario-XX-*.md`** — a concrete task or challenge to attempt
- **`hints.md`** — nudges if you get stuck (try without first!)
- **`solutions/`** — example responses or approaches (read after attempting)

A **`sample-project/`** directory at the root contains a small Python/Flask app you can
use as a target codebase for Modules 03–05 if you don't have your own project to hand.

The scenarios are designed to be attempted live in a chat session with an LLM. Open the
scenario, paste the prompt into your model of choice, and iterate.

## Principles

- **Do, don't just read.** The point is to run the prompts and see what happens.
- **Iteration beats perfection.** A bad first prompt that you improve is more valuable than a perfect one you copied.
- **Break things intentionally.** The hints often suggest deliberate ways to make prompts fail so you understand *why* good prompts work.

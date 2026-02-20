# Module 04 — Agents

## What is an agent?

An agent is an LLM that operates in a loop: it receives a goal, takes an action (often
using a tool), observes the result, decides what to do next, and repeats until the goal
is achieved (or it gets stuck).

The key difference from a one-shot prompt: **the model reasons about intermediate results
and adapts its plan**. You're not scripting every step — you're setting a goal and
letting the model figure out the path.

## Why agents are more powerful — and more risky

**More powerful:** An agent can handle tasks with unknown intermediate steps. "Refactor
all the code that uses this deprecated API" doesn't have a fixed number of steps — the
agent finds them, edits them, checks its work, and continues.

**More risky:** The agent is making decisions autonomously. A bug in your goal description
or an edge case the model doesn't handle well can cascade. Always set a clear scope.

## Key concepts

### Goal vs plan
You give the agent a goal. It generates the plan. If the plan is wrong, say so and let
it re-plan — don't try to micro-manage the steps.

### Checkpoints
For any task that touches things you care about (files, databases, external services),
ask the agent to checkpoint: "Before making changes, show me what you're going to do."

### Scope constraints
"Refactor everything" is dangerous. "Refactor the files in `src/api/` only, do not touch
tests" is a bounded task the agent can execute safely.

### Interruption
You can and should interrupt an agent mid-task if it's going in the wrong direction.
Better to course-correct early than to undo 20 automated changes.

## Scenarios in this module

- [Scenario 01 — Simple Agent Task](./scenario-01-simple-agent.md)
- [Scenario 02 — Multi-Step Investigation](./scenario-02-investigation.md)
- [Scenario 03 — Agentic Code Change](./scenario-03-code-change.md)

## A note on trust

Agents can fail silently. Unlike a chat response that's obviously wrong, an agent can
complete a multi-step task, report success, and have made subtly incorrect changes that
only surface later. The more autonomous the agent, the more important it is to verify
its output — not just review its plan. Module 06's verification patterns matter most
in the agentic context. See also the "Detecting silent failures" section in
[hints.md](./hints.md).

## Before you move on

You're ready for module 05 when you understand the difference between "prompt the model"
and "give the agent a goal" — and when you're comfortable letting the model take multiple
steps autonomously in a bounded scope.

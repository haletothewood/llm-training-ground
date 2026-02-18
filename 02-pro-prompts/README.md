# Module 02 — Pro Prompts

## What makes a prompt "pro"

Module 01 was about clarity. This module is about techniques that unlock qualitatively different behaviour from the model: better reasoning, more consistent output, and responses shaped to a specific persona or style.

## Key techniques

### Few-shot prompting
Show the model examples of what you want before asking for the real thing. Instead of describing the format, demonstrate it. The model will pattern-match.

### Chain-of-thought (CoT)
Ask the model to think step-by-step before giving its answer. This dramatically improves accuracy on anything involving reasoning, maths, or multi-step logic. The phrase "Think step by step" or "reason through this before answering" is often enough.

### Role prompting
Assign the model a specific persona: an expert, a critic, a rubber duck. This shapes its vocabulary, assumptions, and the angle it takes. Combined with context, it's powerful.

### Self-critique / reflection
Ask the model to answer, then critique its own answer, then revise. You get a better output in one conversation than you'd get from a single pass.

### Prompt chaining
Break a complex task into a sequence of prompts where each output becomes input to the next. More reliable than one giant prompt for complex tasks.

## Scenarios in this module

- [Scenario 01 — Few-Shot](./scenario-01-few-shot.md)
- [Scenario 02 — Chain of Thought](./scenario-02-chain-of-thought.md)
- [Scenario 03 — Role Prompting](./scenario-03-role-prompting.md)
- [Scenario 04 — Self-Critique](./scenario-04-self-critique.md)

## Before you move on

You're ready for module 03 when you can choose the right technique for a given task without having to think too hard about it.

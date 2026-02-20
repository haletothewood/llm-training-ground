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

## Further reading

- [Prompt Engineering Guide](https://www.promptingguide.ai/) — DAIR.AI's comprehensive reference for prompting techniques, with examples across models. Good as a lookup reference once you know the technique names from this module.

- [Anthropic's prompt engineering documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — Claude-specific guidance, but the underlying principles (few-shot, CoT, role prompting) transfer directly to other models. Covers some techniques not in this module.

- [OpenAI's prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) — GPT-specific but covers the same core techniques from a different angle. Useful for seeing how the same ideas are framed across providers.

## A note on trust

Chain-of-thought and self-critique make the model's reasoning visible — which is useful,
but also creates a new risk: the reasoning can look thorough and still be wrong. Module 06
examines this deliberately, using self-critique as a case study in what "visible reasoning"
does and doesn't guarantee. Keep that in mind as you practise these techniques.

## Before you move on

You're ready for module 03 when you can choose the right technique for a given task without having to think too hard about it.

One context shift to flag before you continue: from Module 03 onwards, you're directing
an agent with file and action access — not just a chat responder. The prompting instincts
from Modules 01 and 02 transfer directly, but the stakes change. A poorly scoped prompt
in a chat session produces a bad text response. A poorly scoped prompt to an agent can
modify files, call APIs, or take actions that are hard to reverse.

# Module 06 — Critical Judgment

## By the end of this module you'll be able to

- Spot context degradation in a live conversation and know when to start fresh
- Apply the reversibility heuristic to decide how carefully to review any given AI output
- Use the "prove it" and "show your sources" prompts to expose model confabulation
- Categorise a task as high-trust or low-trust before delegating it to AI

---

## Why this module exists

The previous modules covered how to use AI effectively. This one covers something harder:
knowing when not to, when to distrust what it tells you, and when the context you're
working in has quietly degraded to the point where the output is unreliable.

Most AI-related mistakes don't come from bad prompting. They come from treating AI output
as a fact when it's a hypothesis, or continuing in a broken context because starting fresh
feels like giving up.

## Key concepts

### Context poisoning
A conversation is an append-only log. Every exchange accumulates — including contradictions,
corrections, and drift. A model has to reconcile everything in that log each time it
responds. Long enough, and the context becomes a liability: the model averages across
conflicting signals rather than following your actual intent.

### Output plausibility vs correctness
Confident prose does not mean correct facts. A model will assert a file path, an API
signature, a historical date, or a library version with exactly the same tone whether
it's read it or fabricated it. You need habits for telling the difference.

### Task suitability
AI is genuinely excellent at some tasks and actively dangerous at others. The difference
is not always obvious. Learning to categorise before you start — "is this a task where
an error is cheap and reversible, or expensive and hard to detect?" — is a meta-skill
worth developing deliberately.

### Reversibility
Before delegating a task to AI, ask: if this output is wrong, how bad is it? Writing
boilerplate you'll review anyway is low-risk. Generating a security policy you'll paste
straight in is high-risk. The reversibility heuristic lets you calibrate trust to stakes.

## Scenarios in this module

- [Scenario 01 — When to Reset](./scenario-01-context-management.md)
- [Scenario 02 — Trust but Verify](./scenario-02-validate-and-verify.md)
- [Scenario 03 — Knowing When to Use AI](./scenario-03-judgment-calls.md)

## Before you move on

You're ready to call this module done when you have a reliable answer to three questions
before you start any AI-assisted task:

1. Is this context fresh enough to trust?
2. Will I be able to verify the output independently?
3. What's the cost if the output is wrong, and have I set up enough friction to catch it?

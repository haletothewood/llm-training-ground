# Module 00 — How LLMs Work

> **Start here.** This module has no exercises — read it once before doing anything else.
> The concepts here explain *why* the advice in Modules 01–05 works, and when it fails.

## By the end of this module you'll be able to

- Explain in one sentence why hallucination is a structural property, not a fixable bug
- Describe what happens to earlier context in a long conversation
- Explain why two runs of the same prompt produce different output

---

## What is the model actually doing?

### Token prediction

An LLM does not "think" or "reason" in the human sense. At every step it picks the most
statistically probable next token — a token being a word, word fragment, or punctuation
mark — given everything that came before it.

This has a practical consequence: **the model will confidently produce text that sounds
right whether or not it is right**. Fluency and accuracy are independent properties.
A well-formed sentence is not evidence that the sentence is true.

This is why Module 06 exists, and why verification is not optional.

### The context window

Every time the model generates a response, it reads the entire conversation from the
beginning — your system prompt (if any), every message you sent, every response it gave.
There is no compressed "memory" of earlier turns. It's a fresh read of the full transcript,
bounded by a maximum length called the **context window**.

Two consequences for your workflows:

- **Early context matters.** What you establish in the first message shapes how the model
  interprets everything that follows. Module 01 (context setting) is anchored here.
- **Long conversations degrade.** Once the context window fills, older content gets dropped
  or compressed. A conversation that started well can go wrong not because the model
  "forgot" — it literally can no longer see what you said earlier.

### No persistent memory between sessions

When you close a chat and start a new one, the model has no record of the previous
conversation. None. It does not know your name, your codebase, your preferences, or
anything you told it last week.

Any "memory" you see in AI products is a feature built on top of the base model — not
a property of the model itself. Someone is retrieving prior context and injecting it
back into the prompt.

This is why Module 01's guidance on explicit context is not just good practice — it's
load-bearing. Every session is a blank slate.

### Non-determinism

Given the same prompt, the model will almost certainly produce a different output each
time. Temperature — a parameter that controls how much randomness is injected — is the
main dial, but even at temperature 0 (minimum randomness) you will see variation.

For production use this matters: you cannot assume a prompt that worked yesterday will
produce identical output tomorrow. Module 02's few-shot and self-critique techniques help
constrain variance, but they don't eliminate it.

### Why hallucination sounds confident

The model optimises for producing fluent, coherent text. When it doesn't "know" something
(in the statistical sense — it has no relevant training signal), it does not return an
error. It produces a plausible-sounding continuation. That continuation may be a real
fact, a plausible-but-wrong fact, or an entirely fabricated one — and the output looks
identical in all three cases.

This is not a bug the model will eventually fix. It is a structural property of token
prediction. The only reliable mitigation is external verification, which Module 06
treats in depth.

---

## Where this connects

| Concept | Relevant modules |
|---------|-----------------|
| Context window | Module 01 (context setting), Module 06 (context poisoning and reset) |
| No persistent memory | Module 01 (supplying context explicitly), Module 06 (why sessions drift) |
| Token prediction / hallucination | Module 06 (verification habits, when to trust output) |
| Non-determinism | Module 02 (few-shot consistency, self-critique), Module 06 |
| Tool use has real-world effects | Module 03 (tools), Module 04 (agents), Module 05 (MCP), Module 06 (reversibility) |

---

## Further reading

These are widely-used resources for going deeper on the concepts above. Listed roughly
from visual/accessible to technical.

- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) — Jay Alammar's visual walkthrough of the transformer architecture underlying all modern LLMs. No maths required to get the intuition.

- [Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/@AndrejKarpathy) — Andrej Karpathy's YouTube channel. His "Let's build GPT" video (~2 hours) constructs a working language model from first principles. The single best way to internalise what token prediction actually means in code.

- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course/) — Free course from Hugging Face. Chapter 1 covers the transformer model family conceptually; later chapters cover practical model use, fine-tuning, and evaluation.

- [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) — Google's free ML fundamentals course. Useful background if you want the statistical learning context that LLMs sit on top of.

- [Anthropic Research](https://www.anthropic.com/research) — Anthropic's published research, including their mechanistic interpretability work ("what is the model actually doing internally?") and alignment research. More technical, but directly relevant to understanding why LLMs behave as they do.

---
*Last verified: February 2025 · Claude Sonnet 4*

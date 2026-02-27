# Scenario 02 — Trust but Verify

**Requires:** any chat interface

## Goal
Build reliable habits for treating AI output as a hypothesis rather than a fact — and
learn the prompting patterns that make verification easier.

## Background

AI output sounds confident by default. The model uses the same tone whether it has
read the relevant file ten seconds ago or is confabulating a plausible-sounding answer
from training data. There is no audible difference between "I know this" and "I believe
this based on patterns in my training data."

The practical implication: every factual claim in an AI response — a file path, a
function signature, a library version, a behaviour — needs to be verified against a
ground-truth source before you rely on it. The question is how to make that verification
as cheap as possible.

---

## Part A — Expose the reasoning

Ask for any explanation of something in your codebase:

```
Explain how [some function or module in your codebase] works.
```

Then follow up with this:

```
Walk me through every step of your reasoning. For each claim you made, tell me:
1. Did you read that directly from the files, or is it an inference?
2. If it's an inference, what are you basing it on?
3. What would change your answer if it turned out to be wrong?
```

You're not trying to catch the model out. You're forcing it to distinguish between
"I read this" and "I inferred this" — and surfacing where the uncertainty actually lives.

---

## Part B — Show your sources

When a model makes a specific factual claim about your codebase, ask for direct evidence:

```
You said [specific claim]. Show me the exact line(s) from the file that support that.
Include the file path and line number.
```

A model that has actually read the file will reproduce the relevant lines accurately.
A model that is confabulating will either:
- Produce lines that don't exist
- Quote lines that exist but don't support the claim
- Hedge and become suddenly vague ("the implementation likely does…")

The vagueness after a direct challenge is often the clearest signal.

---

## Part C — The "prove it" pattern

This exercise applies the technique to a real file.

Pick any file in a codebase you own. Then ask the model:

```
Read [file path] and tell me what the function [function name] does.
```

Once it answers, run the prove-it challenge:

```
Quote the exact line(s) from [file path] that tell you [specific claim from the answer].
Do not paraphrase — copy the exact text.
```

Then open the file yourself and check whether the quote exists, and whether it says
what the model claims it says.

If the model can't produce a direct quote but maintains the claim, that's a confabulation.

---

## Distinguishing claim types

Not all model claims carry the same risk. It's useful to sort them before deciding
how hard to verify:

| Claim type | Example | Risk |
|------------|---------|------|
| Read from context | "This function on line 42 does X" | Low — verify against file |
| Inferred from code | "This probably follows the observer pattern" | Medium — check the pattern |
| From training data | "React 18 introduced concurrent rendering" | High — check the docs |
| Confabulated | "The `useCache` hook is defined in utils/cache.ts" | Very high — may not exist |

The most dangerous claims are the last category, because they're indistinguishable in
tone from the first. The prove-it pattern exposes them.

---

## What to notice

- Did the model distinguish "read" from "inferred" when you asked in Part A?
- In Part B, did the quote match the actual file?
- How did the model behave when challenged on a claim it couldn't support?

---

## Reflection questions

1. What's the difference between a model being wrong and a model confabulating? Does
   the distinction matter for how you respond?
2. In Part C: if the quote was accurate, does that mean everything else in the answer
   was accurate? Why or why not?
3. How would you adapt the "prove it" pattern for claims about external APIs or
   libraries (where you can't open the file yourself)?

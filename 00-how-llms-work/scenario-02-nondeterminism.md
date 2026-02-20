# Scenario 02 — Non-Determinism

> **Optional.** This scenario is for developers who want to see output variance first-hand,
> which is a prerequisite for understanding why consistency techniques matter.

---

## Part A — Same prompt, different outputs

Pick a prompt with a judgment call in it — something where there are multiple valid
answers. Try this one:

```
What's the best way to handle errors in an async Node.js function?
Give me one concrete recommendation in 2–3 sentences.
```

Run it **three to five times** without changing anything. Copy each output.

**What to observe:**
- Does the model always recommend the same pattern (e.g. try/catch vs `.catch()`)?
- Does the phrasing vary substantially, or just superficially?
- Does the level of detail vary?
- Does any run contradict another?

For a factual lookup question ("what is the HTTP status code for not found?") variance
will be low. For a recommendation or stylistic judgment, variance will be much higher.

---

## Part B — Does "think step by step" stabilise output?

Take the same prompt and add a chain-of-thought instruction:

```
What's the best way to handle errors in an async Node.js function?
Think step by step about the trade-offs before giving your recommendation.
Give me one concrete recommendation in 2–3 sentences.
```

Run this three to five times and compare outputs to Part A.

**What to observe:**
- Does the step-by-step reasoning lead to more consistent conclusions?
- Does adding reasoning actually change which recommendation gets made, or just how
  it's explained?
- Is the variance lower in the recommendation itself, even if the reasoning path varies?

---

## Part C — Record it yourself

Run the Part A prompt five times. After each run, write down the **core recommendation**
in one line (e.g. "use try/catch" or "use .catch()"). Don't paraphrase — just the key
advice.

```
Run 1:
Run 2:
Run 3:
Run 4:
Run 5:
```

Then do the same for the Part B (step-by-step) prompt.

```
Run 1:
Run 2:
Run 3:
Run 4:
Run 5:
```

Count how many unique recommendations you got from each. The ratio — unique answers ÷
total runs — is a rough measure of variance. Lower is more consistent.

This exercise is worth doing once with a real prompt from your own work.

---

## What to take from this

- Output is not deterministic. A prompt that "worked" is a sample, not a guarantee.
- For tasks where you need consistency (classification, extraction, formatting), use
  few-shot examples and explicit format instructions — not just a well-worded instruction.
- For reasoning tasks, chain-of-thought tends to reduce variance in the conclusion even
  when the reasoning steps differ. This is why Module 02 covers CoT before self-critique.
- If you need reproducibility in production, treat each LLM call as a hypothesis to
  verify, not a function call with a deterministic return value.

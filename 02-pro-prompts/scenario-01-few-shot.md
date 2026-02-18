# Scenario 01 — Few-Shot Prompting

## Goal
Use examples to teach the model a format or style it couldn't easily infer from a description alone.

## Background
Few-shot prompting means providing 2–5 examples of input→output pairs before your real request. The model learns the pattern from the examples rather than from instructions.

---

## Part A — Zero-shot (no examples)

```
Classify the sentiment of the following customer review as Positive, Negative, or Neutral,
and give a one-sentence reason.

Review: "The delivery was fast but the packaging was completely crushed."
```

What did you get? Was the format consistent with what you needed?

---

## Part B — Few-shot (with examples)

```
Classify the sentiment of customer reviews. Use this exact format:

Review: "Absolutely loved it, will buy again!"
Sentiment: Positive
Reason: Customer expresses strong satisfaction and repeat purchase intent.

Review: "It works, I guess. Nothing special."
Sentiment: Neutral
Reason: Customer acknowledges functionality but shows no enthusiasm.

Review: "Worst purchase I've ever made. Broke on day one."
Sentiment: Negative
Reason: Customer reports product failure and expresses strong dissatisfaction.

---

Now classify this one:

Review: "The delivery was fast but the packaging was completely crushed."
```

---

## What to notice

- Did the few-shot version produce output in exactly the format of the examples?
- Did it handle the ambiguous "mixed" review differently in Part A vs Part B?
- Try running Part B 3 times — is the format more consistent than Part A's 3 runs?

---

## Challenge

Think of a classification, tagging, or formatting task you do repeatedly. Write a few-shot
prompt with 3 examples. Run it on 5 real inputs and check consistency.

## When to use few-shot

- You need a very specific output format
- The task is hard to describe but easy to demonstrate
- You need consistency across many runs
- Zero-shot results are inconsistent or off-format

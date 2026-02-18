# Scenario 02 — Chain of Thought

## Goal
Use step-by-step reasoning prompts to improve accuracy on tasks that require logic or inference.

## Background
LLMs are next-token predictors. When you ask for a final answer directly, the model has to arrive at it in one jump. Asking it to reason step-by-step gives it "working memory" — each step informs the next, and errors are caught earlier.

---

## Part A — Direct answer

```
A project has 4 developers. Each developer takes 3 days to complete one feature module.
The project needs 10 modules. Two developers will be on leave for the first 6 days.
How many days will the project take to complete?
```

Note the answer. Is it right? Did the model show its working?

---

## Part B — Chain of thought

```
A project has 4 developers. Each developer takes 3 days to complete one feature module.
The project needs 10 modules. Two developers will be on leave for the first 6 days.

Think through this step by step before giving your final answer:
1. How many modules can be completed in the first 6 days?
2. How many modules remain after day 6?
3. How long does the remainder take with all 4 developers?
4. What is the total project duration?
```

---

## Part C — Zero-shot CoT (the magic phrase)

You don't always need to specify the steps. Sometimes this is enough:

```
A project has 4 developers. Each developer takes 3 days to complete one feature module.
The project needs 10 modules. Two developers will be on leave for the first 6 days.

Think step by step, then give your final answer.
```

---

## What to notice

- Did Part A get the right answer? Did Part B or C catch an error Part A made?
- In Part B, were the model's intermediate steps correct even if its final answer had a mistake?
- Which version would you trust more if you couldn't verify the answer yourself?

---

## When to use chain of thought

- Maths or estimation problems
- Multi-step reasoning ("if X, then Y, therefore Z")
- Debugging ("why is this code producing this output")
- Any time accuracy matters more than speed

---

## Challenge

Find a recent decision you made that required several steps of reasoning (e.g. choosing a technology, estimating a cost, diagnosing a problem). Write a chain-of-thought prompt to re-examine it. Did the model agree with your conclusion, or surface something you missed?

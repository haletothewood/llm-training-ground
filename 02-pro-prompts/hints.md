# Module 02 — Hints

## Choosing the right technique

| Situation | Technique |
|-----------|-----------|
| Need consistent format across many runs | Few-shot |
| Task involves multi-step reasoning or maths | Chain of thought |
| Need domain expertise or a specific tone | Role prompting |
| First pass wasn't good enough | Self-critique |
| Task is too complex for one prompt | Prompt chaining |

## Combining techniques

These aren't mutually exclusive. A strong prompt might:
- Assign a role (who the model is)
- Provide a few examples (what the output looks like)
- Ask for step-by-step reasoning (how to get there)

Example:
```
You are a senior data analyst. Think step by step.

Here are two examples of how I write data insights:

Example 1:
Data: [...]
Insight: Revenue grew 12% MoM driven primarily by enterprise segment expansion.

Example 2:
Data: [...]
Insight: Churn rate spiked to 8% in Q3, concentrated in the SMB tier.

Now write an insight for this data:
[YOUR DATA HERE]
```

## Common mistakes in this module

**Role without substance:** "You are an expert" without specifying *what kind* of expert
or what the expert should care about adds little value.

**Too many steps at once:** Chain-of-thought works because steps build on each other.
If you specify 10 steps upfront, the model tries to anticipate all of them at once,
which defeats the purpose.

**Skipping the critique step:** It's tempting to take the first answer. Don't. One
round of self-critique often produces the biggest quality jump.

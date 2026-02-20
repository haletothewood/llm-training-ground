# Scenario 03 — Knowing When to Use AI

## Goal
Develop a reliable framework for deciding when AI is genuinely useful, when it's
a liability, and when you're better off just reading the docs.

## Background

The most common AI mistake isn't a bad prompt — it's using AI for the wrong task.
A model that's brilliant at explaining unfamiliar code and generating test scaffolding
can be actively dangerous when writing security policy or generating financial logic
you can't independently verify.

The difference is not about model quality. It's about the nature of the task.

---

## Where AI genuinely excels

These task types have a high hit rate across most models:

- **Boilerplate generation** — CRUD endpoints, test fixtures, config files, serialisation
  code. The patterns are well-established and easy to review.
- **Explaining unfamiliar code** — summarising what a function does, translating a design
  pattern, explaining what a regex matches. You can verify the explanation against the code.
- **First drafts** — documentation, PR descriptions, commit messages, technical emails.
  The output needs editing but saves the hardest part: the blank page.
- **Test scaffolding** — generating test cases for known-good logic, particularly edge
  cases and boundary conditions you might not think of.
- **Format translation** — converting between JSON and YAML, reformatting data structures,
  translating SQL to a query builder syntax. Mechanical, verifiable.

---

## Where it's risky

These task types have a much higher failure rate — not because the model is lazy, but
because the task structure makes errors hard to catch:

- **Security-critical logic** — authentication, authorisation, cryptography, input
  sanitisation. Errors here are often invisible in review and catastrophic in production.
- **Financial or legal logic** — precision matters, domain knowledge is deep, and the
  model's training data may be outdated or wrong for your jurisdiction.
- **Code you can't explain** — if the model generates something you don't understand
  well enough to review, you're not using AI to accelerate your work; you're outsourcing
  your judgment to a model that can't be held accountable.
- **Confident-wrong domains** — areas where the model produces fluent, plausible output
  but has unreliable training data: niche frameworks, recent API changes, obscure
  library behaviour, your internal codebase.

---

## The reversibility heuristic

Before using AI on any task, ask: **if this output is wrong, how bad is it?**

| Output type | Reversibility | Appropriate trust |
|-------------|--------------|-------------------|
| A draft you'll rewrite anyway | Easy | High |
| Boilerplate you'll review line-by-line | Easy | High |
| Test cases (for code you own) | Easy | High |
| Refactored code with full test coverage | Medium | Medium |
| Documentation that others will read | Medium | Medium |
| Config changes in production | Hard | Low |
| Security logic | Hard | Low |
| Anything you paste in without reading | Hard | None |

The table is a starting point, not a rulebook. The key question is always: have I
set up enough independent verification to catch an error before it costs me?

---

## The "just read the docs" threshold

There's a point at which reaching for AI is slower and less reliable than reading the
primary source. If you find yourself:

- Asking the model to describe a public API that has official documentation
- Re-asking the same question multiple times because the answer keeps being slightly wrong
- Asking about something released recently enough that the model's training data might
  not include it

...you've crossed the threshold. The documentation is faster, ground-truth, and doesn't
hallucinate. AI is a useful layer on top of documentation; it's a poor substitute for it.

---

## Part A — Audit your last five AI uses

Think back to the last five times you used AI in your work. For each one, answer:

1. Which category above does the task fall into — excels, risky, or docs threshold?
2. Did you verify the output independently?
3. If the output was wrong, would you have caught it? How?

You're not looking for a perfect score. You're building a map of your actual patterns
vs your instincts about when AI is safe.

---

## Part B — Invert the flow

For your next technical task involving an unfamiliar library or API:

**Normal flow:** ask the model, use the output, maybe verify.

**Inverted flow:**
1. Read the official documentation first — even briefly, just the relevant section.
2. Form your own understanding: "I think this works by…"
3. Then ask the model: "Does this match your understanding? What am I missing?"

Compare what you get. The inverted flow often surfaces model errors that you'd have
missed if you'd let the model go first, because you now have an independent reference
point.

---

## Part C — Reversibility as a one-week habit

For one week, before using AI on any task, state the reversibility out loud (or write it):

> "If this output is wrong and I don't catch it, the consequence is: [X]."

This single step — naming the consequence before you start — changes how carefully
you review the output. Track how many times naming the consequence made you more
careful than you would have been otherwise.

---

## What to notice

- Did the Part A audit reveal any patterns you weren't aware of?
- In Part B: did the inverted flow change what you asked, or what you noticed in the answer?
- After Part C: did naming the reversibility upfront change your review behaviour?

---

## Reflection questions

1. Is there a task type you currently use AI for that belongs in the "risky" column?
   What would you change about how you use it there?
2. What's the difference between "I can't explain this code" and "this code is complex"?
   Why does that distinction matter for AI use?
3. The reversibility heuristic puts "config changes in production" in the hard-to-reverse
   column. What safeguards would move it to medium?

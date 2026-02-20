# Scenario 04 — Self-Critique and Reflection

## Goal
Use a multi-step conversation to get the model to evaluate and improve its own output.

## Background
A single-pass LLM response is the model's best guess given your prompt. But the model can
also critique, revise, and reflect — effectively acting as its own reviewer. This is
especially useful for writing, plans, and arguments where quality matters more than speed.

---

## The basic pattern

Instead of one prompt, use a sequence:

1. **Generate** — ask for an initial response
2. **Critique** — ask the model to find weaknesses in what it just wrote
3. **Revise** — ask it to rewrite with those weaknesses addressed

---

## Scenario — Improving a proposal paragraph

### Step 1: Generate

```
Write a short paragraph (4–5 sentences) pitching the idea of switching our team's
deployment process from manual SSH to a CI/CD pipeline. The audience is a non-technical
engineering manager who cares about reliability and developer time.
```

Copy the output (use Ctrl+Shift+V to paste so the model doesn't use the file as context).

### Step 2: Critique (paste the output in)

```
Here is a paragraph I'm going to send to an engineering manager:

[PASTE OUTPUT HERE - use Ctrl+Shift+V to paste]

Act as a critical editor. What are the weaknesses of this paragraph? Is it too jargon-heavy?
Does it actually address what the manager cares about? Is the value proposition clear?
Give me 3 specific things to improve.
```

### Step 3: Revise

```
Using those 3 improvements, rewrite the paragraph. Keep it concise.
```

---

## What to notice

- Was the revised paragraph noticeably better than the first?
- Did the critique surface issues you would have spotted yourself?
- Did the critique miss anything important?

---

## Shortcut version

You can compress all three steps into one prompt:

```
Write a short paragraph pitching CI/CD adoption to a non-technical engineering manager.
After writing it, critique it for clarity and persuasiveness, then write a revised version
that addresses those critiques.
```

Try both approaches and compare.

---

## Challenge

Take a piece of writing you've already written (an email, a doc, a PR description). Paste
it in (use Ctrl+Shift+V to paste so the model doesn't use the file as context) and ask the model to critique it, then revise it. How much did it improve?

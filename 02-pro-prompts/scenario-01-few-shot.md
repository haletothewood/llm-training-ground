# Scenario 01 — Few-Shot Prompting

## Goal
Use examples to teach the model a format or style it couldn't easily infer from a description alone.

## Background
Few-shot prompting means providing 2–5 examples of input→output pairs before your real request. The model learns the pattern from the examples rather than from instructions.

---

## Part A — Zero-shot (no examples)

Copy the prompt (use Ctrl+Shift+V to paste so the model doesn't use the file as context).
```
Classify the following git commit message into one of these types:
feat, fix, refactor, docs, chore.
Give a one-sentence reason.

Commit: "Update readme with installation steps"
```

What did you get? Was the format consistent with what you'd want if you were processing many commits?

---

## Part B — Few-shot (with examples)

Copy the prompt (use Ctrl+Shift+V to paste so the model doesn't use the file as context).
```
Classify git commit messages into: feat, fix, refactor, docs, chore.
Use this exact format:

Commit: "Add OAuth2 login flow"
Type: feat
Reason: Introduces new user-facing authentication functionality.

Commit: "Fix null pointer in session middleware"
Type: fix
Reason: Corrects a defect causing crashes in existing behaviour.

Commit: "Extract token validation into separate module"
Type: refactor
Reason: Restructures existing code without changing its external behaviour.

---

Now classify these:

Commit: "Remove deprecated getUserById calls"
Commit: "Handle empty array edge case in sortUsers"
Commit: "Update readme with installation steps"
```

---

## What to notice

- Did the few-shot version produce output in exactly the format of the examples?
- Did it classify all three commits with the same Type/Reason structure?
- Try running Part B 3 times — is the format more consistent than Part A's 3 runs?
- For the "Remove deprecated getUserById calls" commit: did it pick `refactor` or `chore`?
  Run it a few times and see if the answer is stable.

---

## Challenge

Think of a classification or tagging task you do repeatedly in your workflow — PR labels,
issue triage, log severity, API response codes. Write a few-shot prompt with 3 examples.
Run it on 5 real inputs and check consistency.

## When to use few-shot

- You need a very specific output format
- The task is hard to describe but easy to demonstrate
- You need consistency across many runs
- Zero-shot results are inconsistent or off-format

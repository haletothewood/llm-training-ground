# Scenario 01 — Vague vs Precise

## Goal
Experience the difference between a vague and a precise prompt producing very different outputs from the same model.

## Part A — The vague version

Paste this into your LLM (use Ctrl+Shift+V to paste so the model doesn't use the file as context) and note the response:

```
Fix the bug.
```

Take note of: How many assumptions did the model make? Did it ask you clarifying questions or just guess? Was the output actionable at all?

---

## Part B — The precise version

Now paste this (use Ctrl+Shift+V to paste so the model doesn't use the file as context):

```
In src/auth/token.ts, the function validateToken(token: string) currently throws
a TokenExpiredError (from the jsonwebtoken library) when the token has expired.

The expected behaviour is: return false when the token is expired, rather than
throwing. Return true when the token is valid.

Constraints:
- Do not change the function signature
- Do not add any new dependencies

Fix only this function. Do not modify anything else.
```

Compare the two outputs.

---

## What to notice

- Which one required more back-and-forth?
- Which output was closer to usable without editing?
- In Part A, did the model invent a plausible-sounding bug and fix? How would you know if it was right?
- How many words did the precise prompt add? Was it worth it?

---

## Challenge

Take the vague prompt from Part A and rewrite it yourself — without looking at Part B — to describe a real bug you've encountered or could imagine encountering. Include: file/function location, observed behaviour, expected behaviour, and any constraints. Run it and see if you get a usable fix in one shot.

---

## Hints

See [hints.md](./hints.md) if you want a checklist for what "specific" means in practice.

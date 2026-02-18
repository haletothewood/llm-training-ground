# Scenario 01 — Vague vs Precise

## Goal
Experience the difference between a vague and a precise prompt producing very different outputs from the same model.

## Part A — The vague version

Paste this into your LLM and note the response:

```
Help me write an email.
```

Take note of: How many assumptions did the model make? Did it ask you clarifying questions or just guess?

---

## Part B — The precise version

Now paste this:

```
Write a short professional email (3–4 sentences) from a project manager to a client,
explaining that the delivery date for their software project has moved from March 14th
to March 21st due to an unexpected integration issue. Keep the tone apologetic but
confident. End with an offer to jump on a call if they have concerns.
```

Compare the two outputs.

---

## What to notice

- Which one required more back-and-forth?
- Which output was closer to usable without editing?
- How many words did the precise prompt add? Was it worth it?

---

## Challenge

Take the vague prompt from Part A and rewrite it yourself — without looking at Part B — to be as specific as possible for a real email you might need to send. Run it, and see if you get a usable result in one shot.

---

## Hints

See [hints.md](./hints.md) if you want a checklist for what "specific" means in practice.

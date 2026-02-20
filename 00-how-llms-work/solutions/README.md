# Module 00 — Solutions

Module 00 scenarios are observation exercises, not prompting tasks. There is no single
correct output — the point is to observe specific behaviours. This file describes what
you should have seen, and what it means.

---

## Scenario 01 — Memory and Context

### Part A: What you should observe

The model has no memory of the previous session. A typical response:

> "I don't have access to previous conversations — each session starts fresh for me.
> I don't know your name or what project you're working on."

Or, if the model confabulates:

> "I believe you mentioned your name is Alex earlier..."

Both confirm the same thing: there is no persistent memory. The second response is
actually more concerning — the model invented a plausible answer rather than saying it
didn't know. This is hallucination in its most common form.

**If the model "remembered" correctly:** you're seeing a product feature (memory
injection), not a model property. The client retrieved the previous session and added it
to the context automatically.

### Part B: What you should observe

With a small filler block: the model likely answered `src/auth/token.ts` correctly.

With a very large filler block: accuracy drops. You might see:
- "I don't see a file mentioned" — the model can no longer "reach" the early context
- A vague answer without the specific filename
- A hallucinated filename that sounds plausible

**The key insight:** the model processes the entire context each time but doesn't weight
all of it equally. Information buried in the middle of a long context is less reliably
retrieved than information near the beginning or end. This is why long, unfocused
conversations degrade.

---

## Scenario 02 — Non-Determinism

### Part A: Sample outputs from the same prompt

Here are three real runs of "What's the best way to handle errors in an async Node.js
function? Give me one concrete recommendation in 2–3 sentences."

**Run 1:**
> Use `try/catch` blocks inside your async functions to handle errors explicitly. This
> gives you clear control over what happens when a promise rejects, and keeps error
> handling co-located with the code that might fail. Avoid relying on unhandled rejection
> warnings as a substitute for real error handling.

**Run 2:**
> Wrap your async logic in a `try/catch` and rethrow or handle the error appropriately
> for your use case. For Express.js applications specifically, make sure to call `next(err)`
> to pass errors to your error-handling middleware. This keeps your error flow consistent
> across the application.

**Run 3:**
> The most reliable pattern is to use `.catch()` on the returned promise rather than
> wrapping in try/catch — this avoids accidentally swallowing synchronous exceptions
> inside the async block. Chain `.catch()` at the call site so callers decide how to
> handle failures. For critical paths, add a global `process.on('unhandledRejection')`
> handler as a last resort.

Notice: Run 1 and Run 2 agree (try/catch). Run 3 recommends the opposite (`.catch()`).
The model isn't wrong in any individual run — both patterns have merit — but a developer
who runs this once gets one answer and assumes it's the consensus.

### Part B: What step-by-step reasoning typically does

Adding "think step by step" tends to produce more consistent conclusions across runs,
even if the reasoning paths vary. You'll often see:

- The model considers multiple approaches before committing to one
- The recommendation tends to be less extreme (it hedges appropriately)
- Variance in the final recommendation decreases, even when the reasoning differs

This is why CoT is covered in Module 02 before self-critique — stabilising the
reasoning path is a prerequisite for self-critique to be meaningful.

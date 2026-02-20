# Scenario 01 — When to Reset

## Goal
Recognise the signals that a conversation context has degraded, and practise the habits
that prevent you from building on corrupted output.

## Background

A conversation with an LLM is not a working memory you share. It's a transcript that
the model reads from the beginning every time it replies. The longer that transcript gets,
the harder it is for the model to stay consistent — especially when the conversation
contains corrections, U-turns, or conflicting instructions.

This creates **context poisoning**: the model starts averaging across contradictory signals
rather than following your current intent. It doesn't announce this. The output just gets
gradually vaguer, more hedged, or subtly wrong.

---

## Signals that a context has degraded

Watch for these in any long-running conversation:

- **Contradiction** — the model asserts something that conflicts with what it said earlier,
  without acknowledging the conflict
- **Constraint drift** — a rule you established at the start ("always use TypeScript", "no
  external dependencies") stops being followed
- **Sycophancy** — the model starts agreeing with everything, including things it previously
  pushed back on
- **Confabulation** — details that can't be verified from the files you've shared start
  appearing in the output (made-up function names, file paths, config keys)
- **Vagueness creep** — answers that were specific early in the conversation become
  increasingly hedged and non-committal

One or two of these can be corrected in-context. All five appearing together is a signal
to start fresh.

---

## Part A — Audit a real conversation

Find a conversation with an LLM that ran longer than 10–15 exchanges — a debugging
session, a document-drafting session, anything that went back and forth for a while.

Read through it and look for the signals above. Then paste the final exchange into a
fresh context and ask the model the same question you ended with. Compare the answers.

```
[Paste the final question from your old conversation here]
```

If the fresh answer is noticeably more coherent or accurate, that's your evidence that
the old context had degraded.

---

## Part B — Deliberately poison a context

This exercise makes the degradation visible by manufacturing it.

### Step 1: Set up a rule-heavy context

Start a new conversation and paste this:

```
For this entire conversation, follow these rules strictly:
1. All code examples must be in Python 3.10+
2. Never use external libraries — standard library only
3. All function names must use snake_case
4. Every function must have a one-line docstring
5. Never return None — raise an exception instead

Confirm you've understood these rules.
```

### Step 2: Have a normal conversation (8–10 exchanges)

Ask some real questions — code help, explanations, anything. Gradually introduce some
friction: ask about things that don't quite fit the rules, request a code snippet in
a different language "just to see what it looks like", then come back. Keep going for
8–10 exchanges.

### Step 3: Check for constraint drift

At the end, paste this:

```
Write a short function that reads a file and returns its contents as a list of lines.
```

Then check the output against the rules you set in Step 1:
- Is it Python?
- Does it use only the standard library?
- Does every function have a docstring?
- Does it raise instead of returning None?

Count how many rules survived 10 exchanges. Most contexts will have lost at least one.

---

## The one-task-per-conversation principle

The most reliable fix is prevention: **use one conversation per task**. A conversation
that starts focused and ends focused is almost always better than one that grew to cover
multiple problems.

This feels inefficient. It isn't. The cost of starting a fresh context is seconds.
The cost of working in a degraded one — getting subtly wrong output and not catching it
— is much higher.

---

## Handoff pattern — extracting a reusable summary

When you do need to continue work across sessions, extract the relevant context explicitly
before you close the conversation. Paste this at the end of a long session:

```
Before we finish: summarise the key decisions, constraints, and open questions from
this conversation in a form I can paste into a fresh context to continue this work.
Include: the goal we were working toward, any rules or constraints that must carry
forward, the current state of any code or document we were working on, and the next
step to take.
```

Save that summary. When you start fresh, paste it at the top. The new context is now
bootstrapped with everything that matters, without the noise of everything that doesn't.

---

## What to notice

- How many exchanges did it take before constraint drift appeared in Part B?
- Were any of the signals subtle enough that you might not have caught them in real work?
- Does the "one task per conversation" principle change how you'd approach a long task?

---

## Reflection questions

1. In your Part A audit: if the context had degraded, at which exchange do you think it
   started? What was the trigger?
2. Which degradation signal is hardest to notice in the moment — and why?
3. How would you explain the handoff pattern to a colleague who thinks starting a fresh
   conversation is "wasteful"?

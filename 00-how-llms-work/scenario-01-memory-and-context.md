# Scenario 01 — Memory and Context

**Requires:** any chat interface

> **Optional.** This scenario is for developers who want to observe the no-memory and
> context-window properties directly, rather than just taking them on faith.

---

## Part A — Prove there is no persistent memory

Start a fresh chat session with your LLM. Tell it something specific and personal:

```
My name is [your name] and I'm working on a project called [project name].
Remember this for later.
```

End that session completely (close the tab, start a new conversation — whatever your
client requires to begin a blank session).

In the new session, ask:

```
What's my name and what project am I working on?
```

**What to observe:** The model has no record of the previous session. It will either say
it doesn't know, or it will make something up. Both outcomes confirm the same thing:
there is no memory between sessions.

If your client does seem to "remember" — you're seeing a product feature, not a model
property. The previous conversation was retrieved and injected into the new session's
context behind the scenes.

---

## Part B — Observe context fill degrading accuracy

This is harder to see cleanly, but worth understanding. Start a new session and paste
this in one message (use Ctrl+Shift+V):

```
I need help with our authentication system. The token expiry logic lives in
src/auth/token.ts. Keep this in mind — I'll ask about it later.

[Now paste at least 3,000 words of unrelated content — for example, copy the first
three sections of the Wikipedia article on "History of computing hardware".
The goal is to push the earlier message further back in the context.]

OK, back to my earlier question. Which file contains the token expiry logic?
```

**What to observe:** With a small amount of filler the model should still answer
correctly (`src/auth/token.ts`). With a very large filler block — especially in
models with smaller context windows — accuracy may drop. The model may give a vague
answer, miss the filename, or say it wasn't mentioned.

This illustrates why long, unfocused conversations are unreliable: the earlier context
that grounded the conversation may no longer be visible to the model.

---

## What to take from this

- Every session starts blank. Supply all necessary context at the start of each session.
- Long conversations with lots of irrelevant content degrade quality. Keep sessions
  focused, or start a fresh session for a new topic.
- If accuracy drops mid-conversation, suspect context fill before assuming model failure.

# Scenario 02 — Context Setting

## Goal
Learn how supplying background context dramatically changes the quality and relevance of a response.

## Setup

Imagine you're a developer who's just joined a team. You need to understand why a particular architectural decision was made. You're going to ask an LLM to help you think through it.

---

## Part A — No context

```
Why would someone use a message queue instead of a direct API call?
```

The model will give you a textbook answer. It's probably accurate, but is it useful for your situation?

---

## Part B — With context

```
I've just joined a backend engineering team. Our system handles order processing for an
e-commerce platform. The previous team used RabbitMQ to queue order confirmation emails
instead of calling the email service directly from the order API. I need to explain this
decision to a new team member who comes from a frontend background and has never worked
with queues.

Can you give me a plain-English explanation of why this pattern was likely chosen, and
what the main trade-off is?
```

---

## What to notice

- Did Part B produce an explanation you could actually paste into a Slack message or doc?
- How much of Part B's output was shaped by the audience ("frontend background") and the
  specific technology (RabbitMQ)?

---

## Challenge

Think of something in your own work you've recently had to explain to someone. Write a
context-setting prompt that gives the model: your role, the audience, the specific thing
to explain, and the tone/format you want. Run it and see if the output is usable.

---

## Key insight

The model is not your colleague — it has no shared history with you. Every prompt is a
fresh start. Context you don't supply, it will guess. Context you do supply, it will use.

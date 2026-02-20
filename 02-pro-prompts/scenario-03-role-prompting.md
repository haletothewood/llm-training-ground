# Scenario 03 — Role Prompting

## Goal
Use persona assignment to shape the model's expertise, tone, and perspective.

## Background
When you assign the model a role ("You are a senior security engineer reviewing this code"),
you do two things: you activate relevant knowledge patterns, and you set expectations for
the level and style of response. It's not magic — the model doesn't *become* that person —
but it meaningfully shifts the output.

---

## Part A — No role

Copy the prompt (use Ctrl+Shift+V to paste so the model doesn't use the file as context).
```
Review this Python function and tell me if there are any problems with it:

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
```

---

## Part B — With a security engineer role

```
You are a senior application security engineer conducting a code review. Your job is to
identify security vulnerabilities, explain the risk, and provide a corrected version.
Be direct and technical — the audience is a mid-level developer.

Review this Python function:

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
```

---

## Part C — With a different role (junior dev mentor)

```
You are a patient senior developer mentoring a junior who is just learning about
databases and security. Use simple language and an encouraging tone.

Look at this code and explain gently what the problem is and how to fix it:

def get_user(user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)
```

---

## What to notice

- Did Part B go deeper on the vulnerability than Part A?
- How different was the tone and vocabulary between Part B and Part C?
- Did any role produce a *wrong* answer? (Roles can sometimes over-commit to a persona
  and miss edge cases — worth watching for.)

---

## Challenge

Think of a piece of feedback you need on your own work — code, writing, a plan. Write the
same prompt twice with two different roles (e.g. "a harsh critic" vs "a supportive
collaborator"). Compare what each surfaces.

---

## Useful roles to experiment with

- `You are a rubber duck. Your job is to listen and ask one clarifying question at a time.`
- `You are a skeptical technical interviewer.`
- `You are a product manager who knows nothing about code but cares deeply about user outcomes.`
- `You are a senior engineer who has seen this exact bug before.`

# Module 07 — Making It Stick

## By the end of this module you'll be able to

- Write project-level AI rules that persist across sessions
- Automate one repetitive task with an LLM API call
- Build a personal feedback loop for evaluating your AI usage over time

---

## Why this module exists

Skills decay without practice infrastructure. The previous modules taught techniques; this
one turns them into defaults. A `CLAUDE.md` file, a git hook, and a weekly review habit
are worth more than memorising prompt patterns.

Module 06 ended with knowing *when* to use AI and *how much* to trust it. The missing
step: turning that knowledge into durable habits and infrastructure in a real workflow.
This module bridges "I learned these skills" to "I use these skills daily without
thinking about it."

## Key concepts

### Project rules
Persistent instructions that travel with the repo, not the person. Different tools
implement this differently (CLAUDE.md, .cursor/rules, copilot-instructions.md) but the
principle is the same: codify your standards so you don't re-explain them every session.

A good rules file prevents the same class of mistake across every session. A bad one
micromanages the model into ignoring what it's good at. The line between the two is
something you'll find by experimenting.

### Automation threshold
The point at which a task you do repeatedly is worth wrapping in a script that calls an
LLM API directly. Not everything should be automated, but the things that should be are
often obvious in hindsight: structured input, text output, low stakes if it's slightly
wrong, high annoyance if you do it by hand.

### Feedback loops
You can't improve what you don't measure. Tracking what you actually use AI for (vs what
you think you use it for) surfaces patterns Module 06's audit exercise only glimpsed.
A week of structured observation reveals more than a single retrospective.

## Scenarios in this module

- [Scenario 01 — Project Rules](./scenario-01-project-rules.md)
- [Scenario 02 — Automate One Thing](./scenario-02-automate-one-thing.md)
- [Scenario 03 — The Weekly Review](./scenario-03-the-weekly-review.md)

## Before you move on

You're done when you have at least one project rule file committed to a repo, one
automated script you've actually used, and one week of usage observations you can look
back on.

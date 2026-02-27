# Scenario 03 — Format Control

**Requires:** any chat interface

## Goal
Use explicit format instructions to get output that's ready to use without reformatting.

---

## Part A — No format instruction

```
What are the main differences between REST and GraphQL?
```

You'll get something — probably paragraphs, possibly a list. It depends on the model's
defaults. That's the problem: you're at the mercy of the default.

---

## Part B — Explicit format

```
Compare REST and GraphQL across the following dimensions: query flexibility, over-fetching,
versioning, tooling, and learning curve.

Format your response as a markdown table with these columns: Dimension | REST | GraphQL.
One row per dimension. Be concise — aim for one sentence per cell.
```

---

## Part C — JSON output

Sometimes you need structured data, not prose:

```
List 5 common HTTP status codes that a REST API developer should know.

Respond in JSON only. Use this exact schema:
[
  { "code": 200, "name": "OK", "when_to_use": "..." },
  ...
]
Do not include any explanation outside the JSON block.
```

---

## What to notice

- Did the table in Part B slot straight into a doc or presentation?
- Did the JSON in Part C parse without errors? (Try pasting it into a JSON validator.)
- What happens if you add "Do not include any explanation outside the JSON block" vs leaving
  that out?

---

## Challenge

Think of a report, table, or structured data you regularly produce manually. Write a prompt
that would generate it in the exact format you need. Add explicit format instructions and
run it.

# Scenario 03 — The Weekly Review

## Goal
Track your AI usage for one week and discover your actual patterns.

## Background

Module 06 Scenario 03 asked you to audit your last five AI uses from memory. This
scenario replaces memory with data. A week of structured tracking reveals patterns that
a one-time retrospective misses: which tasks you actually use AI for (vs which ones you
think you do), which form factors you reach for, and where the hit rate is highest.

The act of tracking also changes behaviour. You'll notice yourself making more deliberate
choices about when and how to use AI — which is the point.

---

## Part A — Set up the tracker

Create a file you'll actually open daily. A markdown file in your project, a note in
your notes app, a text file on your desktop — whatever has the lowest friction.

Use this template:

```markdown
# AI Usage Tracker — Week of [date]

| Date | Task | Form factor | Outcome | Again? |
|------|------|-------------|---------|--------|
| | | | | |
```

**Column definitions:**

- **Date** — when you used (or considered using) AI
- **Task** — what you were trying to do (one sentence)
- **Form factor** — how you used it: `chat`, `CLI`, `API`, `inline` (autocomplete),
  or `none` (decided not to use AI)
- **Outcome** — `useful`, `partially useful`, `waste of time`, or `didn't use`
- **Again?** — would you use AI for this task again? `yes`, `no`, `maybe`

---

## Part B — Track for one week

Every time you use (or consider using) AI for a work task, add a row. The important
details:

- **Include the times you decided NOT to use AI.** Those decisions are just as
  informative as the times you did. Log them with form factor `none` and outcome
  `didn't use`.
- **Be honest about outcomes.** "Partially useful" is the most common real answer.
  If you used AI to generate code but then rewrote half of it, that's partially useful,
  not useful.
- **Aim for at least 10 entries.** If you're getting fewer than that, you're probably
  not logging the small uses — autocomplete acceptances, quick questions, format
  conversions.
- **Log immediately.** If you wait until end of day, you'll forget the details that
  matter most.

---

## Part C — Review

At the end of the week, read through your tracker and answer these questions:

1. **What's your most common use case?** (The task that appears most often)
2. **What's your hit rate?** (Count of `useful` / total entries, as a percentage)
3. **Were there tasks where AI was a net negative?** (Took longer than doing it yourself,
   or produced output that needed so much fixing it wasn't worth it)
4. **Were there tasks where you didn't use AI but should have?** (Tasks marked `none`
   where, in retrospect, AI would have helped)
5. **What form factor appeared most?** (`chat`, `CLI`, `API`, `inline`)

Then write a personal "rules of engagement" — 3 to 5 sentences describing when and how
you'll use AI going forward. Not aspirational goals; practical rules based on what you
actually observed.

Example:

> I use AI most for explaining unfamiliar code and generating test scaffolding. My hit
> rate is about 70%. Chat works best for exploration; CLI works best for things I've
> already done once and want to repeat. I waste the most time when I use AI for tasks
> I could do faster myself — especially small edits where the prompting overhead exceeds
> the time saved. My rule: if I can do it in under 2 minutes, just do it.

---

## What to notice

- Did your actual usage pattern match what you would have predicted before tracking?
- Which form factor (chat, CLI, API, inline) appeared most? Is that what you expected?
- Did the act of tracking change your behaviour during the week? Did you use AI more
  carefully, or avoid it in cases where you might have otherwise reached for it?
- Were there days with no entries? What does that tell you about your workflow?

---

## Reflection questions

1. How would you update your project rules file (Scenario 01) based on what you learned
   this week?
2. Is there another task worth automating (Scenario 02) that you spotted in your tracker?
3. What's the one habit from this curriculum you're most likely to keep?
4. If you did this exercise again in a month, what do you think would change?

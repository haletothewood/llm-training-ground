# Module 07 — Hints

## Scenario 01 — Project Rules

Start with what annoys you. The best rules prevent mistakes you've already made. If you
can't think of 5 repeated instructions, that's a signal you might not need a rules file
yet — and that's fine.

The most effective rules are usually negative: "don't do X" works better than "always
do Y" because it's easier for the model to avoid something specific than to always
remember a positive instruction.

If you're not sure whether a rule is working, remove it and see if the behaviour changes.
A rule you can't tell the difference without isn't worth keeping.

---

## Scenario 02 — Automate One Thing

If you don't have an API key, you can use Claude Code itself as the automation layer —
write a shell script that pipes input to `claude -p "your prompt"`. The principle is the
same: structured input goes in, formatted text comes out.

The most common first-run failure is a prompt that's too vague. In a chat session, you'd
refine it over 2–3 exchanges. In a script, you need to get it right the first time. If
the output isn't useful, look at the prompt before looking at the code.

If the script works but the output needs editing every time, try adding an explicit
example of the output format you want to the prompt (few-shot, from Module 02).

---

## Scenario 03 — The Weekly Review

The tracker doesn't need to be fancy. A text file you append to is better than a
spreadsheet you never open. The minimum viable entry is: what, how, was it worth it.

If you forget to log for a day, don't backfill from memory — that defeats the purpose.
Just pick up the next day.

The "didn't use" entries are often the most revealing. They show where your instinct is
to reach for AI but you chose not to — or where you didn't even consider it and maybe
should have.

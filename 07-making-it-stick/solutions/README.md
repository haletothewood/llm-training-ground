# Module 07 — Solutions

Module 07 is primarily practical — the scenarios produce artifacts (a rules file, a
script, a usage log) rather than model-generated outputs. There's no single correct
answer to compare against.

What you should have after completing this module:

---

## Scenario 01 — Project Rules

A `CLAUDE.md` (or equivalent) committed to a project repo. A good one:

- Is under 40 lines
- Includes at least one "do not" rule that prevents a real mistake you've seen
- Was tested in a fresh session where the model followed the rules without being reminded
- Doesn't micromanage — leaves room for the model to use judgment on things that
  don't need rigid constraints

If the model ignored a rule during your Part C test, check whether the rule was too
vague ("write clean code") or too buried in a long file. Specificity and brevity are
the two strongest predictors of whether a rule gets followed.

---

## Scenario 02 — Automate One Thing

A working script that you've run at least 3 times on real data. Calibration points:

- The prompt inside the script should be more precise than what you'd type in a chat
  session — because there's no back-and-forth to refine it
- If the output needs editing every time, the prompt needs work (try adding a concrete
  output example — few-shot, from Module 02)
- If it works well, the script is probably under 30 lines — the boilerplate is minimal
  and the prompt is doing the real work

### Common first-run failures

| Symptom | Likely cause |
|---------|-------------|
| Output is too generic | Prompt doesn't specify format precisely enough |
| Output includes preamble ("Sure! Here's...") | Add "respond with only the formatted output, no preamble" |
| Script errors on empty input | Missing the stdin check — add the `if not diff.strip()` guard |
| API key error | `ANTHROPIC_API_KEY` not set in environment |

---

## Scenario 03 — The Weekly Review

A completed tracker with at least 10 entries and a personal "rules of engagement"
paragraph. Things to check:

- Did you include `none` entries (times you considered AI but didn't use it)?
- Is your hit rate realistic? If it's 100%, you're probably not logging the failures.
- Does your "rules of engagement" paragraph describe what you actually do, not what
  you aspire to do?

The tracker is most valuable if you revisit it in a month. Your patterns will have
shifted — and knowing *how* they shifted is the feedback loop this module is about.

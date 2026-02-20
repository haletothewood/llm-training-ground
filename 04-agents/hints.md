# Module 04 — Hints

## Agent prompt checklist

Before running an agent task, verify your prompt has:

- [ ] **A clear goal** — not a list of steps, but what "done" looks like
- [ ] **A scope constraint** — which files/dirs are in bounds, which are not
- [ ] **A checkpoint instruction** — "show me your plan before making changes"
- [ ] **An uncertainty instruction** — "if you're unsure, ask rather than guess"

## Controlling agent behaviour

**Too autonomous?**
```
Before taking any action that modifies a file, tell me what you're about to do and wait
for me to say "go ahead".
```

**Too cautious / asking too many questions?**
```
Make reasonable assumptions and proceed. Only ask if you hit a genuine blocker — not to
confirm details you can infer from context.
```

**Scope creep?**
```
Do not change anything outside [specific scope]. If you notice something else that
should be fixed, note it in your response but do not touch it.
```

## Recovery patterns

**Agent went off track:**
"Stop. Undo any changes you made in this session using git checkout. Let's start over
with a clearer scope."

**Agent is stuck in a loop:**
Interrupt it, ask it to summarise what it has tried, then redirect: "Given that X didn't
work, try Y instead."

**Agent made changes you don't understand:**
"Explain every change you made and why, file by file."

## Detecting silent failures

Silent failure is when the agent completes the task, reports success, and the output
is wrong in a way that isn't immediately obvious.

**What silent failure looks like:**
- Code that compiles and passes lint but implements the wrong logic
- Scope creep: changes in files you didn't mention
- Missing edge cases: the function works on the happy path but not the edge case that
  motivated the task
- Implementing exactly what you said rather than what you meant

**Detection habits:**
- Diff every changed file after an agent run — don't just trust the summary
- Test the specific case that motivated the task, not just the general case
- If you don't fully understand a change the agent made, ask it to explain its reasoning
  file by file before merging
- For any change touching business logic: ask yourself "does this handle the failure case?"
  and check that the agent addressed it

## The golden rule

An agent is as good as the goal you give it. Vague goal → unpredictable path.
Specific goal with scope constraints → reliable, reviewable output.

# Module 03 — Hints

## Prompting for tool use

**Be task-oriented, not question-oriented.**
"What are the tests?" → "Run the tests and tell me which ones failed."

**Name the artefact, not the action.**
"Look at the package.json" → "Read package.json and list the scripts section."
(More precise = fewer wrong tool choices.)

**Say what to do with the result.**
"Read requirements.txt" is incomplete. "Read requirements.txt and tell me which packages
are unpinned" gives the model a goal to work toward.

## Common failure modes

**The model reads the wrong file.** Be explicit: name the file or describe it precisely.

**The model fabricates instead of using a tool.** If you suspect this, ask: "Did you
actually read the file, or are you inferring?" and check the tool call log if available.

**The model uses a tool when it should reason.** Sometimes you don't need a file read —
you just need the model to think. Over-relying on tools can slow things down. Use tools
when you need *current* or *specific* information, not for general knowledge questions.

## When skills are the right choice

Use a skill when:
- You run the same prompt more than 2–3 times a week
- The task is well-defined enough to be templated
- Consistency matters more than flexibility

Don't use a skill when:
- Each instance of the task is meaningfully different
- You're still figuring out what the prompt should be
- The task is simple enough to just type

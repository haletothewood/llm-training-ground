# Scenario 02 — Automate One Thing

## Goal
Write a short script that calls an LLM API to automate a task you currently do manually.

## Background

Every interaction you've had in this curriculum used a chat interface or a CLI tool as
the middleman. In this scenario, you remove the middleman: your code calls the API
directly. The model is the same — only the interface changes.

This matters because a script you can run from the command line, wire into a git hook,
or call from a Makefile becomes part of your infrastructure. A chat conversation is
ephemeral. The goal is to find one task worth making permanent.

---

## Part A — Pick the task

Choose something you actually do repeatedly. Good candidates:

- Writing commit messages from a diff
- Summarising pull requests
- Explaining error logs
- Generating test stubs from function signatures
- Writing changelog entries
- Converting code between formats or styles

The ideal task has **structured input** (a diff, a log, a function signature) and
**text output**. If the input is vague and requires back-and-forth, it's a better fit
for chat than for a script.

The walkthrough below uses "PR summary from git diff" — swap in your own task if you
prefer.

---

## Part B — Build it

### Setup

```bash
pip install anthropic
```

You'll also need an `ANTHROPIC_API_KEY` environment variable set:

```bash
export ANTHROPIC_API_KEY="your-key-here"
```

Get a key from [console.anthropic.com](https://console.anthropic.com) under API Keys.
Add the export to your `.bashrc` / `.zshrc` so it persists across sessions.

### The script

Create `pr_summary.py`:

```python
#!/usr/bin/env python3
"""Generate a PR summary from a git diff."""

import sys
import anthropic

def main():
    diff = sys.stdin.read()
    if not diff.strip():
        print("No diff provided. Usage: git diff | python pr_summary.py")
        sys.exit(1)

    MAX_CHARS = 100_000  # ~25k tokens; avoids hitting API context limits
    if len(diff) > MAX_CHARS:
        print(f"Warning: diff is {len(diff):,} chars — truncating to {MAX_CHARS:,}",
              file=sys.stderr)
        diff = diff[:MAX_CHARS]

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Summarise this git diff as a pull request description.

Format:
## Summary
(2-3 bullet points: what changed and why)

## Files changed
(list each file with a one-line description of the change)

Diff:
{diff}"""
        }]
    )
    print(message.content[0].text)

if __name__ == "__main__":
    main()
```

### What each part does

**`sys.stdin.read()`** — Reads the diff from stdin. This is deliberate: it makes the
script composable with pipes. You can use `git diff | python pr_summary.py` or
`cat some_file.diff | python pr_summary.py`. Composability with Unix pipes is one of
the most useful properties a CLI tool can have.

**`anthropic.Anthropic()`** — Creates a client that reads the API key from the
`ANTHROPIC_API_KEY` environment variable. No hardcoded secrets. If the key isn't set,
this will raise a clear error.

**The prompt** — Specifies the exact output format. In a chat session you can say "no,
format it differently" and iterate. In a script, you get one shot — so the prompt needs
to be precise the first time. Everything Module 01 taught about clear prompting matters
*more* here, not less.

**`message.content[0].text`** — The API returns a structured response object. The actual
text is nested inside `.content[0].text`. This is just the Anthropic SDK's response
format — every provider has its own version of this.

### Run it

```bash
git diff HEAD~1 | python pr_summary.py
```

---

### Using a different provider

The pattern is nearly identical with OpenAI. Two things change: the SDK and the
response structure. The prompt doesn't change at all.

```bash
pip install openai
```

```python
from openai import OpenAI

client = OpenAI()  # reads OPENAI_API_KEY from env

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": f"...same prompt as above..."}]
)
print(response.choices[0].message.content)
```

Different SDK, same pattern. The fact that the prompt is portable across providers is
one of the key advantages of learning prompting well — it's not vendor-specific.

### No API key at all?

Use Claude Code as the engine — zero setup:

```bash
git diff HEAD~1 | claude -p "Summarise this git diff as a pull request description.
Format: ## Summary (2-3 bullets) ## Files changed (one line each)"
```

Shorter, but same principle: structured input, LLM, formatted output. The tradeoff:
less control over model parameters, but nothing to install or configure.

---

## Part C — Wire it in

Make the script part of your actual workflow. Pick one:

**Option 1 — Git alias:**

```bash
git config --global alias.summary '!git diff HEAD~1 | python /path/to/pr_summary.py'
```

Then: `git summary`

**Option 2 — Shell function** (add to `.bashrc` / `.zshrc`):

```bash
pr-summary() { git diff "${1:-HEAD~1}" | python /path/to/pr_summary.py; }
```

Then: `pr-summary` or `pr-summary main..HEAD`

**Option 3 — Makefile target** (for projects that already use Make):

```makefile
.PHONY: pr-summary
pr-summary:
	git diff HEAD~1 | python pr_summary.py
```

Whichever you choose: **run it on real data at least 3 times.** Tweak the prompt if the
output isn't what you want. The first version of any automation prompt needs iteration —
that's expected, not a failure.

---

## What to notice

- How does the output quality compare to what you'd get from a chat session?
- What did you have to change in the prompt to make it work without back-and-forth?
- What broke on the first run?
- Is the output good enough to use directly, or does it need editing every time?

---

## Key insight

An API call is a one-shot prompt with no room for clarification. Everything Module 01
taught about precise prompting matters *more* here, not less. The difference between a
script that's useful and one that sits unused is almost always the quality of the prompt
inside it.

---

## Challenge

Swap out the task. Replace the PR summary prompt with something from Part A — commit
messages, error log explanations, test stubs, changelog entries. The script skeleton
stays the same: read from stdin, call the API, print the result. Only the prompt and
the input source change.

That's the point. Once you have the pattern, the cost of automating the next task is
just writing a new prompt.

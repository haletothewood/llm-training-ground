# Scenario 03 — Using a Skill (Claude Code)

**Requires:** Claude Code, Cursor, or similar AI coding tool

> **Claude Code-specific.** This scenario uses Claude Code's `/command` skill system.
> See the [Module 03 README](./README.md#what-are-skills) for the equivalent in Cursor
> (Rules) and GitHub Copilot (Custom Instructions).

## Goal
Use a named skill (slash command) to invoke a well-defined, repeatable task.

## What is a skill?

In Claude Code, skills are `/commands` — pre-defined prompt templates that invoke a
structured workflow. They're useful when a task is:
- Repeated often enough to be worth standardising
- Complex enough that you don't want to re-specify it every time
- Well-defined enough that a template captures it accurately

---

## Built-in skills to try

### /commit

Stage your changes and run:

```
/commit
```

Claude will:
1. Review what's staged (`git diff --staged`)
2. Check recent commit history for your team's style
3. Write a commit message following that style
4. Commit it

**Experiment:** Make a small change to a file, stage it, and run `/commit`. Did the
message accurately reflect what you changed? Was the tone/format consistent with existing
commits in the repo?

---

### Invoking skills with context

Skills can be combined with additional instructions:

```
/commit

Note: this commit is part of a hotfix branch and should reference ticket PROJ-4821
in the message.
```

Does the skill incorporate your additional context?

---

## Creating a custom skill

Skills live in `~/.claude/commands/` (or a project-level `.claude/commands/` directory).
Note: older versions of Claude Code used `~/.claude/skills/` — update to `commands/` if
you're on a recent release.
A skill is just a markdown file with a prompt template.

Create a file at `~/.claude/commands/summarise-pr.md`:

```markdown
# Summarise PR

Read the git diff between the current branch and main. Write a pull request description
with the following sections:

## What changed
One paragraph, plain English.

## Why
One paragraph explaining the motivation (infer from commit messages and code context).

## How to test
Bullet list of suggested manual test steps.

Keep the total length under 300 words.
```

Then invoke it with:
```
/summarise-pr
```

---

## What to notice

- How does invoking a skill compare to typing out the full prompt each time?
- Where do skills break down? (Hint: when the task varies too much for a fixed template.)
- What tasks in your workflow would benefit from a standardised skill?

---

## Challenge

Identify one task you do repeatedly in a chat session. Write it as a skill file and test it
on a real case. Refine the template based on what the first run gets wrong.

---

## If you're using Cursor or Copilot

**Cursor — Rules:** Create `.cursor/rules/summarise-pr.mdc` in your project with the same
prompt template content. Rules can be set to trigger automatically (always-on) or manually.
See the [Cursor Rules docs](https://docs.cursor.com/context/rules) for the full format.

**GitHub Copilot — Custom Instructions:** Add the prompt template to
`.github/copilot-instructions.md`. Unlike Claude Code skills, this applies to every
Copilot chat session in the workspace automatically — there's no explicit invocation step.
The trade-off: always-on context vs. on-demand invocation.

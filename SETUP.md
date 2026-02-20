# Setup Guide

Before starting the exercises, spend five minutes confirming you have what you need.

---

## 1. Pick your AI coding tool

The scenarios work with any of these. Pick whichever you already have or are most
likely to use day-to-day.

| Tool | What it is | Best for |
|------|------------|----------|
| **Claude Code** | CLI tool by Anthropic; runs in your terminal | Modules 03–06, MCP |
| **Cursor** | VS Code fork with built-in AI | Modules 01–05 |
| **GitHub Copilot** | AI inside VS Code / JetBrains | Modules 01–03 |
| **Claude.ai / ChatGPT** | Browser chat | Modules 00–02 only |

**Recommendation:** use Claude Code if you're starting from scratch. The exercises are
written primarily for it, and it has the widest tool support. Cursor is a good alternative.

### Claude Code install

```bash
npm install -g @anthropic-ai/claude-code
claude
```

You'll need an [Anthropic account](https://console.anthropic.com) — a free tier is
available. On first launch, `claude` will prompt you to log in.

### Cursor install

Download from [cursor.com](https://cursor.com). Requires a Cursor account (free tier
available).

---

## 2. Module 05 — additional requirements

Module 05 (MCP Servers) builds a TypeScript server. You'll need:

- **Node.js 18 or later** — check with `node --version`
- **npm** — ships with Node; check with `npm --version`

If you don't have Node, install it from [nodejs.org](https://nodejs.org) or via your
package manager (`brew install node` on macOS).

---

## 3. Sample project (Modules 03–05)

Modules 03–05 ask you to work with real code. This repo includes a small Python Flask
app in `sample-project/` for exactly this purpose.

To run it locally:

```bash
cd sample-project
pip install -r requirements.txt
python app.py
```

The server starts at `http://localhost:5000`. You don't need to run it to use it as
a target for the agent exercises — the agent can read and modify the files directly.

---

## 4. About "paste with Ctrl+Shift+V"

You'll see this instruction in several Module 01 and 02 scenarios:

> *"Paste this prompt using Ctrl+Shift+V"*

This matters specifically in **Claude Code**, which is file-context-aware. If you copy
and paste a prompt normally (Ctrl+V), Claude Code may detect that the clipboard content
came from a file in the repo and silently attach that file as context — which would
contaminate the exercise, since you're supposed to be testing what the model does with
*only* the prompt text.

**Ctrl+Shift+V** pastes the text as plain input without triggering file attachment.

If you're using a browser chat interface (Claude.ai, ChatGPT) or Cursor, this doesn't
apply — paste normally.

---

## 5. You're ready

Start with [Module 00 — How LLMs Work](./00-how-llms-work/README.md).

If you already understand token prediction, context windows, and hallucination,
skip to [Module 01 — Clear Prompting](./01-clear-prompting/README.md).

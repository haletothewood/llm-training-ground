# Scenario 01 — Using a Pre-Built MCP Server

## Goal
Connect a pre-built MCP server to Claude Code (or your client of choice) and use it to
extend what the model can do.

## Popular pre-built MCP servers to start with

| Server | What it does | Install |
|--------|-------------|---------|
| `@modelcontextprotocol/server-filesystem` | Read/write local files with path controls | `npx` |
| `@modelcontextprotocol/server-github` | Search repos, read files, manage issues | `npx` |
| `@modelcontextprotocol/server-postgres` | Query a PostgreSQL database | `npx` |
| `@modelcontextprotocol/server-brave-search` | Web search via Brave API | `npx` |

Full list: https://github.com/modelcontextprotocol/servers

---

## Setting up the filesystem server (Claude Code)

This is the lowest-friction starting point — no API keys needed.

### 1. Add the server to Claude Code config

Edit (or create) `~/.claude/claude.json` and add:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/Documents"
      ]
    }
  }
}
```

Replace the path with a real directory you want the model to access.

### 2. Restart Claude Code

### 3. Test it

```
List all markdown files in my Documents folder and tell me which one was most recently
modified.
```

Did the model use the MCP filesystem tool rather than the built-in file tools?

---

## Setting up the GitHub server

Requires a GitHub personal access token.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

Test prompt:
```
Search my GitHub repositories for any that have "api" in the name and tell me when each
was last updated.
```

---

## What to notice

- How does the model indicate it's using an MCP tool vs its built-in tools?
- What can the MCP server do that the built-in tools can't?
- What happens if you ask the model to do something outside the server's capabilities?

---

## Hints

See [hints.md](./hints.md) for troubleshooting connection issues.

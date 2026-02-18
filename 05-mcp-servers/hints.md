# Module 05 — Hints

## Troubleshooting MCP connections

**Server won't start:**
- Check `npx` is available: `npx --version`
- Run the server command manually in your terminal — it should start without error
- Check Claude Code logs: `~/.claude/logs/` (or wherever your client stores logs)

**Tools not appearing in Claude Code:**
- Restart Claude Code completely after changing `claude.json`
- Validate the JSON syntax of your config (`cat ~/.claude/claude.json | python3 -m json.tool`)
- Confirm the `args` array paths are absolute, not relative

**Model isn't using the tool:**
- Is the task description in your prompt matched by the tool's description?
- Try explicitly mentioning the tool: "Use the notes tool to..."
- Check the tool description — is it clear enough for the model to know when to use it?

**Tool call returns an error:**
- Run the server manually and send a test JSON-RPC request to see the raw error
- Check file permissions if the server reads/writes files
- Add console.error logging to your server for debugging

---

## Writing good tool descriptions

The model decides whether to use a tool based on its name and description. Good descriptions:

**Be specific about when to use the tool:**
```
// Bad: "Search files"
// Good: "Search the local filesystem for files matching a name or content pattern.
//        Use when the user asks to find a file, locate code, or search their computer."
```

**Describe the output:**
```
// Bad: "Get user information"
// Good: "Fetch a user's profile by ID. Returns name, email, role, and account status."
```

**List required vs optional parameters in the description:**
```
// Useful: "Requires: query. Optional: max_results (default 10), file_type."
```

---

## Architecture patterns

**Local-only server:** stdio transport, no auth needed. Good for personal tools.

**Shared team server:** HTTP+SSE transport, add authentication. Good for shared knowledge
bases or internal APIs.

**Stateless vs stateful:** Most servers should be stateless. If you need state
(e.g. a shopping cart), keep it in an external store (file, DB) not in the server process.

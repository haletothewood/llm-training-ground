# Scenario 02 — Understanding the Protocol

**Requires:** Claude Code, Cursor, or similar AI coding tool

## Goal
Understand how MCP works under the hood, so you can debug problems and design your
own servers effectively.

## What's actually happening

When an MCP client (Claude Code, Cursor, etc.) starts an MCP server, it:

1. Spawns the server process (or connects to an HTTP endpoint)
2. Sends an `initialize` request
3. Receives back a list of available `tools`, `resources`, and `prompts`
4. Registers these so the model can use them

When you run a prompt, the model sees the tool definitions and decides whether to call
one. If it does, the client:
1. Sends a `tools/call` request to the MCP server
2. Waits for the result
3. Feeds the result back to the model as context
4. Continues generating

This is all JSON-RPC over stdio (for local servers) or HTTP+SSE (for remote ones).

---

## Exercise — Inspect the protocol

### Option A: Use MCP Inspector

```bash
npx @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem /tmp
```

This opens a browser-based UI showing the live JSON-RPC messages between client and server.

Try calling a tool manually from the inspector. What does the request/response look like?

---

### Option B: Read a server's source

Pick a simple server and read its implementation:

- `@modelcontextprotocol/server-everything` is a reference server that demonstrates
  all protocol features in minimal code.

Clone it:
```bash
git clone https://github.com/modelcontextprotocol/servers
cd servers/src/everything
```

Ask your agent to explain it:
```
Read the source of this MCP reference server and explain:
1. How it registers its tools
2. What each tool does
3. How it handles a tool call and returns a result
```

---

## Key concepts to understand

**Tool definition:**
```json
{
  "name": "search_files",
  "description": "Search for files matching a pattern",
  "inputSchema": {
    "type": "object",
    "properties": {
      "pattern": { "type": "string" }
    },
    "required": ["pattern"]
  }
}
```

The description is what the model reads to decide whether to use the tool. **Write it
for the model, not for humans.** A clear, precise description = the model uses the tool
correctly. A vague description = the model misuses it or ignores it.

---

## What to notice

- The model only sees tool *descriptions*, not tool *implementations*
- The quality of tool descriptions directly affects how reliably the model uses them
- MCP is stateless per request — the server doesn't "remember" previous tool calls

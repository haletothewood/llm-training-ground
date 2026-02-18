# Scenario 03 — Building a Minimal MCP Server

## Goal
Build the simplest possible MCP server that exposes one useful tool, connect it to
Claude Code, and verify it works end-to-end.

## Prerequisites
- Node.js 18+ or Python 3.10+
- Basic familiarity with either language

---

## The server: a note-taking tool

We'll build a server that exposes two tools:
- `add_note(content)` — appends a note to a local file
- `list_notes()` — returns all notes

Small scope, real utility — and a good template for anything that reads/writes local data.

---

## Implementation (TypeScript)

```bash
mkdir my-notes-mcp && cd my-notes-mcp
npm init -y
npm install @modelcontextprotocol/sdk
```

Create `server.ts`:

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import * as fs from "fs";
import * as path from "path";

const NOTES_FILE = path.join(process.env.HOME || ".", "mcp-notes.txt");

const server = new Server(
  { name: "notes", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    {
      name: "add_note",
      description: "Append a short note to the user's personal notes file. Use this when the user asks to save, remember, or note something.",
      inputSchema: {
        type: "object",
        properties: {
          content: { type: "string", description: "The note text to save" }
        },
        required: ["content"]
      }
    },
    {
      name: "list_notes",
      description: "Return all notes the user has previously saved.",
      inputSchema: { type: "object", properties: {} }
    }
  ]
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "add_note") {
    const content = request.params.arguments?.content as string;
    const timestamp = new Date().toISOString().split("T")[0];
    fs.appendFileSync(NOTES_FILE, `[${timestamp}] ${content}\n`);
    return { content: [{ type: "text", text: "Note saved." }] };
  }

  if (request.params.name === "list_notes") {
    const notes = fs.existsSync(NOTES_FILE)
      ? fs.readFileSync(NOTES_FILE, "utf-8")
      : "No notes yet.";
    return { content: [{ type: "text", text: notes }] };
  }

  throw new Error(`Unknown tool: ${request.params.name}`);
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

Compile and test:
```bash
npx tsc server.ts --module nodenext --target es2022
node server.js
# Should hang — it's waiting for JSON-RPC input on stdin, which is correct
```

---

## Connect it to Claude Code

Add to `~/.claude/claude.json`:

```json
{
  "mcpServers": {
    "notes": {
      "command": "node",
      "args": ["/absolute/path/to/my-notes-mcp/server.js"]
    }
  }
}
```

---

## Test it

In Claude Code:
```
Remember to review the deployment checklist before Friday.
```

Then:
```
What notes do I have saved?
```

Did it use your tools? Did it add the note and retrieve it correctly?

---

## What to notice

- How did the tool description affect whether the model used it?
- What happens if you change the description to be vaguer?
- What would you add to make this server actually useful to you?

---

## Next steps

- Add a `delete_note(index)` tool
- Add date filtering to `list_notes`
- Replace the flat file with a SQLite database
- Build a server for something you actually need: a Jira integration, a local knowledge
  base, a codebase index, your calendar

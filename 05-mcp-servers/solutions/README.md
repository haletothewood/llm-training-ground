# Module 05 — Solutions

---

## Scenario 01 — Using a Pre-Built MCP Server

### What successful filesystem MCP tool use looks like

After configuring `@modelcontextprotocol/server-filesystem` and asking:

> "List all markdown files in my Documents folder and tell me which was most recently modified."

A model using the MCP tool:

> *[uses filesystem:list_directory tool]*
> *[uses filesystem:get_file_info on each .md file]*
>
> "I found 8 markdown files in your Documents folder. The most recently modified is
> `project-notes.md`, last updated 3 hours ago. Here are all of them sorted by
> modification date:
> 1. `project-notes.md` — 3 hours ago
> 2. `meeting-2024-01.md` — 2 days ago
> ..."

**What distinguishes MCP tool use from built-in tools:** In Claude Code, you'll see
tool calls in the output prefixed with the MCP server name (e.g. `filesystem:list_directory`
rather than the native `list_files` tool). If you don't see the MCP server prefix,
the model may have used its built-in tools instead.

### What happens outside the server's scope

> "Move my Documents/project-notes.md to the Desktop."

If the server is configured with read-only permissions, or the Desktop path is outside
the allowed directory, the model should respond:

> "I don't have access to your Desktop — the filesystem server is configured to access
> only your Documents folder. You could move the file manually, or I can copy the
> content to a new file if that helps."

A model that attempts the operation anyway (and fails silently) is not respecting its
tool constraints — a warning sign for agentic tasks.

---

## Scenario 02 — Understanding the Protocol

### What a tool definition looks like in JSON-RPC

When you send `{"jsonrpc": "2.0", "method": "tools/list", "id": 1}` to a server, a
well-formed response looks like:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "read_file",
        "description": "Read the contents of a file at the given path.",
        "inputSchema": {
          "type": "object",
          "properties": {
            "path": {
              "type": "string",
              "description": "Absolute path to the file to read"
            }
          },
          "required": ["path"]
        }
      }
    ]
  }
}
```

**The key insight:** The model sees this JSON schema — it does not see your source code.
The `description` field is literally the entire signal the model uses to decide whether
to call this tool. A vague description like "read a file" will be called less reliably
than "Read the contents of a file at the given absolute path. Use this when the user
asks about the content of a specific file."

---

## Scenario 03 — Building a Minimal MCP Server

### Expected output when the server starts correctly

```bash
node dist/server.js
```

No output — the server is waiting on stdin. This is correct. The server communicates
over stdio (stdin/stdout), not over HTTP. Press Ctrl+C to stop it.

### What successful tool use looks like in Claude Code

After connecting the notes server and asking:

> "Remember to review the deployment checklist before Friday."

Claude Code:

> *[calls add_note with content: "Review deployment checklist before Friday"]*
>
> "Done — I've saved a note for you."

Then:

> "What notes do I have?"

> *[calls list_notes]*
>
> "You have one note:
> [2024-01-15] Review deployment checklist before Friday"

### Effect of tool description on model behaviour

**Vague description:** `"description": "Save a note"`

Result: the model may call it erratically, or may not call it at all when you say
"remember this" — because "remember" doesn't obviously match "save".

**Specific description:** `"description": "Append a short note to the user's personal notes file. Use this when the user asks to save, remember, or note something."`

Result: "remember", "note down", "save this for later" all reliably trigger the tool.

The description is a prompt — it tells the model when and how to use the tool.
Write it the same way you'd write a prompt instruction.

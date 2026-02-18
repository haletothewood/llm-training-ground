# Module 05 — MCP Servers

## What is MCP?

MCP (Model Context Protocol) is an open standard that lets you connect an LLM to
external systems — databases, APIs, filesystems, services — in a structured, reusable way.

Think of it as a plugin system for LLMs. Instead of pasting data into a prompt or writing
custom tool glue code for every integration, you build (or use) an MCP server that exposes
capabilities the model can call.

## Why it matters

Without MCP: to give Claude access to your database, you'd write a one-off script that
queries the DB and pastes results into a prompt. It's fragile, not reusable, and the
model can't choose *which* query to run — you have to decide that upfront.

With MCP: you define a server with tools like `query_database(sql)` or `get_user(id)`.
The model calls these tools based on what the task requires. It's a proper integration,
not a hack.

## How it works (architecture)

```
Your LLM client (Claude Code, etc.)
    ↕  MCP protocol (JSON-RPC over stdio or HTTP)
MCP Server
    ↕
External system (database, API, filesystem, etc.)
```

The server exposes three types of capabilities:
- **Tools** — functions the model can call (like `search_docs`, `create_ticket`)
- **Resources** — data the model can read (like file contents, database rows)
- **Prompts** — reusable prompt templates the server provides

## Scenarios in this module

- [Scenario 01 — Using a Pre-Built MCP Server](./scenario-01-using-a-server.md)
- [Scenario 02 — Understanding the Protocol](./scenario-02-understanding-the-protocol.md)
- [Scenario 03 — Building a Minimal MCP Server](./scenario-03-building-a-server.md)

## Before you move on

After this module you should understand: what MCP solves, how to connect a pre-built
server to your LLM client, and have a mental model of how to build your own.

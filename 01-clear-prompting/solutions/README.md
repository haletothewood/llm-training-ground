# Module 01 — Solutions

These are example model responses and annotations. Your outputs will differ (non-determinism
is real), but they should have the same shape.

---

## Scenario 01 — Vague vs Precise

### Part A: Response to "Fix the bug."

A representative response:

> "I'd be happy to help fix the bug! Could you please provide more details about:
> - What language or framework you're using
> - What the bug is doing (error message, unexpected behaviour, etc.)
> - The relevant code snippet
> - What you expected to happen"

Or, from a model that doesn't ask for clarification:

> "Sure! Here's how to fix a common bug in Python — if you're getting an `AttributeError`,
> it usually means you're calling a method on a `None` value. Make sure to add a null
> check: `if obj is not None: obj.method()`."

**What to notice:** The first response asks four clarifying questions and can't proceed.
The second invents a completely fictional bug (AttributeError on None) and provides a
confident, useless fix. Neither is your bug.

### Part B: Response to the precise prompt

A representative response:

```typescript
function validateToken(token: string): boolean {
  try {
    jwt.verify(token, process.env.JWT_SECRET!);
    return true;
  } catch (error) {
    if (error instanceof TokenExpiredError) {
      return false;
    }
    throw error; // Re-throw unexpected errors
  }
}
```

> "I've updated `validateToken` to catch `TokenExpiredError` specifically and return
> `false` rather than letting the exception propagate. Other JWT errors (malformed token,
> invalid signature) are re-thrown since those are unexpected conditions that should
> surface to the caller. The function signature is unchanged."

**What to notice:**
- The response is immediately usable with no follow-up questions
- The model correctly inferred that non-expiry errors should still throw (good engineering judgement, enabled by the constraint "fix only this function")
- Word count of the precise prompt: ~75 words. Words saved in back-and-forth: easily 200+

---

## Scenario 02 — Context Setting

### Without context: a textbook response

Prompt: "Explain how to handle database connection errors."

> "Database connection errors can be handled using try-catch blocks and retry logic.
> Common patterns include: exponential backoff for transient failures, circuit breakers
> for sustained outages, and connection pooling to manage resource exhaustion.
> Always log errors with sufficient context for debugging..."

Generic, safe, not actionable for your specific situation.

### With context: a specific, actionable response

Prompt specifying: Express.js + PostgreSQL + pg library + production environment + errors surfacing as 500s to users

> "In your Express/pg setup, the most important fix is catching the connection error
> before it propagates to your error handler as a 500. In your pg `Pool` setup:
> ```javascript
> pool.on('error', (err) => {
>   logger.error('Unexpected database error', err);
>   // Don't exit — pool will reconnect automatically
> });
> ```
> For query-level errors in your route handlers, distinguish between connection errors
> (`ECONNREFUSED`, `ETIMEDOUT`) and query errors (`23505` for unique constraint, etc.).
> Connection errors warrant a retry; query errors should surface to the caller with a
> 503 (unavailable) rather than a 500 (server error) — it tells clients to retry later."

**What to notice:** The model named specific error codes, gave pg-specific event handler
syntax, and distinguished error types in a way that actually affects your HTTP response
codes. None of that was possible without the context.

---

## Scenario 03 — Format Control

### Same content, three formats

**Request:** "List the main HTTP methods used in REST APIs."

**Without format instruction:**
> "The main HTTP methods are GET, POST, PUT, DELETE, and PATCH. GET retrieves resources,
> POST creates new ones, PUT replaces existing resources, PATCH partially updates them,
> and DELETE removes resources..."

**With "respond as a markdown table":**
> | Method | Purpose | Body? | Idempotent? |
> |--------|---------|-------|-------------|
> | GET | Retrieve a resource | No | Yes |
> | POST | Create a resource | Yes | No |
> | PUT | Replace a resource entirely | Yes | Yes |
> | PATCH | Partially update a resource | Yes | No |
> | DELETE | Remove a resource | Optional | Yes |

**With "respond as JSON":**
```json
[
  { "method": "GET", "purpose": "Retrieve a resource", "has_body": false, "idempotent": true },
  { "method": "POST", "purpose": "Create a resource", "has_body": true, "idempotent": false },
  ...
]
```

**Key insight:** The content is identical. The format instruction changes whether you
can paste the result into a spreadsheet, a config file, or a codebase directly.

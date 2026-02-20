# Module 06 — Solutions

Module 06 is primarily reflection — these scenarios don't have a single correct output.
This file gives you calibration points: what healthy vs unhealthy patterns look like.

---

## Scenario 01 — Context Management

### Signs of context degradation (what to look for)

In a long conversation, healthy model behaviour:
- Refers back to specifics you mentioned earlier ("you mentioned earlier that the token was JWT-based")
- Maintains consistent constraints ("I see the constraint was no new dependencies, so...")
- Asks when uncertain ("Did you say the error only happens on POST requests?")

Warning signs of context degradation:
- Gives an answer that contradicts a constraint you specified 10 messages ago
- Restates something you already agreed was wrong
- Uses vague language where it was previously specific ("the auth module" → "some authentication-related file")
- Agrees with contradictory statements without flagging the contradiction

### What the handoff prompt produces

If you ask the model:

> "Summarise this conversation in a way that captures all the decisions made, the
> current task state, and any constraints that should apply to future responses.
> Format it as a briefing I can paste into a new session."

A good response:

> **Session handoff — task management API**
>
> **Current task:** Adding input validation to `app.py` POST /tasks endpoint
>
> **Decisions made:**
> - Error format: `{"error": "validation failed", "detail": "..."}` (consistent with existing 404s)
> - Allowed priority values: low, medium, high (from PRIORITY_ORDER in tasks.py)
> - Allowed status values: open, in_progress, done (from VALID_STATUSES)
>
> **Constraints:**
> - Only modify app.py — no changes to tasks.py or storage.py
> - No new dependencies
> - Return 400 for validation failures
>
> **Not yet done:** The PUT /tasks/<id> endpoint also lacks validation — flagged but
> out of scope for this session.

You can paste this into a new session and pick up exactly where you left off.

---

## Scenario 02 — Validate and Verify

### The "prove it" challenge in action

You ask the model:

> "The Flask docs say you should always use `abort()` instead of returning error tuples directly."

The model answers:

> "Actually, Flask supports both approaches. `abort()` raises an exception that Flask's
> error handlers catch, which is useful for consistent error page rendering. Returning
> tuples (`return {'error': 'not found'}, 404`) is equally valid and often preferred in
> API contexts because it's more explicit.
>
> Here's the relevant Flask documentation passage:
> *'abort() raises an HTTPException — it's useful when you want to use Flask's error
> handling system. For APIs returning JSON, returning a tuple with a status code is
> simpler and more readable.'*"

**Issue:** You should verify that quote directly. Go to the Flask docs and search for
the exact wording. The model may have accurately paraphrased or may have invented a
plausible-sounding quote. Either is possible. If you can't find the quote, the model
confabulated it.

**The pattern:** When the model says "the docs say", "according to X", or quotes a
source — always check the primary source before trusting it.

---

## Scenario 03 — Judgment Calls

### Part A: Audit results — common patterns

Most developers find they're using AI for:
- **High-appropriate use:** boilerplate, explaining unfamiliar code, first-draft docs, test scaffolding
- **Low-appropriate use (that they hadn't noticed):** explaining unfamiliar APIs where the model's training data may be outdated, writing security-adjacent logic without independent review, taking output without reading it

The goal of the audit isn't a perfect score — it's to surface your actual patterns vs your intuition.

### Part B: Inverted flow — what changes

When you read the docs first, you typically notice:
- The model's summary was accurate but incomplete (it left out important caveats)
- The model slightly mischaracterised something (e.g., called a method deprecated that's just "legacy")
- You now have the vocabulary to ask a much more precise question

The inverted flow works because having any independent reference point makes it much
easier to spot errors. Without it, you're comparing the model's answer to itself.

### The reversibility test applied to this repo

| Task | Reversibility | Appropriate trust |
|------|--------------|-------------------|
| Using AI to write test cases for tasks.py | High | High |
| Using AI to explain what filter_by_priority does | High | High |
| Using AI to add validation to app.py | Medium (tests catch it) | Medium |
| Using AI to write the authentication logic for a real app | Low | Low — review line by line |
| Using AI to generate database migration scripts | Low | Low — run against a copy first |

The pattern: if you have tests and can run them, trust is higher. If the output goes
directly to production or users, trust is lower regardless of how confident the model sounds.

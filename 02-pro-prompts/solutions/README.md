# Module 02 — Solutions

---

## Scenario 01 — Few-Shot Prompting

### Zero-shot classification (no examples)

Commit message: `"update deps"`

A zero-shot model might classify this as:
- `chore` (reasonable)
- `fix` (wrong — this is maintenance, not a bug fix)
- `build` (also defensible)

You'll see different answers across runs. The model is guessing at your convention.

### Few-shot classification (with examples)

After showing 3 examples mapping your team's style to labels, the same commit:

> `chore`

And it stays `chore` across multiple runs. The model is now matching your pattern,
not guessing at a universal one.

**What to notice:** Few-shot examples don't just improve accuracy — they *define* what
"correct" means for your specific context. The model can't know your team's commit
convention unless you show it.

---

## Scenario 02 — Chain of Thought

### Without CoT

Question: "If a train leaves at 2pm travelling at 80mph, and another leaves the same
station at 3pm travelling at 100mph, when does the second train overtake the first?"

A common wrong answer (without CoT):
> "The second train overtakes at 4pm."

*(This is wrong — the correct answer is 7pm. The second train needs to close a 80-mile
gap at a closing rate of 20mph: 80 ÷ 20 = 4 hours after the second train departs.)*

### With CoT ("think step by step")

> "Let me work through this:
> 1. At 3pm (when the second train departs), the first train has been travelling for 1 hour at 80mph, so it's 80 miles ahead.
> 2. The second train travels at 100mph, the first at 80mph — the closing rate is 20mph.
> 3. Time to close an 80-mile gap at 20mph: 80 ÷ 20 = 4 hours.
> 4. 4 hours after 3pm = 7pm.
>
> The second train overtakes at **7pm**."

**What to notice:** The correct answer isn't just arrived at more reliably — you can
*check the reasoning*. If step 3 was wrong, you'd catch it. With the single-shot answer,
you have no way to audit. CoT makes reasoning falsifiable.

---

## Scenario 03 — Role Prompting

### Same code, two roles

```python
def login(username, password):
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    result = db.execute(query)
    return result.fetchone() is not None
```

**Role: senior security engineer**

> "This is a textbook SQL injection vulnerability. The username and password values are
> interpolated directly into the query string — an attacker can pass `' OR 1=1 --` as
> the username to bypass authentication entirely.
>
> The fix is parameterised queries:
> ```python
> db.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
> ```
>
> Additional issues: passwords appear to be stored in plaintext (you're comparing raw
> password strings). Use a hashing library like `bcrypt` with a per-user salt. Never
> store or compare raw passwords."

**Role: mentor reviewing a junior's code**

> "Good start — the query logic is on the right track. There's an important issue to
> address, though. When you build SQL strings by concatenating user input like this,
> it creates what's called SQL injection. Someone could type something unexpected as
> their username and bypass the login entirely.
>
> The standard fix is to pass the values separately from the query — your database
> library handles the escaping:
> ```python
> db.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
> ```
>
> One more thing to look into: how are passwords stored in the database? Storing them
> as plain text is a significant risk — worth a conversation with your team."

**What to notice:** The security finding is identical. The delivery, vocabulary, and
assumed audience differ completely. Role prompting is not about getting different
*content* — it's about calibrating *depth, tone, and framing* for your actual reader.

---

## Scenario 04 — Self-Critique

### Single-pass pitch

> "Introducing DataPulse — the real-time analytics platform that transforms your raw
> data into actionable insights in seconds. With our intuitive dashboard and AI-powered
> recommendations, teams can make faster, smarter decisions without needing a data
> science background. Start your free trial today and unlock the full potential of
> your data."

### After self-critique and revision

**Self-critique step:**

> "Weaknesses in the above:
> 1. 'actionable insights in seconds' is a claim without evidence or specificity
> 2. 'intuitive' is meaningless marketing language
> 3. No competitive differentiation — what does this do that Grafana/Mixpanel don't?
> 4. The call to action is generic
> 5. No target customer specified"

**Revised pitch:**

> "DataPulse connects to your existing data sources in under five minutes and gives
> non-technical team members a live view of the metrics that drive decisions — without
> writing SQL or waiting for the analytics team. Unlike general-purpose BI tools,
> DataPulse is built specifically for product and growth teams: pre-built templates
> for funnel analysis, retention curves, and A/B test results, with plain-English
> explanations of what changed and why.
>
> Try it free for 30 days — no data migration required."

**What to notice:** The revised pitch has specifics (under five minutes, names the
target team, names the templates). The critique step forced the model to name the
weaknesses it would otherwise have smoothed over. Self-critique works because it
creates a deliberate adversarial pass before finalising.

# Appendix — Cost and Model Selection

A practical reference for keeping API costs under control and choosing the right
model for the task.

---

## How you get charged

You pay for tokens — the sub-word units the model reads and writes. Every API call
has two costs:

- **Input tokens**: everything in the request — your system prompt, conversation
  history, any files or context you've attached.
- **Output tokens**: everything the model writes back.

Input is significantly cheaper than output (typically 3–5x cheaper per token).
A common mistake is generating long outputs when a short one would do: asking for
"a detailed explanation" when "a one-paragraph summary" is sufficient doubles or
triples the output cost for no benefit.

---

## Model tiers

| Model | Best for | Relative cost |
|-------|----------|---------------|
| **Haiku** | Classification, extraction, formatting, simple Q&A | Cheapest |
| **Sonnet** | General coding tasks, summarisation, reasoning | Mid-range |
| **Opus** | Complex reasoning, architecture decisions, nuanced writing | Most expensive |

The differences are real. A task that needs careful multi-step reasoning will
produce worse results on Haiku than on Opus. A task that just needs to classify
a support ticket into one of five categories will produce the same result on Haiku
as on Opus — and cost a tenth as much.

**Rule of thumb: start with Sonnet. Move to Haiku if the task is simple and speed
matters. Move to Opus if quality is critical and cost is acceptable.**

---

## Matching task to tier

**Use Haiku for:**
- Classifying or tagging items (support tickets, log levels, categories)
- Extracting structured data from text (parsing addresses, pulling fields from documents)
- Simple format conversion (JSON to YAML, reordering columns)
- High-volume, low-stakes tasks where you'll run many calls per minute

**Use Sonnet for:**
- General code generation and refactoring
- Summarisation and explanation
- Multi-step reasoning that doesn't require deep expertise
- Most everyday development tasks

**Use Opus for:**
- Architectural decisions and trade-off analysis
- Complex debugging where the model needs to hold many constraints simultaneously
- High-stakes writing where nuance matters
- Tasks where you've already tried Sonnet and found the quality insufficient

---

## Evals and repeated runs

The eval runner in Module 08 makes multiple API calls per task per trial. A typical
eval configuration — 3 trials across 2 tasks — generates approximately:

- 2 tasks × 3 trials = 6 graded attempts
- Each attempt: 1 generation call + 1 grading call = 2 API calls
- Total: ~12 API calls

Running evals at scale (many tasks, many trials, Opus for grading) adds up quickly.
A practical workflow:

1. Develop and iterate with Haiku or Sonnet to keep iteration cheap.
2. Run a final validation pass with Opus to confirm quality before shipping.
3. Use the grader model separately from the generation model — a Haiku grader
   is often sufficient to check whether an output meets a spec.

---

## Prompt caching

If your system prompt is long and repeated across many calls, prompt caching
significantly reduces cost. The model provider caches the prefix of your prompt,
and you pay a reduced rate on cache hits.

Caching helps when:
- You have a long, stable system prompt (instructions, few-shot examples, context)
- You're making many calls in a short window (evals, batch processing)
- The prompt is identical across calls (caching breaks if the prefix changes)

Caching does not help when:
- Each call has a unique prefix (user-specific context, timestamps in the prompt)
- You're making one-off calls rather than batches

To make caching effective, put stable content (system instructions, reference material)
at the top of your prompt and variable content (user input, current date) at the bottom.

---

## Keeping costs predictable

A few habits that prevent bill surprises:

- **Set a per-call output limit**: most APIs support a `max_tokens` parameter.
  Set it lower than the model's maximum. If a task should produce 200 tokens,
  don't leave the limit at 4096.
- **Log token counts in development**: most API responses include usage data.
  Log it. Surprising token counts usually indicate a prompt that's grown without
  you noticing.
- **Use streaming for UX, not for cost**: streaming doesn't reduce cost — it just
  makes the output feel faster. Don't confuse the two.
- **Audit long system prompts**: prompts grow over time. If your system prompt is
  over 1000 tokens, check whether all of it is still needed.

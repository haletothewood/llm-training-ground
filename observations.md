# My Observations

Use this file to record what you notice as you work through the modules. The scenarios
say "note the response" and "what did you observe" — this is where to write it down.

There are no right answers here. The value is in noticing patterns across multiple runs
and across modules. Things that surprised you are often the most useful to write down.

---

## Module 00 — How LLMs Work

### Scenario 01 — Memory and Context

**Part A: Did the model remember anything from the previous session?**


**Part B: At what point did the filler content cause accuracy to drop?**


**What surprised me:**


---

### Scenario 02 — Non-Determinism

**Part A: Unique recommendations across 5 runs (no CoT):**

| Run | Core recommendation |
|-----|---------------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

Unique answers: ___ / 5

**Part B: Unique recommendations across 5 runs (with CoT):**

| Run | Core recommendation |
|-----|---------------------|
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | |

Unique answers: ___ / 5

**Did CoT reduce variance? By how much?**


---

## Module 01 — Clear Prompting

### Scenario 01 — Vague vs Precise

**Vague prompt: how many clarifying questions did the model ask? Did it hallucinate a bug?**


**Precise prompt: was the output usable without editing?**


**What the precise prompt added (in words):** ___

**Was it worth it?**


---

### Scenario 02 — Context Setting

**Without context: what did the model assume about your situation?**


**With context: what specifically changed in the answer?**


---

### Scenario 03 — Format Control

**Which format instruction was hardest to get right?**


**Did any format instruction produce unexpected results?**


---

## Module 02 — Pro Prompts

### Scenario 01 — Few-Shot

**Zero-shot: how consistent was the classification across 3 runs?**


**Few-shot: did consistency improve? What was the ratio?**


---

### Scenario 02 — Chain of Thought

**Without CoT: did the model get the right answer?**


**With CoT: did the reasoning reveal any errors you could catch?**


---

### Scenario 03 — Role Prompting

**Which role produced the most useful output for your actual situation?**


**What changed between roles — depth, tone, vocabulary, or content?**


---

### Scenario 04 — Self-Critique

**What did the critique step catch that the first draft missed?**


**How different was the final output from what you'd have got in one pass?**


---

## Module 03 — Skills & Tools

### Scenario 01 — Using a Tool

**Did the model choose the right file to read without being told?**


**Did it make any mistakes in reading or interpreting the file?**


---

### Scenario 02 — Combining Tools

**How many steps did the model take autonomously?**


**Did it flag any limitations of its search?**


---

### Scenario 03 — Using a Skill

**What task in your workflow would most benefit from a skill?**


**Where did the skill break down? (When did the fixed template not fit?)**


---

## Module 04 — Agents

### Scenario 01 — Simple Agent Task

**How many files did the agent read?**


**Did it make any wrong inferences? What caused them?**


---

### Scenario 02 — Multi-Step Investigation

**Did the agent identify the correct root cause?**


**Did it stay focused or explore more files than needed?**


---

### Scenario 03 — Agentic Code Change

**Did the "plan first" step catch anything you'd have wanted to change?**


**Did the agent stay within the scope you set?**


---

## Module 05 — MCP Servers

### Scenario 01 — Using a Pre-Built Server

**How did the model indicate it was using an MCP tool vs built-in tools?**


**What could the MCP server do that built-in tools couldn't?**


---

### Scenario 02 — Understanding the Protocol

**What surprised you about the JSON-RPC tool definition format?**


---

### Scenario 03 — Building a Minimal MCP Server (optional)

**Did the tool description change how reliably the model used the tool?**


**What would you build for your actual workflow?**


---

## Module 06 — Critical Judgment

### Scenario 01 — Context Management

**Signs of degradation you spotted in a real conversation:**


**Did the handoff prompt produce a summary you could actually reuse?**


---

### Scenario 02 — Validate and Verify

**Did the "prove it" challenge expose any confabulation?**


---

### Scenario 03 — Judgment Calls

**From the Part A audit: any tasks you were using AI for that belong in the "risky" column?**


**Did the reversibility habit change how carefully you reviewed any output?**


---

## Module 07 — Making It Stick

### Scenario 01 — Project Rules

**Did the rules file change first-response quality? How?**


**What rule was most effective? What rule was ignored?**


**Where's the line between useful constraint and micromanagement?**


---

### Scenario 02 — Automate One Thing

**How did the automation-prompt quality compare to chat-prompt quality?**


**What broke on the first run? What did you change?**


**What would you automate next?**


---

### Scenario 03 — The Weekly Review

**Tracking table:**

| Date | Task | Form factor | Outcome | Again? |
|------|------|-------------|---------|--------|
| | | | | |

**Weekly summary:**

- Most common use case:
- Hit rate (useful / total):
- Net-negative tasks:
- Missed opportunities:
- Most common form factor:

**Personal rules of engagement:**

*Starter prompts — answer these after your week of tracking:*
- What's one class of task I'll now use AI for that I wasn't before?
- What's one situation where I'll require human review before acting on AI output?
- What's my rule for when to start a fresh conversation rather than continuing an existing one?

---

## Module 08 — Eval

### Scenario 01 — Eval a Prompt

**Prompt A average score:** ___ / 8

**Prompt B average score:** ___ / 8

**Delta (B minus A):**

**Which criterion showed the biggest difference?**


**How hard was it to score consistently on the rubric?**


---

### Scenario 02 — Eval a Skill

**Without rules file average:** ___ / 8

**With rules file average:** ___ / 8

**Delta:**

**Was the baseline surprisingly good? On which criteria?**


**Which rules had a visible effect? Which had none?**


**What did you change in the revised rules file?**


---

### Scenario 03 — Tessl Task Evals (optional)

**Skill evaluated:**

**Number of scenarios tested:**

**Pass rate with skill:** ___ %

**Pass rate without skill:** ___ %

**Number of negative deltas:**

**What changes did you make based on the results?**


---

## Overall patterns

**The technique I'll use most going forward:**


**The situation where I'll be most careful going forward:**


**The biggest thing this course changed about how I use AI:**


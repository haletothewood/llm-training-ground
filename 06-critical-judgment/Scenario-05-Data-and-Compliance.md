# Scenario 05 — Data and Compliance

## Goal
Develop a practical framework for deciding what data is safe to include in LLM
prompts, understand the compliance categories that affect that decision, and build
a habit of classifying data before pasting it.

## Background

Every token you send to a third-party API goes somewhere: into a request, into
server logs, and potentially into future training data or model evaluations. For
personal experiments with public information, this is rarely a concern. For
professional work involving real customer data, proprietary code, or regulated
information, it matters a great deal.

This isn't a legal guide. Regulations vary by jurisdiction, organisation, and
context. What this scenario gives you is a practical mental model: what categories
of data deserve caution, why, and what your options are when you need AI assistance
with sensitive material.

---

## The central question

Before pasting anything into an LLM prompt, ask:

> "Would I be comfortable if this text appeared in a training dataset or was reviewed
> by the API provider's staff?"

If yes, proceed.
If no, redact the sensitive parts before sending, or use a self-hosted model.

This isn't paranoia — it's the same question you'd ask before pasting data into
any third-party tool.

---

## Part A — Classify the data

Below are sample snippets. For each one, classify it as:

- **Safe**: no restrictions; fine to include in prompts to any third-party API
- **Caution**: may be appropriate in some contexts but warrants consideration
- **Never** (for third-party APIs): should only be processed by a self-hosted model
  or requires explicit legal/compliance review first

Work through these before reading the guidance below.

---

**Snippet 1:**
```
def calculate_discount(price: float, percentage: float) -> float:
    return price * (1 - percentage / 100)
```

**Snippet 2:**
```
Patient: Jane Smith, DOB: 1978-04-12
Diagnosis: Type 2 diabetes (E11.9)
Medication: Metformin 500mg twice daily
Last HbA1c: 7.2% (2024-11-03)
```

**Snippet 3:**
```
Error: Connection refused at db.internal.acme.com:5432
Database: acme_prod
User: app_service
```

**Snippet 4:**
```
The Fibonacci sequence starts: 1, 1, 2, 3, 5, 8, 13...
```

**Snippet 5:**
```
Customer: Acme Corp
Contract value: $2.4M ARR
Renewal date: 2025-06-30
Primary contact: bob.johnson@acmecorp.com
Pain points: slow onboarding, missing SSO
```

**Snippet 6:**
```
API_KEY=sk-prod-aBcDeFgHiJkLmNoPqRsTuVwXyZ
DATABASE_URL=postgres://admin:hunter2@db.prod.internal/main
```

**Snippet 7:**
```
SELECT u.email, u.name, o.total, o.created_at
FROM users u JOIN orders o ON u.id = o.user_id
WHERE o.created_at > '2024-01-01'
ORDER BY o.total DESC
LIMIT 100;
```
*(with actual results attached: 100 rows of real customer names, emails, and purchase amounts)*

---

### Guidance

**Safe**: Snippet 4 (public knowledge). Snippet 1 (generic utility function with no business context).

**Caution**: Snippet 7 (the query itself is probably fine; attaching real customer results makes it sensitive). Snippet 5 (CRM data — depends on your organisation's data handling agreements and the API provider's terms).

**Never for third-party APIs**:
- Snippet 2: protected health information (PHI). Regulated under HIPAA in the US, and equivalent frameworks elsewhere. Real patient data should not leave your compliance boundary without explicit legal clearance.
- Snippet 3: internal infrastructure details. Leaking DB hostnames, usernames, and internal service topology is a security risk even if no passwords are included.
- Snippet 6: credentials. This is the clearest case — never. Not in a prompt, not in a screenshot, not in a support ticket.

Snippet 1 sits at the boundary. A generic utility function is probably fine. If it's from a codebase where the function names or file structure would reveal proprietary architecture, that changes the calculus.

---

## Part B — Hosted vs self-hosted: what actually changes

Not all model access is equivalent. The data handling picture looks different depending
on how you're accessing the model.

| Access method | Who processes the data | Logs | Training use |
|---------------|----------------------|------|-------------|
| Third-party API (Anthropic, OpenAI, etc.) | Provider's infrastructure | Provider's logs | Check provider's terms — often opt-outable for API users |
| Provider's enterprise tier | Provider's infrastructure, stricter SLA | Reduced retention, often zero | Typically prohibited |
| Self-hosted open-weight model | Your infrastructure | Your logs | You control this |
| On-device model | Your device | Local only | You control this |

**The practical implication**: for most regulated data, the question isn't "can I use AI?"
— it's "can I use *this provider* with *this data*?" Self-hosted models collapse many of
the compliance concerns, at the cost of infrastructure complexity and (usually) some
capability.

For PHI specifically: running a fine-tuned open model on your own HIPAA-compliant
infrastructure may be legally defensible in a way that sending the same data to a
third-party API may not be, regardless of the provider's assurances.

---

## Part C — A practical framework for professional use

Before pasting any non-trivial content into a prompt at work, run through this:

### Step 1: What type of data is this?

| Category | Examples | Default stance |
|----------|----------|---------------|
| PII (personally identifiable information) | Names + email, name + address, any combination that identifies a real person | Caution — redact or use enterprise tier |
| PHI (protected health information) | Medical records, diagnoses, insurance data | Never (third-party API) without explicit clearance |
| Financial data | Account numbers, transaction records, credit card data | Never |
| Credentials and secrets | API keys, passwords, tokens | Never |
| Internal architecture | DB schemas, internal hostnames, service topology | Caution — assess exposure |
| Proprietary business logic | Pricing algorithms, customer scoring models | Caution — check employment agreements |
| Proprietary code (general) | Source code from a private repo | Caution — check employment agreements and API terms |
| Public or generic content | Open-source code, publicly available text, your own notes | Safe |

### Step 2: What's your context?

- Are you using a personal account or your organisation's enterprise API agreement?
- Does your organisation have a data handling policy for AI tools? (If yes, follow it.)
- Is the provider's data processing agreement consistent with your compliance requirements?

### Step 3: Redact, don't avoid

In many cases, you can get the AI assistance you need without sending the sensitive data.
Replace real values with placeholders:

Instead of:
```
This query is running slowly on our production database acme_prod:
SELECT * FROM users WHERE email = 'jane@acmecorp.com'
```

Send:
```
This query is running slowly. Help me optimise it:
SELECT * FROM users WHERE email = ?
```

The model doesn't need the real values to help with the SQL. Redact before sending.

---

## Regulatory categories to be aware of

This is not legal advice. These are awareness categories — if your work touches them,
involve someone with domain expertise.

**GDPR (EU)**: governs processing of personal data of EU residents. Sending EU resident
PII to a US-based API provider may require a Data Processing Agreement with that provider,
and the provider must meet adequacy requirements. Most major providers have DPAs available.

**HIPAA (US healthcare)**: governs PHI. Sending PHI to a third party requires a Business
Associate Agreement (BAA) with that party. Most major API providers offer a BAA on their
enterprise tier, not on standard consumer accounts.

**SOC 2**: a compliance framework for service providers, not a law. A provider being SOC 2
Type II certified means they've had their security controls independently audited. It's
a meaningful signal of operational maturity but does not by itself make them suitable
for PHI or payment card data.

**PCI-DSS (payment cards)**: governs cardholder data. Credit card numbers, CVVs, and
cardholder data should not be in LLM prompts, period.

---

## What to notice

- In Part A: were any classifications harder than you expected? Which ones?
- Did Snippet 1 (the utility function) feel safe? Does it change if the function is from
  a codebase you don't own?
- In Part C: have you ever redacted data before sending it to an AI tool, or has it
  been a habit you haven't built yet?

---

## Reflection questions

1. Your organisation has a policy that says "no customer data in AI tools." A colleague
   argues that the CRM data (Snippet 5) doesn't count as "customer data" because the names
   aren't included. How do you respond?
2. A self-hosted model gives you control over data, but requires infrastructure work and
   may have lower capability than frontier models. How do you weigh that trade-off for a
   task involving PHI?
3. Is there data you currently paste into AI tools that, after this exercise, you'd
   treat differently? What would you change?

---

## A note on trust

The question "is this data safe to send?" has two parts that people often conflate:
**technical** (will this data be logged, stored, or used for training?) and **legal**
(does my organisation, employment agreement, or applicable regulation permit this?).

API providers have gotten significantly better at the technical part — most offer
enterprise tiers with zero data retention and no training use. The legal part is
harder to generalise, because it depends on your jurisdiction, your organisation's
agreements, and the type of data involved.

The safest default for professional use: when in doubt, redact. The model rarely
needs the exact values to help you — it needs the structure. Send the structure,
not the data.

# Alignment Audit

Use this reference when the request is non-trivial and user intent is not yet precise enough to route, map, implement, or verify safely.

## Goal

Close the communication gap before the workflow spends its evidence budget. The output should make the next safe engineering action obvious.

## When to run

Run for:

- ambiguous scope, behavior, acceptance criteria, terminology, or non-goals
- optional unknowns-first output that identifies user-only decisions or architecture-changing uncertainty
- L3+ behavior changes
- design decisions with meaningful trade-offs
- requests that include vague terms like "better", "clean up", "support", "modernize", or "make robust"
- conflicting signals between the user's wording, docs, tests, and code

Skip for:

- typo fixes
- obvious local edits
- read-only explanations
- cases where the repo already answers the question and the verification signal is clear

## Protocol

Ask one question at a time. Each question must include:

- the decision being made
- why it matters
- the recommended answer
- the consequence of accepting the recommendation

Before asking, check whether the repository can answer the question. Prefer code, tests, then docs. If code answers it, report the evidence instead of asking.

When `references/unknowns-first/architecture-interview.md` was used, fold its recommended defaults and open user-only decisions into this audit instead of producing a second alignment artifact.

Walk upstream decisions first:

```text
intent -> user-facing behavior -> contract/API -> data shape -> side effects -> non-goals -> verification
```

Do not ask broad surveys like "Any other requirements?" Replace them with concrete scenarios:

- "Should invalid input be rejected at parse time or normalized before storage? Recommended: reject at parse time because the existing parser owns validation."
- "Should this include migration of old config files? Recommended: no, unless persisted configs already exist in supported releases."

## Stop condition

Stop when these are known:

- the requested outcome
- acceptance criteria
- non-goals
- owner component or first component to inspect
- compatibility constraints
- verification signal
- any user-only decisions that remain open

If a user-only decision remains open and blocks safe implementation, pause and ask. If the decision can be deferred safely, record the default and continue.

## Output

```md
## Alignment

- Resolved decisions:
- Recommended defaults accepted:
- Open user decisions:
- Acceptance criteria:
- Non-goals:
- Repo-answerable questions checked:
```

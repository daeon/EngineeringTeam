# Domain Context

Use domain context to make EngineeringTeam artifacts speak the repository's language.

This is a soft dependency. If the repository has no domain glossary or ADRs, continue with code-first evidence and note the gap only when it affects understanding or verification.

## Files

Most repositories use one context:

```text
/
├── CONTEXT.md
├── docs/
│   └── adr/
└── src/
```

Larger repositories may use multiple contexts:

```text
/
├── CONTEXT-MAP.md
├── docs/
│   └── adr/
└── packages/
    ├── billing/
    │   ├── CONTEXT.md
    │   └── docs/adr/
    └── auth/
        ├── CONTEXT.md
        └── docs/adr/
```

## CONTEXT.md rules

`CONTEXT.md` is a glossary, not a spec.

Include:

- canonical domain terms
- short definitions
- important relationships between terms
- confusing aliases to avoid
- resolved ambiguities

Exclude:

- implementation details
- task plans
- temporary hypotheses
- file inventories
- decisions that belong in ADRs

Suggested shape:

```md
# Project Context

## Language

**Canonical Term**:
Definition in domain language.
_Avoid_: overloaded synonym, stale term

## Relationships

- Term A owns many Term Bs

## Flagged ambiguities

- "Old phrase" previously meant X and Y. Resolved: use "Canonical Term" for X.
```

## ADR rules

Use ADRs sparingly. Offer or write one only when all three are true:

1. Hard to reverse: changing the decision later has meaningful cost.
2. Surprising without context: future maintainers will wonder why this path was chosen.
3. Real trade-off: credible alternatives existed and were rejected for specific reasons.

Suggested ADR shape:

```md
# Title

## Status

Accepted

## Context

## Decision

## Consequences

## Alternatives Considered
```

## How EngineeringTeam uses this

- Repo Atlas records whether domain context exists and where.
- Component Brief and Contract Graph use canonical terms when they clarify behavior.
- Evidence Ledger treats docs as supporting evidence, behind code and tests.
- Context garbage collection updates durable terms only when the task reveals reusable language.
- Final reports mention stale or missing context only when it affected confidence.

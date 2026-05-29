# Repo Intelligence Schema

Use this schema to build concise, evidence-backed repo understanding before implementation.

## Repo Atlas

```md
# Repo Atlas

## System Type
## Main Languages / Frameworks
## Runtime / Build Model
## Main Components
## Entry Points
## Test Surfaces
## Domain Context
## Relevant ADRs
## Generated Code Rules
## Config / Schema Sources
## External Integration Points
## Known High-Risk Areas
## Repo-Specific Instructions
## Build / Test Commands
## Last Verified
```

## Component Brief

```md
# Component Brief

## Relevant Component
## Responsibility
## Important Files
## Relevant Symbols
## Main Call Path
## Related Tests
## Similar Existing Patterns
## Inputs / Outputs
## Side Effects
## Open Questions
## Evidence
```

## Rules

- Keep the atlas concise.
- Prefer code and executable commands over stale docs.
- Read `CONTEXT.md`, `CONTEXT-MAP.md`, and relevant ADRs when present; treat them as soft dependencies.
- Use canonical domain vocabulary in repo artifacts when a glossary defines it.
- Record whether domain context exists and where under `## Domain Context`; record relevant ADR paths under `## Relevant ADRs`.
- Cite file paths and symbols for every important claim.
- Expand context only when it reduces implementation or verification risk.
- Do not persist one-off task details as durable repo knowledge.

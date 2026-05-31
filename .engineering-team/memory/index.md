# EngineeringTeam Memory Index

Project-scoped memory is advisory context for EngineeringTeam work in this repository.

## Guardrails

- Current source code, tests, and generated outputs win over memory.
- Treat memory as a starting point; verify against the repo before relying on it.
- Do not store secrets, credentials, private user information, temporary logs, or speculation.
- Every durable memory entry should include evidence/source paths.
- Do not store raw Run Ledger content in memory; promote only curated memory candidates.

## Memory Files

Populated with evidence-backed entries (last verified 2026-05-29). Re-verify against current source before relying on any entry.

- `repo-atlas.md` — reusable repository map, entry points, build/test commands, and generated-code rules.
- `component-briefs.md` — durable component ownership notes, important files/symbols, and common call paths.
- `contracts.md` — producer/consumer contracts, data shapes, integration boundaries, and known failure modes.
- `verification.md` — validated commands, coverage notes, and recurring environment constraints.
- `gotchas.md` — evidence-backed pitfalls, recurring failure modes, and stale-context warnings.

## Entry Template

```md
## <short title>

- Status: current | needs-verification | stale
- Summary:
- Evidence/source paths:
- Origin run:
- Last verified:
- Confidence: high | medium | low
- Review trigger:
```

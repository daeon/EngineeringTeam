# Unknowns-First Fused Workflow Example

This example shows how the optional unknowns-first layer fuses into EngineeringTeam artifacts instead of replacing them.

## Request

```text
Use engineering-team to make this config loader support workspace-level overrides without breaking existing project configs.
```

## Unknowns-First Route

- Used: yes
- Reason: compatibility and ownership are unclear; existing configs may have hidden consumers.
- Phase loaded: `references/unknowns-first/blindspot-pass.md`, then `references/unknowns-first/risk-first-plan.md` if overrides affect persistence.
- Artifact target: Intake, Component Brief, Contract Graph, Evidence Ledger, Implementation Gate.
- Re-entry trigger: tests or docs reveal generated config schemas or migration requirements.

## Intake

- Mode: implementation
- Primary task type: migration / compatibility
- Autonomy level: L4 if multiple packages consume config, otherwise L3
- Risk mode: migration/compatibility
- First areas to inspect: config schema, loader entry point, default config fixtures, tests, release notes

## Contract Graph

| Edge | Producer | Contract / Data Shape | Consumer | Failure Mode | Coverage |
|---|---|---|---|---|---|
| Project config file -> loader | User config | Existing project-level keys | Runtime config object | Workspace override masks project config unexpectedly | Existing config-loader tests |
| Workspace override -> merge policy | New override source | Precedence and validation rules | Loader consumers | Compatibility break for existing projects | New precedence test |

## Risk-First Decisions

| Decision | Default | Alternatives | Why default | Invalidating discovery | Verification |
|---|---|---|---|---|---|
| Override precedence | Workspace fills missing values only | Workspace always wins | Preserves existing project configs | Docs already promise workspace wins | Fixture covering both values |
| Migration | No automatic rewrite | Rewrite old configs | Avoids irreversible edits | Supported releases require persisted migration | Migration test or release note check |

## Implementation Gate

- Files allowed to change: loader, config schema, focused tests, docs for precedence.
- Missing evidence: none after call path and fixtures are inspected.
- Verification required: config-loader unit tests and package validation.
- Rollback path: remove override parsing and precedence docs; existing config path remains intact.

## Final Report Shape

The final response should summarize behavior changed, behavior preserved, compatibility risk, verification, rollback, and any residual assumptions using `references/final-report.md`.

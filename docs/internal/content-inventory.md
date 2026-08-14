# Content Inventory And Distillation Record

This record describes the consolidated package introduced in 0.2.0. The repository exposes one discoverable skill and keeps detailed procedures as progressive-disclosure resources inside that bundle.

## Canonical Structure

| Area | Authority | Contract |
|---|---|---|
| Skill entrypoint | `skills/engineering-team/SKILL.md` | The only recursive `SKILL.md` and the only top-level entry under `skills/`. |
| Mode routes | `skills/engineering-team/references/route-*.md` | Five directly linked routes: codebase, debugging, logs, performance, and handoff. |
| Shared workflow | `skills/engineering-team/references/*.md` | Intake, mapping, evidence, gating, verification, closeout, and memory procedures loaded only when needed. |
| Artifacts | `skills/engineering-team/templates/*.md` | Fill-in structures used by routes and shared workflow references. |
| Specialist sources | `agents-src/*.yaml` | Eleven spawnable specialist definitions; the main session owns Lead responsibility. |
| Generated agents | `agents/`, `.codex/agents/`, `.github/agents/`, `skills/engineering-team/assets/agents/` | Generated from specialist sources; never edit by hand. |
| Public guidance | `README.md`, `docs/*.md` | Summarizes behavior and links to canonical skill/reference files. |
| Durable repo context | `.engineering-team/memory/*.md` | Evidence-backed repository facts, not task transcripts. |

## Authority Modes

| Mode | Source writes | Permitted output |
|---|---:|---|
| Implementation | After evidence and implementation gates | Smallest authorized patch plus verification and closeout artifacts. |
| Read-only analysis | Never | Evidence-backed report and next probes only. |
| Handoff | Never | One continuation artifact only; no source/config edits. |

## Hard Validation Contracts

- `validate_single_skill_contract()` recursively requires exactly `skills/engineering-team/SKILL.md` and rejects extra top-level `skills/` entries.
- `validate_no_spawnable_lead()` requires the Lead source and all four generated Lead outputs to remain absent.
- Every backticked `references/*.md` token in the main skill and bundled references must resolve.
- The five route references and selected workflow references/templates retain their required headings.
- Generated specialist outputs must match `agents-src/*.yaml`; `AGENTS.md` and generated `CLAUDE.md` must remain synchronized.
- Manifests share one version, session-start hooks remain absent, and the OpenCode plugin must parse.

## Consolidation Decisions

| Former item | 0.2.0 destination | Reason |
|---|---|---|
| `skills/codebase-analysis/SKILL.md` | `references/route-codebase-analysis.md` | Preserve procedure without creating a second skill trigger. |
| `skills/debugging-forensics/SKILL.md` | `references/route-debugging.md` | Keep read-only authority explicit under one router. |
| `skills/log-forensics/SKILL.md` | `references/route-log-analysis.md` | Keep log handling and output contract route-local. |
| `skills/performance-forensics/SKILL.md` | `references/route-performance.md` | Preserve measurement-first behavior under one router. |
| `skills/handoff/SKILL.md` | `references/route-handoff.md` | Model handoff as artifact-only authority, not a standalone skill. |
| `references/analysis-routing.md` | Four focused read-only route references | Remove a second routing layer and make the main skill's choice direct. |
| `agents-src/lead-engineer.yaml` and outputs | Main-session Lead rules in `SKILL.md` and `agent-routing.md` | Prevent a Lead from spawning another Lead and clarify ownership. |
| `skills/d3-viz` gitlink | Removed | It was unrelated to the EngineeringTeam skill contract. |

## Maintainer Rule

Change the smallest canonical layer: routing in `SKILL.md`, route procedure in the matching `route-*.md`, shared procedure in its reference, artifact shape in its template, or specialist behavior in `agents-src/*.yaml`. Update validators and public migration guidance in the same change whenever the package contract changes.

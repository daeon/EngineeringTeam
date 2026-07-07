# Unknowns-First Router

Use this optional pre-intake layer when a task has enough ambiguity that EngineeringTeam should expose assumptions before it spends the full evidence budget.

## Trigger rules

Run the smallest useful unknowns-first phase when the request is non-trivial and any of these signals are present:

- ambiguous outcome, scope, acceptance criteria, terminology, or non-goals
- unfamiliar component, unclear owner, or missing call path
- architecture-changing, security-sensitive, migration-sensitive, release-sensitive, production-impacting, or irreversible work
- high-impact behavior change with weak or stale evidence
- conflicting signals between user wording, code, tests, docs, generated outputs, logs, or runtime observations
- assumption-heavy implementation where an early cheap probe could invalidate the plan

Do not run it automatically for every L2+ task. `references/intake-risk.md` still owns autonomy level and risk mode.

## Skip rules

Skip unknowns-first for:

- typo fixes, formatting, or obvious one-file edits
- read-only explanation of a known local fact
- repo-answerable questions where code, tests, or docs already provide the answer
- emergency user instructions where the next safe action is already explicit and reversible
- tasks where the user explicitly asks for the existing fast path and risk is low

If a skipped task reveals ambiguity, re-enter this router and record the reason.

## Smallest useful phase

Choose only the phase that reduces immediate risk:

| Signal | Load | Output maps to |
|---|---|---|
| General ambiguity or hidden assumptions | `references/unknowns-first/blindspot-pass.md` | Repo Atlas notes, Evidence Ledger assumptions, Run Ledger residual risk |
| Architecture-changing uncertainty | `references/unknowns-first/architecture-interview.md` | Alignment Audit open decisions and recommended defaults |
| Concrete options need a cheap comparison | `references/unknowns-first/prototype-reference-probe.md` | Component Brief references, options considered, non-production artifacts |
| Plan depends on risky defaults | `references/unknowns-first/risk-first-plan.md` | Implementation Gate, Impact Map, verification strategy |
| Implementation diverges from assumptions | `references/unknowns-first/implementation-notes-log.md` | Run Ledger deviations, skipped checks, follow-ups |
| Reviewer needs a compact explanation | `references/unknowns-first/change-explainer-quiz.md` | Final Report, rollback, reviewer checklist |
| Need quick triage only | `references/unknowns-first/risk-score.md` | Intake support only |

## Artifact mapping

Unknowns-first creates no parallel artifact system. Write outputs into the existing EngineeringTeam artifacts:

- route decision and risk mode -> `references/intake-risk.md`
- assumptions and blind spots -> `references/evidence-ledger.md` and `references/run-ledger.md`
- user-only decisions -> `references/alignment-audit.md`
- options and references -> `references/component-brief.md`
- defaults, alternatives, and invalidators -> `references/implementation-gate.md` and `references/impact-map.md`
- deviations and skipped checks -> `references/run-ledger.md`
- reviewer explanation and rollback -> `references/final-report.md`

## Output

```md
## Unknowns-first route

- Used: yes / no
- Reason:
- Phase loaded:
- Artifact target:
- Skip rationale:
- Re-entry trigger:
```

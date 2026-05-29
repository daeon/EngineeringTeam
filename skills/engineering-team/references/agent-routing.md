# Agent Routing

## Score agents (0–3)

- 0 = not useful; 1 = possibly useful; 2 = useful; 3 = essential

| Task signal | Lead | Investigator | Implementer | Verifier | Skeptic | Advisor | Architect | Security | Optimization | Migration | Release | DX |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| small typo/local obvious edit | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| failing/flaky test | 3 | 3 | 1 | 3 | 3 | 0-1 if unresolved | 0-1 | 0-1 | 1-2 if timing/concurrency | 0 | 0 | 0 |
| bug/root cause | 3 | 3 | 2 | 2 | 3 | 2-3 if unclear/conflicting | 1-2 if boundary implicated | 1-3 if trust/input/auth | 1-3 if hot path | 1-3 if legacy | 1 if prod | 0 |
| feature implementation | 3 | 2 | 3 | 2 | 2 | 1-2 if assumption-heavy | 2 if API/boundary | 2-3 if exposed/user input | 1-2 if hot path | 1-2 if compatibility | 1-2 if rollout | 1-2 if UX/docs |
| broad refactor | 3 | 2 | 3 | 2 | 3 | 2 if cross-component | 3 | 1-2 | 1-2 | 1-2 | 1 | 0 |
| architecture/API design | 3 | 2 | 1-2 | 1-2 | 3 | 2-3 if consequential | 3 | 1-2 | 1-2 | 1-2 | 1-2 | 1-2 |
| security-sensitive change | 3 | 2 | 2 | 2 | 3 | 2-3 if L5/uncertain | 1-2 | 3 | 1 | 1 | 1-2 | 0 |
| performance investigation | 3 | 2 | 1-2 | 2 | 3 | 1-2 if production-sensitive | 1-2 | 0-1 | 3 | 0-1 | 1 | 0 |
| read-only codebase analysis | 3 | 3 | 0 | 0-1 | 1-2 | 0-1 if consequential | 2-3 | 0-1 | 0-1 | 0-1 | 0 | 1 |
| read-only debugging forensics | 3 | 3 | 0 | 1-2 for repro commands | 3 | 1-2 if unclear/conflicting | 1-2 if boundary implicated | 1-2 if trust/input/auth | 1-2 if timing/hot path | 1 if legacy | 1 if prod | 0 |
| read-only log forensics | 3 | 2 | 0 | 0-1 | 3 | 1-2 if incident-sensitive | 0-1 | 1 if sensitive data | 1-2 if latency/saturation | 0-1 | 2-3 for observability/rollback | 0 |
| migration/compatibility | 3 | 2 | 2 | 2 | 3 | 2-3 if irreversible/ambiguous | 1-2 | 1-2 if semantics/security | 1 if scale | 3 | 1-2 | 0 |

## Agent descriptions

| Agent | Spawn when score is 2-3 |
|---|---|
| Lead Engineer (`lead_engineer`) | Always; usually the main session acts as lead |
| Codebase Investigator (`codebase_investigator`) | Unknown repository impact, bug, feature, refactor, migration, test discovery |
| Implementation Engineer (`implementation_engineer`) | Code change likely after evidence gate |
| Test / Verification Engineer (`test_verification_engineer`) | Behavior change, bug, flaky test, regression, CI issue, quality risk |
| Evidence Skeptic (`evidence_skeptic`) | Any non-trivial task, unclear root cause, high-risk change, conflicting evidence |
| System Design Architect (`system_design_architect`) | Architecture, broad refactor, public API, module boundary, long-term maintainability |
| Security Analyst (`security_analyst`) | Trust boundary, auth, permissions, secrets, user input, shell, filesystem, network, dependency risk |
| Optimization Engineer (`optimization_engineer`) | Latency, throughput, memory, CPU, IO, concurrency, scalability, caching, polling, benchmark validity |
| Migration Analyst (`migration_analyst`) | Legacy behavior, compatibility, schema/config/API translation, import/export, upgrade path |
| Release / Rollback Engineer (`release_rollback_engineer`) | Production risk, deployment, rollout, feature flag, rollback, observability |
| DX / Documentation Reviewer (`dx_documentation_reviewer`) | User-facing docs, CLI behavior, error messages, developer ergonomics, onboarding, examples |
| Advisor Consultant (`advisor_consultant`) | Gate-only second opinion for L4/L5, unclear root cause after investigation, conflicting evidence, security/migration/release/production-sensitive decisions, or assumption-heavy completion checks |

Conceptual read-only roles may be simulated with installed agents when no native agent exists: Codebase Cartographer maps repositories, Runtime Trace Analyst traces execution, Reproduction Engineer designs repro probes, Log Forensics Analyst reconstructs timelines, Observability Architect evaluates telemetry, and Performance Investigator designs measurements.


## Skill routing graph

For selecting between implementation and read-only investigation skills, load `references/analysis-routing.md`. It contains the high-level routing graph from `engineering-team` to `codebase-analysis`, `debugging-forensics`, `log-forensics`, `performance-forensics`, implementation workflow, and `handoff`, plus the conceptual specialist roles useful for each path.

## Selection rules

- Always include Lead Engineer as coordinator.
- Spawn all agents scored 3.
- Spawn agents scored 2 only when they cover a distinct risk area.
- Include Evidence Skeptic for non-trivial L3+ work.
- Include Advisor Consultant only when a risk gate requires independent decision review.
- Initially cap at 5 teammates unless the task is clearly complex.
- If more than 5 agents score 2-3, spawn the top 5 first and defer the rest with explicit triggers.

## Routing output

```md
## Agent routing

| Agent | Score | Reason | Initial question |
|---|---:|---|---|

## Deferred agents

| Agent | Why deferred | Spawn trigger |
|---|---|---|
```

## Single-session simulation

When subagents are unavailable or not warranted, simulate specialist roles in the main session. Label each reasoning step with the active role so the work is auditable:

```text
[Investigator] Searched for all callers of X — found 3 files: ...
[Skeptic] Claim "X is unused" is unproven: grep shows Y still imports it.
[Lead] Revised plan: patch X but preserve Y's import path.
[Verifier] Ran targeted tests: 2 pass, 0 fail.
```

Rules for single-session simulation:
- At minimum simulate Lead, Investigator, and Skeptic for L3+ work.
- The Skeptic step must run before implementation — not after.
- Do not skip a role because you believe its conclusion is obvious.

## Team creation and fallback

If the harness supports subagents and a proactive trigger is met, delegate bounded work using `templates/subagent-brief.md`. If subagents are unavailable, unsafe, or not worth the overhead, simulate the roles in the main session while preserving the same evidence and implementation gates.

Rules:
- The current session is the Lead Engineer.
- Give teammates task-specific context; teammates do not inherit full conversation history.
- Assign non-overlapping questions.
- Require independent investigation before deliberation.
- During investigation, teammates must not edit files.
- Avoid concurrent edits to the same file.

## Context budget policy

`references/subagent-context-policy.md` owns the canonical context-budget table (`brief-only`, `component-context`, `artifact-context`, `full-context`). Select the smallest useful budget for every teammate.

Default Advisor Consultant to `brief-only` with `fork_context: false`. Use `fork_context: true` and `full-context` only when the lead cannot safely summarize; state the reason explicitly.

## Deliberation protocol

Before implementation, every selected teammate answers:

1. What do you believe is true?
2. What evidence supports it?
3. What could make you wrong?
4. What is the smallest safe next action?
5. What should not be changed?

The Lead Engineer synthesizes one plan. Resolve contradictions with evidence or targeted follow-up checks. Do not concatenate opinions; do not average contradictory conclusions.

## Adaptive spawning

Spawn additional specialists when evidence justifies them:

- Auth middleware touched → Security Analyst
- Public interface changed → System Design Architect
- Polling, caching, locking, batching, buffering, memory ownership touched → Optimization Engineer
- Legacy/config/schema conversion touched → Migration Analyst
- Runtime/prod behavior changed → Release / Rollback Engineer
- CLI/docs/error behavior changed → DX / Documentation Reviewer

## Proactive subagent triggers

Spawn a read-only investigator when:

- more than 5 files may be relevant
- ownership is unknown
- the same term appears in multiple components
- generated code may be involved
- public API, config, schema, or contract boundary may be touched

Spawn Evidence Skeptic when:

- root cause is inferred but not proven
- docs, tests, runtime behavior, or code disagree
- a proposed fix changes behavior
- the plan depends on "probably", "seems", "unused", or "should be safe"

Spawn Test / Task Runner when:

- test/build output may be long
- dependency setup may be noisy
- failure attribution requires command output
- the main context should not absorb logs

Spawn a domain specialist when:

- a distinct risk domain appears
- the specialist has a bounded question
- the result can be summarized as a context capsule

## Delegation envelope

Every subagent assignment must include:

- role
- mission
- context budget
- allowed tools
- inputs
- output limit
- required output
- explicit "do not" boundaries

Use `templates/subagent-brief.md`.

## Context capsule rule

Every subagent returns a context capsule using `templates/context-capsule.md`.

The Lead Engineer reads capsules, not full transcripts, unless a capsule is insufficient or contradictory.

## Main agent ownership

The Lead Engineer owns the final decision.

Subagent findings are evidence, not authority. The Lead must reconcile contradictions using the Evidence Ledger and, when needed, Advisor Gate.

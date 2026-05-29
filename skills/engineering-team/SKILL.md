---
name: engineering-team
description: "Use for non-trivial software engineering: map the repo before edits, classify risk, route the smallest useful EngineeringTeam, trace contract graphs, require evidence, implement safely, verify changes, and preserve reusable repo knowledge."
---

# EngineeringTeam

Use this skill when the user asks a coding agent to investigate, implement, debug, refactor, review, optimize, secure, migrate, or verify software and the task is not an obvious one-line edit.

Invocation patterns:

- Explicit: mention `engineering-team` in the prompt or choose it from `/skills`.
- Implicit: a harness may choose this skill when the task matches the description.
- Subagents: spawn specialists only when explicitly asked or when the harness policy permits it. When subagents are unavailable, perform the same role checks in the main session.

Do not rely on this skill as a giant memory file. Load references and scripts only when needed.

# EngineeringTeam

Coordinate a software engineering task using a repo-first harness workflow and the smallest useful set of expert agents.

## Core philosophy

Do not treat this as a giant prompt. Treat it as an engineering harness.

The goal is not merely to answer or patch code. The goal is to build enough repo intelligence to make a small, safe, evidence-backed change.

Default flow:

```text
Task
  → classify risk
  → choose risk mode and context budget
  → align on user intent when scope, behavior, or L3+ risk requires it
  → select smallest useful agent team
  → build repo atlas
  → build component brief
  → trace contract graph
  → create evidence ledger
  → run advisor gate when risk mode requires it
  → pass implementation gate
  → patch
  → verify
  → attribute failures
  → hand off
  → garbage-collect context
```

## Non-negotiable rule

Move from broad context to narrow context before editing:

```text
repo map → component map → feature map → contract graph → focused files → change plan → implementation → verification
```

Never jump directly into editing unless the owning component, affected contract, call path, risk level, and verification strategy are clear.

When user intent is ambiguous, align before mapping too deeply. Ask one question at a time, include the recommended answer, and explore the repo instead of asking whenever the repo can answer the question.

## When to use this skill

Use for non-trivial software engineering work involving any of these:

- debugging, regressions, flaky tests, crashes, root-cause analysis
- feature implementation or behavior changes
- refactoring that may alter design, ownership, contracts, or tests
- architecture, APIs, interfaces, module boundaries, dependency direction
- security-sensitive code, trust boundaries, auth, permissions, inputs, secrets, shell/filesystem/network access, dependency risk
- performance, latency, throughput, memory, CPU, IO, caching, batching, polling, locking, concurrency, scalability
- migration, compatibility, legacy behavior, schema/config/API translation, imports/exports, upgrades
- release, rollout, rollback, observability, production behavior, operational risk
- PR or diff review requiring multiple lenses
- codebase audit, analysis, feedback, or improvement planning without implementation
- user asks for agents, teams, deliberation, debate, review board, red team, or coordination

## When not to use a full team

Avoid spawning a full team when:

- the task is a typo, formatting fix, or obvious local edit
- work is sequential and mostly in one file
- same-file conflicts are likely
- one focused subagent is cheaper and safer
- the user asked only for a concise answer

For small tasks, still perform minimal repo orientation before editing.

## Required mental model

Before implementation, the lead must be able to say:

```text
I know where this behavior enters the system,
where it is transformed,
where it leaves the system,
which contracts it depends on,
how it can fail,
and how I will verify the change.
```

If that is not true, keep mapping.

---

# Phase 1: Intake and risk classification

Restate the task in engineering terms.

Identify:

- requested outcome
- known files, symptoms, or components
- constraints from the user
- risk level
- unknowns that must be resolved from the repo
- expected deliverable

Classify the task into one or more types:

1. Bug investigation
2. Feature implementation
3. Refactor
4. Architecture / design
5. Security
6. Performance / optimization
7. Test / verification
8. Migration / compatibility
9. Release / operations
10. Documentation / developer experience

Assign an autonomy level:

| Level | Meaning | Required before edit |
|---|---|---|
| L0 | Read-only exploration or analysis (no edits) | Repo Atlas + Analysis Report |
| L1 | Plan only | Repo Atlas |
| L2 | Local patch, no behavior change | Component Brief + nearby pattern/test |
| L3 | Behavior change | Contract Graph + regression test or verification path |
| L4 | Multi-component change | Impact Map + specialist review |
| L5 | Architecture, migration, security, release, or production-sensitive change | Explicit constraints + rollout/rollback plan + skeptic gate |

Choose one primary risk mode:

| Risk mode | Meaning | Default routing |
|---|---|---|
| `low-risk-local` | Obvious local edit or explanation | Lead only; no advisor |
| `behavior-change` | Local behavior, tests, or contracts may change | Verifier + skeptic as needed; use diagnosis loop for bug-driven changes |
| `cross-component` | Multiple modules, packages, services, or owners | Investigator + architect + skeptic |
| `security-sensitive` | Trust boundary, auth, inputs, secrets, shell, filesystem, network, dependency risk | Security + skeptic; advisor for L5 or uncertainty |
| `migration/compatibility` | Legacy behavior, config/schema/API translation, upgrade or import/export risk | Migration + release + skeptic; advisor for irreversible or ambiguous choices |
| `release/production` | Runtime, rollout, rollback, observability, live system, or production behavior | Release + advisor; human approval before sensitive side effects |
| `uncertain-root-cause` | Investigation has not converged on evidence-backed root cause | Investigator + skeptic + advisor before implementation; feedback loop before hypotheses |
| `conflicting-evidence` | Source, tests, docs, logs, or runtime observations disagree | Investigator + skeptic + advisor before implementation |

Always produce this artifact — even for L0 tasks — it is the routing receipt that makes the risk classification auditable.

Output:

```md
## Intake

- Task:
- Scope:
- Primary task type:
- Secondary task types:
- Autonomy level:
- Risk mode:
- Initial assumptions:
- Known constraints:
- First areas to inspect:
```

**L0 fast path:** When autonomy level is L0, proceed directly to Phase 4 then Phase 4.5 (Analysis Report). Skip Phases 1.5 through 3.5 and Phases 5 through 13. Phase 14 (Context GC) still applies.

L0 tasks include: codebase audits, feedback requests, "analyze this repo", "what are the risks here?", architecture surveys with no planned change, and PR or diff reviews that produce findings only.

---

# Phase 1.5: Alignment and audit gate

Use this gate when scope, behavior, acceptance criteria, terminology, or trade-offs are ambiguous, or when autonomy is L3 or higher. Skip it for `low-risk-local` work where the request and verification path are already clear.

Rules:

- Ask one question at a time.
- Include the recommended answer and why.
- If a question can be answered from the repository, inspect the repo instead of asking the user.
- Walk dependencies between decisions in order; do not ask downstream questions before the upstream choice is resolved.
- Challenge vague or overloaded terms and propose precise wording.
- Stop the audit when the next safe action, acceptance criteria, non-goals, and verification signal are clear.

Output when the gate runs:

```md
## Alignment

- Resolved decisions:
- Recommended defaults accepted:
- Open user decisions:
- Acceptance criteria:
- Non-goals:
- Repo-answerable questions checked:
```

See `references/alignment-audit.md` for the detailed protocol.

---

# Phase 2: Score and select agents

Do not spawn a fixed team by default. More agents do not automatically create better answers.

Score each candidate agent from 0 to 3:

- 0 = not useful
- 1 = possibly useful
- 2 = useful
- 3 = essential

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

Selection rules:

- Always include Lead Engineer as coordinator.
- Spawn all agents scored 3.
- Spawn agents scored 2 only when they cover a distinct risk area.
- Include Evidence Skeptic for non-trivial L3+ work.
- Include Advisor Consultant only when a risk gate requires independent decision review.
- Initially cap at 5 teammates unless the task is clearly complex.
- If more than 5 agents score 2-3, spawn the top 5 first and defer the rest with explicit triggers.

Do not invoke Advisor Consultant for obvious one-line edits, simple shell answers, routine low-risk docs, or cases where local evidence already proves the next action.

Output:

```md
## Agent routing

| Agent | Score | Reason | Initial question |
|---|---:|---|---|

## Deferred agents

| Agent | Why deferred | Spawn trigger |
|---|---|---|
```

---

# Phase 3: Create the team or fallback

If the user explicitly requests subagents, parallel review, or agent-team coordination, spawn Codex subagents or custom agents. Otherwise, simulate the roles in the main Codex session while preserving the same evidence and implementation gates.

Prefer Codex built-in agents when custom agents are not installed: use `explorer` for read-heavy mapping and `worker` for focused implementation. If this package's `.codex/agents/*.toml` files have been copied into `.codex/agents/` or `~/.codex/agents/`, use the matching custom agents.

Rules:

- The current session is the Lead Engineer.
- Give teammates task-specific context; teammates do not inherit full conversation history.
- Assign non-overlapping questions.
- Require independent investigation before deliberation.
- During investigation, teammates must not edit files.
- Use the shared task list when available.
- Avoid concurrent edits to the same file.
- Codex subagents produce compact artifacts, not verbose essays. The lead session consolidates results and makes the final decision.

---

# Phase 3.5: Context budget policy

Select the smallest useful context package for every teammate:

| Context budget | Use for | Contents |
|---|---|---|
| `brief-only` | Advisor default, security/release decision checks, narrow review | Curated decision brief only |
| `component-context` | Focused specialist work | Component Brief plus focused file paths/symbols |
| `artifact-context` | Multi-step review or verification | Repo Atlas, Contract Graph, Evidence Ledger, Verification Plan |
| `full-context` | Rare fallback when the lead cannot safely summarize | Full-history fork; state why in the brief |

Default Advisor Consultant to `brief-only` with `fork_context: false`. Use `fork_context: true` and `full-context` only when the lead cannot safely summarize enough context; state the reason under `Uncertainty`.

If a full-history fork rejects explicit custom model or reasoning settings, retry in the runtime-supported way instead of pasting the entire conversation into the advisor brief.

---

# Phase 4: Repo orientation and Repo Atlas

Before focusing on the requested area, inspect the repository at a shallow level.

Look for:

- `AGENTS.md`, `CLAUDE.md`, repo-local skill docs, harness instructions
- `CONTEXT.md`, `CONTEXT-MAP.md`, and `docs/adr/` for domain language and prior decisions
- `README.md`, `CONTRIBUTING.md`, architecture docs
- build files, package manifests, dependency files
- test configuration and CI configuration
- source roots, scripts, tools, codegen definitions
- route/entry-point files
- config/schema files

Treat domain docs as a soft dependency: use them when present, but do not block work when they are absent. If `CONTEXT.md` defines project terms, use that vocabulary in artifacts, plans, tests, and final reports. If ADRs exist near the touched area, respect them unless current evidence justifies reopening the decision. See `references/domain-context.md` for glossary and ADR rules.

Prefer structured repo intelligence over raw file reading.

Use or produce:

- file tree summary
- symbol index
- import/dependency graph
- test map
- route/handler map
- config/schema map
- generated-code map
- external integration map

Required artifact for L2+ tasks. For L0 analysis tasks, a concise prose summary with file-path-backed evidence is sufficient — see Phase 4.5.

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

Do not turn the Repo Atlas into a giant permanent document. Keep it concise and evidence-backed.

---

# Phase 4.5: Analysis Report (L0 tasks only)

For read-only exploration and analysis tasks, produce an Analysis Report after completing Phase 4, then skip to Phase 14 (Context GC).

The Analysis Report replaces the Final Report for L0 work. It is the deliverable: findings, evidence, and follow-ups — no implementation plan, no rollback section.

Produce this artifact:

```md
# Analysis Report

## What works well

## Key findings

| Finding | Severity | Evidence | Location |
|---|---|---|---|

## Improvement candidates

## Verification performed

## Follow-ups
```

Severity levels: `high` (correctness, security, trust), `medium` (maintainability, DX), `low` (style, optional).

Tie every finding to a file path, line number, command output, or documented behavior. Label unverified claims as assumptions.

See `references/output-contracts.md` for the full contract and `templates/analysis-report.md` for a filled-in example.

---

# Phase 5: Component Brief

Find the component or feature area relevant to the task.

Use layered search:

```text
1. Search exact user terms.
2. Search related domain terms.
3. Search error strings or log messages.
4. Search public interfaces.
5. Search tests and fixtures.
6. Search callers/callees.
7. Search config/schema references.
```

Do not assume ownership from filenames alone. Verify through call paths, tests, interfaces, and runtime/config references.

Required artifact:

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

---

# Phase 6: Contract Graph and interaction map

Trace the focused area as a contract graph, not just a list of files.

Preferred shape:

```text
source → adapter → contract → domain operation → side effect → observable output → verification
```

For every important boundary, capture:

- producer
- consumer
- contract
- data shape
- ownership
- error behavior
- compatibility risk
- observability/logging/metrics
- existing coverage
- missing coverage
- failure mode

Required artifact:

```md
# Contract Graph

| Edge | Producer | Contract / Data Shape | Consumer | Side Effect | Failure Mode | Coverage | Risk |
|---|---|---|---|---|---|---|---|
```

Use this edge model:

```text
producer → contract → consumer → failure mode → test coverage
```

Important interaction points to check:

- public interfaces
- function/class/module boundaries
- API routes or RPC handlers
- CLI commands
- config files
- data models and schemas
- database or persistence access
- event/message queues
- external service calls
- file system reads/writes
- feature flags
- permission/auth checks
- error handling paths
- logging/metrics/tracing
- tests and fixtures
- generated code or codegen inputs

---

# Phase 7: Evidence Ledger

Every major claim must be connected to evidence.

Evidence may be:

- source file path
- symbol/function/class reference
- test result
- command output
- log excerpt
- API contract
- documented behavior
- reproducible observation

Required artifact:

```md
# Evidence Ledger

| Claim | Evidence | Confidence | Impact |
|---|---|---:|---|
```

Classify unsupported claims as assumptions. Do not smuggle guesses into the plan.

The Evidence Skeptic must classify major claims as:

1. Proven
2. Plausible but unproven
3. Contradicted
4. Irrelevant
5. Risky assumption

---

# Phase 8: Deliberation protocol

Before implementation, every selected teammate answers:

1. What do you believe is true?
2. What evidence supports it?
3. What could make you wrong?
4. What is the smallest safe next action?
5. What should not be changed?

The Lead Engineer must synthesize one plan. Do not concatenate opinions. Do not average contradictory conclusions. Resolve contradictions with evidence or targeted follow-up checks.

---

# Phase 9: Adaptive spawning

Spawn additional specialists only when evidence justifies them.

Spawn when:

- relevant code appears outside the original scope
- skeptic identifies an unreviewed risk area
- proposed implementation touches security, architecture, performance, migration, release, or DX behavior
- tests fail in a way that suggests another domain
- evidence contradicts the initial classification

Examples:

- Auth middleware touched → Security Analyst
- Public interface changed → System Design Architect
- Polling, caching, locking, batching, buffering, memory ownership touched → Optimization Engineer
- Legacy/config/schema conversion touched → Migration Analyst
- Runtime/prod behavior changed → Release / Rollback Engineer
- CLI/docs/error behavior changed → DX / Documentation Reviewer

---

# Phase 10: Advisor gate

Use Advisor Consultant as a decision gate, not as another default teammate.

Invoke Advisor Consultant before implementation when any of these are true:

- autonomy is L4 or L5 and the plan changes behavior across components
- root cause remains unclear after investigation
- source evidence and runtime evidence conflict
- the decision affects security, migration, compatibility, release, production behavior, or rollback
- completion confidence depends on assumptions rather than direct evidence
- Evidence Skeptic returns `Blocked`, `No-Go`, or unresolved contradictions

Do not invoke Advisor Consultant for `low-risk-local` work or routine L2/L3 work where evidence and verification path are clear.

Advisor brief contract:

```md
## Decision Needed
## Current Plan
## Relevant Evidence
## Constraints
## Alternatives Considered
## Uncertainty
## Requested Output
```

Advisor output contract:

```md
## Recommendation
## Confidence
## Assumptions Challenged
## Risks Found
## Missing Evidence
## Better Option
## Go / No-Go
```

Lead follow-through:

- Treat the advisor response as evidence to reconcile, not automatic authority.
- If the advisor returns `No-Go`, do not implement until the missing evidence or safer option is addressed.
- If advisor confidence is below `Medium`, pause for user approval before sensitive side effects.
- Record an Advisor Decision Receipt in the final report whenever advisor runs.

Human approval triggers:

- live DUT or production-like system mutation
- destructive commands or irreversible data/file changes
- broad generated-file rewrites
- production-sensitive workaround or release/rollback decision
- Advisor Consultant returns `No-Go`
- Advisor Consultant confidence is below `Medium`

Advisor Decision Receipt:

```md
## Advisor Decision Receipt
- Decision:
- Evidence used:
- Advisor recommendation:
- Lead decision:
- Why accepted / rejected:
- Follow-up checks:
```

---

# Phase 11: Implementation gate

Do not edit files until the final plan exists.

Before editing, verify:

- problem scope is clear
- Repo Atlas exists or is unnecessary due to tiny scope
- Component Brief exists
- Contract Graph exists for L3+ work
- Evidence Ledger contains the key claims
- affected files are identified
- root-cause or design evidence exists
- architecture/security/performance/migration/release constraints are known when relevant
- Evidence Skeptic reviewed the plan for non-trivial work
- Advisor Consultant reviewed the plan when the advisor gate requires it
- tests or verification commands are defined
- rollback path is understood
- same-file edit conflicts are avoided

If any item fails, continue investigation or spawn the missing specialist.

Output:

```md
## Implementation gate

- Gate status: Pass / Blocked
- Missing evidence:
- Files allowed to change:
- Files inspected but not changing:
- Verification required:
- Rollback path:
```

---

# Phase 12: Implementation rules

During implementation:

- Make the smallest safe change.
- Preserve existing style and conventions.
- Prefer repo conventions over generic best practices.
- Avoid unrelated refactors.
- Avoid broad rewrites.
- Keep changes close to the target behavior.
- Preserve public contracts unless explicitly required.
- Add comments only for non-obvious reasoning.
- Update tests close to the changed behavior.
- For test-first work, use vertical tracer-bullet cycles: one behavior test, minimal implementation, repeat.
- Tests should verify behavior through public interfaces, not private implementation details.
- See `references/tdd-discipline.md` for the full tracer-bullet and test-surface rules.
- Track every changed file.
- Avoid concurrent edits to the same file.
- If generated code is involved, determine whether to modify source definitions, generated outputs, or both according to repo convention.

Prefer mechanically enforced rules over prose instructions:

1. Test
2. Linter
3. Static check
4. Schema validation
5. Type-level constraint
6. CI check
7. Scripted verifier

---

# Phase 13: Verification and failure attribution

Run the narrowest useful verification first, then expand as risk requires.

For bug investigations, regressions, flaky behavior, crashes, or performance regressions, build a fast deterministic feedback loop before fixing. Use `references/diagnosis-loop.md` to reproduce the exact symptom, rank falsifiable hypotheses, instrument one prediction at a time, and convert the minimized repro into a regression signal when a correct seam exists.

For new behavior or regression coverage, use `references/tdd-discipline.md`: avoid horizontal "all tests then all implementation" slicing, prefer one vertical tracer bullet at a time, and reject tests that do not exercise the real public contract.

Preferred order:

1. Fast static checks
2. Targeted unit tests
3. Regression tests near changed behavior
4. Integration or system tests
5. Security, performance, migration, or manual checks when relevant
6. Broader suite only when risk justifies it

For every command, capture:

- command
- result
- important output
- whether failures are related
- next action

If verification fails, do not blindly patch. Classify the failure first:

- wrong implementation
- wrong test expectation
- missing dependency
- environment issue
- flaky test
- incomplete repo understanding
- hidden contract violation
- generated-code mismatch
- stale documentation
- permission/tooling issue

Loop:

```text
failure → attribution → new evidence → revised plan → focused patch → rerun
```

Required artifact:

```md
# Verification Report

| Command | Result | Relevant Output | Related? | Next Action |
|---|---|---|---|---|

## Failure Attribution
## Coverage Gaps
## Unverified Risks
```

If tests cannot be run, explain why and provide exact commands.

---

# Phase 14: Context garbage collection

At the end of a task, decide whether durable repo knowledge should be updated.

Update durable context only when the task reveals reusable information, such as:

- new architecture rule
- new build/test command
- new generated-code convention
- new failure mode
- new component ownership
- new integration contract
- new verification command
- resolved or sharpened domain term that belongs in `CONTEXT.md`
- hard-to-reverse architectural decision that deserves an ADR

Do not update durable context with one-off task details.

If durable context appears stale, report it separately instead of silently trusting it.

Create durable context lazily. If no `CONTEXT.md` exists, create or propose one only when a reusable domain term is resolved. Offer an ADR only when all three are true:

1. The decision is hard to reverse.
2. The decision will be surprising without context.
3. The decision reflects a real trade-off among alternatives.

See `references/domain-context.md` for the glossary and ADR formats.

Output:

```md
## Context garbage collection

- Durable knowledge to update:
- Stale context found:
- One-off details not retained:
```

---

# Final report (L2+ tasks)

For L0 analysis tasks, use the Analysis Report from Phase 4.5 instead of this template.

Return:

```md
## Result

## Agent routing

## Repo mental model

## Focused component

## Contract graph

## Evidence

## Advisor Decision Receipt

## Changes

## Verification

## Risks

## Rollback

## Context updates

## Follow-ups
```

Keep the final report concise. Include concrete file paths, commands, tests, and remaining risks.

For architecture reviews, migration impact maps, performance investigations, or cross-component contract analysis, consider a self-contained temporary HTML visual report when diagrams or side-by-side layout would make the evidence easier to inspect. See `references/visual-review-reports.md`.

If the user asks for terse or compressed output, reduce filler and keep exact technical terms, commands, paths, errors, and risks intact.

---

# Failure modes to actively avoid

- Editing before understanding the repo
- Fixed-team spawning regardless of task
- Many agents agreeing without independent evidence
- Lead averaging opinions instead of resolving contradictions
- Evidence Skeptic becoming decorative
- Searching only exact user terms
- Ignoring repo instructions
- Reading too much irrelevant context
- Modifying unrelated files
- Creating new patterns when existing ones exist
- Adding tests that do not exercise the real path
- Fixing symptoms instead of interaction boundaries
- Missing generated-code conventions
- Ignoring compatibility, rollout, or migration impact
- Assuming a component is unused without checking references
- Trusting stale docs over code
- Same-file edit conflicts
- Test theater
- Security theater
- Premature optimization
- Reporting success without verification
- Forgetting to garbage-collect context
- Producing an implementation Final Report for a read-only analysis task
- Skipping the `## Intake` block — it is always required as the routing receipt

---

# Supporting references

Use these only when needed:

- `references/agent-selection-matrix.md` for detailed routing rules.
- `references/alignment-audit.md` for resolving ambiguous user intent before routing or implementation.
- `references/role-definitions.md` for role contracts.
- `references/output-contracts.md` for report templates.
- `references/routing-examples.md` for examples.
- `references/repo-intelligence-schema.md` for repo atlas and component brief schemas.
- `references/domain-context.md` for optional `CONTEXT.md` glossary and ADR usage.
- `references/contract-graph-schema.md` for interaction and contract mapping.
- `references/evidence-ledger-schema.md` for evidence discipline.
- `references/autonomy-ladder.md` for implementation gates.
- `references/diagnosis-loop.md` for feedback-loop-first bug and performance diagnosis.
- `references/tdd-discipline.md` for vertical-slice behavior testing and anti-test-theater rules.
- `references/failure-attribution.md` for verifier-loop triage.
- `references/context-garbage-collection.md` for durable-context updates.
- `references/visual-review-reports.md` for optional temporary HTML review artifacts.
- `templates/analysis-report.md` for the Analysis Report artifact template for L0 tasks.

# Supporting scripts

Use these only when useful and available:

- `scripts/repo_snapshot.sh` to create a shallow repo map.
- `scripts/symbol_index.sh` to build a lightweight symbol/import index.
- `scripts/test_discovery.sh` to find nearby tests and likely test commands.
- `scripts/changed_surface.sh` to inspect changed files, public surfaces, and risky deltas.
- `scripts/stale_context_check.sh` to identify context files that may need refresh.

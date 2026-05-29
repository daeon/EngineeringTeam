# EngineeringTeam Workflow

EngineeringTeam is a staged workflow. Each stage narrows uncertainty before the agent is allowed to change code.

## 🗺️ Dataflow

```mermaid
flowchart TB
    request[Request] --> intake[Intake_And_Risk]
    intake --> alignment[Alignment_Gate]
    alignment --> routing[Role_Routing]
    routing --> repoAtlas[Repo_Atlas]
    repoAtlas --> componentBrief[Component_Brief]
    componentBrief --> contractGraph[Contract_Graph]
    contractGraph --> evidenceLedger[Evidence_Ledger]
    evidenceLedger --> advisorGate{Advisor_Gate_Needed}
    advisorGate -->|Yes| advisor[Advisor_Decision]
    advisorGate -->|No| implementationGate[Implementation_Gate]
    advisor --> implementationGate
    implementationGate --> patch[Patch]
    patch --> verification[Verification]
    verification --> handoff[Final_Handoff]
```


## 💡 Why The Workflow Exists

The workflow is not ceremony for its own sake. It counters the most expensive failure mode in agent-assisted engineering: acting confidently with incomplete repository context. Each stage retires a different kind of uncertainty:

- Intake retires ambiguity about the requested outcome.
- Repo Atlas retires uncertainty about project shape and local rules.
- Component Brief retires uncertainty about ownership and call path.
- Contract Graph retires uncertainty about consumers and compatibility.
- Evidence Ledger retires unsupported claims.
- Implementation Gate retires accidental broad edits.
- Verification retires unproven success.

For small, obvious edits, EngineeringTeam can take a fast path. For risky changes, the workflow creates a reviewable trail from user request to validated patch.

## 1️⃣ Stage 1: Intake And Risk

The agent restates the task in engineering terms and classifies:

- Requested outcome.
- Known files, symptoms, or components.
- Risk level.
- Unknowns that must be resolved from the repo.
- Expected deliverable.

The risk classification decides whether the task needs a full specialist route or a lightweight lead-only pass.

## 1.5️⃣ Stage 1.5: Alignment Gate

For ambiguous scope, behavior, terminology, acceptance criteria, or L3+ risk, the agent resolves user intent before routing too deeply:

- Ask one question at a time.
- Include a recommended answer.
- Inspect the repository instead of asking when code, tests, or docs can answer.
- Stop when acceptance criteria, non-goals, and verification signals are clear.

## 2️⃣ Stage 2: Role Routing

EngineeringTeam does not spawn a fixed team by default. It scores candidate roles and uses only the smallest set that covers distinct risks.

Examples:

- Unknown repo impact: Codebase Investigator.
- Behavior change: Test Verification Engineer.
- Security boundary: Security Analyst.
- Public API or module boundary: System Design Architect.
- Migration or compatibility: Migration Analyst.
- Production behavior: Release Rollback Engineer.
- Unclear evidence: Evidence Skeptic or Advisor Consultant.

When a task is broad, noisy, or specialist-heavy, the Lead Engineer delegates bounded work to subagents using `templates/subagent-brief.md`. Each subagent returns a compact context capsule. The Lead Engineer uses capsules as evidence and owns the final decision.

## 3️⃣ Stage 3: Repo Atlas

The repo atlas is a shallow map of the system:

- Main languages and frameworks.
- Runtime and build model.
- Entry points.
- Test surfaces.
- Domain context and relevant ADRs, when present.
- Generated-code rules.
- Config and schema sources.
- External integrations.
- Repo-specific instructions.

The goal is orientation, not exhaustive documentation.

Domain docs are a soft dependency. If a `CONTEXT.md`, `CONTEXT-MAP.md`, or ADRs exist, EngineeringTeam uses that vocabulary and respects durable decisions. If they are absent, the workflow continues with code-first evidence.

## 4️⃣ Stage 4: Component Brief

The component brief narrows the map to the relevant behavior:

- Owning component.
- Important files and symbols.
- Main call path.
- Related tests.
- Similar existing patterns.
- Inputs, outputs, and side effects.
- Open questions.

This is the minimum artifact before local edits.

## 5️⃣ Stage 5: Contract Graph

Behavior changes require contract awareness. EngineeringTeam traces producer-to-consumer edges:

```mermaid
flowchart LR
    source[Source] --> adapter[Adapter]
    adapter --> contract[Contract]
    contract --> domain[Domain operation]
    domain --> sideEffect[Side effect]
    sideEffect --> output[Observable output]
    output --> verification[Verification]
```

For each edge, the agent records data shape, ownership, error behavior, compatibility risk, coverage, and failure mode.

## 6️⃣ Stage 6: Evidence Ledger

Every major claim must point to evidence:

- Source path.
- Symbol reference.
- Test result.
- Log excerpt.
- API contract.
- Runtime observation.
- Documented behavior.

Unsupported claims remain assumptions.

## 7️⃣ Stage 7: Implementation Gate

The agent may edit only after the gate passes:

- Scope is clear.
- Files allowed to change are named.
- Evidence supports the diagnosis or design.
- Contract edges are known for behavior changes.
- Tests or verification commands are defined.
- Rollback path is understood for risky work.

## 8️⃣ Stage 8: Verification And Handoff

Verification starts narrow, then expands only when risk justifies it:

1. Fast static checks.
2. Targeted unit tests.
3. Regression tests.
4. Integration or system checks.
5. Security, performance, migration, or manual checks when relevant.

The final handoff reports what changed, what was verified, what remains risky, and what reusable repo knowledge should be preserved.

```mermaid
flowchart TD
    check[Run focused check] --> result{Result}
    result -->|Pass| expand[Expand only if risk justifies it]
    result -->|Fail| classify[Classify failure]
    classify --> impl[Wrong implementation]
    classify --> expectation[Wrong expectation]
    classify --> env[Environment/tooling issue]
    classify --> understanding[Incomplete repo understanding]
    impl --> patch[Patch intentionally]
    expectation --> adjust[Test or acceptance update]
    env --> report[Report limitation]
    understanding --> map[Return to mapping]
    patch --> check
    adjust --> check
    map --> check
```

For bug investigations, EngineeringTeam builds a deterministic feedback loop before fixing. For test-first work, it uses vertical tracer-bullet cycles: one public-interface behavior test, minimal implementation, then the next behavior.

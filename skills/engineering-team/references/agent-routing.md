# Agent Routing

The main session is the Lead Engineer. It owns user intent, route selection, risk classification, synthesis, edit authorization, and the final report. Never spawn a second lead.

## Mandatory subagent routing

For every non-trivial L2+ EngineeringTeam task on a harness with subagent support, delegate the selected specialist questions before broad read-only claims or implementation. L0-L1 work and the explicit typo/formatting-only L2 fast-path exception may remain main-session-only.

Fallback is only for harnesses without subagent support, missing specialist definitions, tool failures, or safety constraints that prevent spawning. Record the reason and apply the same evidence and gate checks in the main session.

## Select by unanswered question

Start with at most three specialists. Each must own one bounded question whose answer can change the decision.

| Signal | Specialist | Initial question |
|---|---|---|
| Unknown ownership, call path, tests, or generated-code source | Codebase Investigator | Where is the behavior owned and how does execution reach it? |
| Behavior change, regression, flaky test, or weak proof | Test Verification Engineer | What check exercises the affected contract and how could it mislead us? |
| Unsupported or conflicting claim; L3+ implementation | Evidence Skeptic | Which key claim is unproven or contradicted? |
| Public API, module boundary, broad refactor, long-term shape | System Design Architect | Which boundary or dependency direction is at risk? |
| Auth, permissions, secrets, user input, shell/filesystem/network | Security Analyst | What trust boundary or abuse path changes? |
| Latency, throughput, memory, IO, locks, caching, benchmark validity | Optimization Engineer | What measurement identifies the actual bottleneck? |
| Schema, config, version, API, import/export, legacy behavior | Migration Analyst | Which source/target semantics can diverge? |
| Production rollout, observability, feature flags, rollback | Release Rollback Engineer | How can this ship, fail partially, and be reversed safely? |
| CLI, docs, examples, onboarding, error behavior | DX Documentation Reviewer | What user/developer contract needs to remain understandable? |
| Consequential ambiguity or whole-plan Go/No-Go | Advisor Consultant | Is the proposed decision wise, proportionate, and reversible? |

Implementation Engineer is a post-gate writer, not an investigation default. Spawn it only after the Implementation Gate assigns explicit source files. Test Verification Engineer and DX Documentation Reviewer may write only their assigned test or documentation lanes after the gate.

## Adaptive expansion

Add another specialist only when a returned capsule exposes a distinct trigger. Do not spawn a fixed committee, duplicate a question, or fan out merely because a role is available.

- L2 local work usually needs Investigator **or** Verifier.
- L3 behavior/root-cause work adds Evidence Skeptic.
- Domain triggers add Security, Optimization, Migration, Release, Architect, or DX.
- L4-L5 work invokes Advisor Consultant only when `references/advisor-gate.md` requires independent decision review.

Advisor output is evidence, not authority. Resolve contradictions with a targeted probe, additional source evidence, or a conditional stop.

## Context budget policy

Use the smallest useful budget defined in `references/subagent-context-policy.md`:

| Budget | Default use |
|---|---|
| `brief-only` | Advisor, skeptic, narrow review |
| `component-context` | Focused investigation |
| `artifact-context` | Multi-step review or verification |
| `full-context` | Rare case where a compact brief is unsafe; state why |

Default Advisor Consultant to `brief-only`. Give each specialist only the paths, artifacts, evidence, constraints, and question needed for its mission.

## Proactive subagent triggers

Delegate when ownership is unknown, more than five files may be relevant, terms span components, generated code may be involved, a public contract may change, output/logs may be long, independent areas can run in parallel, or a distinct risk lens is required.

Keep work in the main session when the task is trivial, user interaction must remain continuous, the edit depends on dense shared context, or same-file conflicts would dominate. Non-trivial L2+ work still requires a recorded fallback reason when delegation cannot run.

## Delegation envelope

Use `templates/subagent-brief.md`. Include role, mission, context budget, allowed tools, inputs, output limit, required artifact, scope-expansion trigger, and explicit prohibited actions.

Before implementation, every selected specialist answers:

1. What appears true?
2. What evidence supports it?
3. What could falsify it?
4. What is the smallest safe next action?
5. What must not change?

## Context capsule rule

Require `templates/context-capsule.md`. Specialists return findings, evidence, contradictions, confidence, risks, scope-expansion triggers, and one recommended next action—not transcripts, raw dumps, or complete logs. The main session reconciles capsules through the Evidence Ledger and owns the final decision.

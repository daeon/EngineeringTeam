# Routing Evals

Use these fixtures to check whether EngineeringTeam routes advisors and specialists proportionately.

These fixtures are mirrored by package contract tests and remain useful for fresh-context routing checks.

Expected outputs are routing expectations, not implementation answers.

| Case | Prompt shape | Expected mode / risk | Expected routing |
|---|---|---|---|
| Trivial typo | "Fix this spelling mistake in README." | Implementation fast path / `low-risk-local` | Main-session Lead only; no subagent or Advisor Consultant |
| Local behavior change | "Change this parser branch and add the nearby regression test." | Implementation / `behavior-change` | Main-session Lead + Verifier; Skeptic if assumptions remain; Implementer only after gate |
| Unclear root cause | "The service sometimes drops responses; logs and tests disagree." | Debugging route / `uncertain-root-cause` or `conflicting-evidence` | Investigator + Skeptic; Advisor before implementation when uncertainty remains |
| Auth boundary | "Update authorization around this endpoint." | `security-sensitive` | Security + Skeptic; Advisor if L5, broad, or uncertain |
| Migration config | "Translate legacy config into the new schema without breaking upgrades." | `migration/compatibility` | Migration + Release + Skeptic; Advisor for irreversible or ambiguous behavior |
| Production workaround | "Patch this live production failure and preserve rollback." | `release/production` | Release + Advisor + human approval before side effects |
| Broad refactor | "Move this behavior across modules and preserve public contracts." | `cross-component` | Investigator + Architect + Skeptic; Advisor if consequences are broad or assumptions remain |
| Docs-only UX | "Clarify CLI error docs after a verified local change." | `low-risk-local` or `behavior-change` | DX as needed; no Advisor Consultant |
| Codebase audit / analysis | "Analyze this repo and provide feedback." | Codebase-analysis route / L2-L4 by breadth | Main-session Lead + Investigator; Architect or Skeptic only for broad design claims |
| Log incident | "Analyze these service logs and reconstruct the outage." | Log-analysis route / L3+ | Investigator or Release + Skeptic for causal claims; redact sensitive data |
| Performance regression | "Explain why endpoint latency doubled without changing code." | Performance route / L3+ | Optimization + Verifier + Skeptic; measurement-first and read-only |
| Engineering handoff | "Prepare this branch for another agent to continue." | Handoff mode | Main-session Lead; write only the continuation artifact |

Advisor anti-patterns:

- Do not invoke Advisor Consultant for obvious one-line edits.
- Do not paste full conversation context into an advisor brief by default.
- Do not treat advisor output as authority without reconciling it against local evidence.
- Do not use advisor as a substitute for Evidence Skeptic; skeptic proves claims, advisor judges the decision.

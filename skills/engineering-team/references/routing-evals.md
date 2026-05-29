# Routing Evals

Use these fixtures to check whether EngineeringTeam routes advisors and specialists proportionately.

Expected outputs are routing expectations, not implementation answers.

| Case | Prompt shape | Expected risk mode | Expected routing |
|---|---|---|---|
| Trivial typo | "Fix this spelling mistake in README." | `low-risk-local` | Lead only; no Advisor Consultant |
| Local behavior change | "Change this parser branch and add the nearby regression test." | `behavior-change` | Lead + Verifier; Skeptic if assumptions remain; no Advisor by default |
| Unclear root cause | "The service sometimes drops responses; logs and tests disagree." | `uncertain-root-cause` or `conflicting-evidence` | Investigator + Skeptic + Advisor before implementation |
| Auth boundary | "Update authorization around this endpoint." | `security-sensitive` | Security + Skeptic; Advisor if L5, broad, or uncertain |
| Migration config | "Translate legacy config into the new schema without breaking upgrades." | `migration/compatibility` | Migration + Release + Skeptic; Advisor for irreversible or ambiguous behavior |
| Production workaround | "Patch this live production failure and preserve rollback." | `release/production` | Release + Advisor + human approval before side effects |
| Broad refactor | "Move this behavior across modules and preserve public contracts." | `cross-component` | Investigator + Architect + Skeptic; Advisor if consequences are broad or assumptions remain |
| Docs-only UX | "Clarify CLI error docs after a verified local change." | `low-risk-local` or `behavior-change` | DX as needed; no Advisor Consultant |
| Codebase audit / analysis | "Analyze this repo and provide feedback." | `low-risk-local` | L0 fast path: Lead only; Repo Atlas → Analysis Report → Context GC; no specialists, no advisor |

Advisor anti-patterns:

- Do not invoke Advisor Consultant for obvious one-line edits.
- Do not paste full conversation context into an advisor brief by default.
- Do not treat advisor output as authority without reconciling it against local evidence.
- Do not use advisor as a substitute for Evidence Skeptic; skeptic proves claims, advisor judges the decision.

# Agent Selection Matrix

Score 0-3:

- 0 = not useful
- 1 = possibly useful
- 2 = useful
- 3 = essential

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
| migration/compatibility | 3 | 2 | 2 | 2 | 3 | 2-3 if irreversible/ambiguous | 1-2 | 1-2 if semantics/security | 1 if scale | 3 | 1-2 | 0 |
| production rollout | 3 | 1-2 | 1-2 | 2 | 2 | 3 | 1 | 1-2 | 1-2 | 1-2 | 3 | 1 |
| docs/DX/CLI UX | 3 | 1 | 1-2 | 1-2 | 1-2 | 0 | 1 | 0-1 | 0 | 0 | 0-1 | 3 |

Spawn the smallest team that covers all score-3 areas and distinct score-2 risks.

Advisor is gate-only. Do not spawn it for low-risk local work or routine L2/L3 tasks with clear evidence and verification.

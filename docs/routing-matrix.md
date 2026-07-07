# Routing Matrix

EngineeringTeam remains the primary router. Unknowns-first is an optional pre-intake layer for tasks where ambiguity itself is the first risk.

| Request shape | Default route | Unknowns-first? | Why |
|---|---|---|---|
| Typo, formatting, or obvious one-file edit | L0-L1 fast path | No | The next safe action is already clear. |
| Local implementation with known owner and tests | `intake-risk.md` -> Component Brief -> Implementation Gate | Usually no | Normal EngineeringTeam artifacts are enough. |
| Ambiguous behavior or acceptance criteria | `unknowns-first/router.md` -> `alignment-audit.md` -> intake | Yes, one focused phase | Hidden assumptions can change the work. |
| Unfamiliar component or missing call path | Blindspot Pass -> Repo Atlas / Component Brief | Yes | Cheap probes can find ownership before routing. |
| Architecture or public-contract decision | Architecture Interview -> Alignment Audit / Impact Map | Yes | One unresolved decision can invalidate implementation. |
| Security, migration, release, or production-sensitive work | Risk-First Plan -> intake/advisor gates | Yes | Defaults, alternatives, rollback, and invalidators must be visible. |
| Debugging with uncertain root cause | Blindspot Pass or Risk-First Plan -> debugging forensics | Often | Avoid patching symptoms before evidence converges. |
| Read-only repo map or local explanation | Analysis routing or fast path | Only if broad/ambiguous | Read-only changes edit posture, not rigor. |

## Routing Rule

Use the smallest phase that reduces the current uncertainty. Unknowns-first outputs map into the normal artifacts: Intake, Alignment Audit, Repo Atlas, Component Brief, Contract Graph, Evidence Ledger, Implementation Gate, Run Ledger, Verification Report, and Final Report.

Do not create a second artifact stack or a second top-level router. The lead engineer still owns final routing.

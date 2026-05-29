# Autonomy Ladder

Use this to decide how much evidence and review are required before editing.

| Level | Meaning | Allowed | Required before edit |
|---|---|---|---|
| L0 | Read-only exploration | Search/read/summarize | None |
| L1 | Plan only | Investigation and plan | Repo Atlas |
| L2 | Local patch, no behavior change | Small local edit | Component Brief + nearby pattern/test |
| L3 | Behavior change | Patch + tests | Contract Graph + regression test or verification path |
| L4 | Multi-component change | Coordinated patch | Impact Map + specialist review |
| L5 | Architecture, migration, security, release, or production-sensitive change | Staged patch/plan | Explicit constraints + rollout/rollback plan + skeptic gate |

Escalate level when a change touches public contracts, auth, permissions, persistence, external services, generated code, production rollout, or legacy compatibility.

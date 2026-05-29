# Autonomy Ladder

Use this to decide how much evidence and review are required before editing.

| Level | Meaning | Allowed | Required before edit |
|---|---|---|---|
| L0 | Read-only exploration or analysis | Search/read/summarize | None (no edits); deliver an Analysis Report |
| L1 | Plan only | Investigation and plan | Repo Atlas |
| L2 | Local patch, no behavior change | Small local edit | Component Brief + nearby pattern/test |
| L3 | Behavior change | Patch + tests | Contract Graph + regression test or verification path |
| L4 | Multi-component change | Coordinated patch | Impact Map + specialist review |
| L5 | Architecture, migration, security, release, or production-sensitive change | Staged patch/plan | Explicit constraints + rollout/rollback plan + skeptic gate |

At L4+ the "Impact Map + specialist review" requirement uses `references/impact-map.md` to scope the blast radius before editing.

Escalate level when a change touches public contracts, auth, permissions, persistence, external services, generated code, production rollout, or legacy compatibility.

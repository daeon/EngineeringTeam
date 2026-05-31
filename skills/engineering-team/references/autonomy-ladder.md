# Autonomy Ladder

Use this to decide how much evidence and review are required before editing or before making broad read-only claims.

Mode and autonomy are separate:

- Read-only mode means no file edits.
- Implementation mode means edits may be allowed after the right gate.
- L0-L5 describes depth, uncertainty, and risk. Do not use L0 just because the request is read-only.

| Level | Meaning | Allowed | Required before edit or broad claim |
|---|---|---|---|
| L0 | Trivial read-only explanation or obvious local inspection with no cross-file claims | Search/read/summarize | None; deliver a lightweight Analysis Report |
| L1 | Plan only or bounded orientation without repo-wide claims | Investigation and plan | Repo Atlas |
| L2 | Local patch or bounded component analysis with no behavior/contract change | Small local edit or component analysis | Component Brief + nearby pattern/test |
| L3 | Behavior, contract, root-cause, debugging, performance, or verification work | Patch + tests, or read-only forensics | Contract Graph + regression test or verification path |
| L4 | Multi-component implementation or broad read-only architecture/design analysis | Coordinated patch or cross-component analysis | Impact Map + specialist review |
| L5 | Architecture, migration, security, release, production-sensitive, or high-uncertainty work | Staged patch/plan or high-rigor analysis | Explicit constraints + rollout/rollback plan + skeptic gate |

At L4+ the "Impact Map + specialist review" requirement uses `references/impact-map.md` to scope the blast radius before editing or before making broad design claims.

Escalate level when a task touches or investigates public contracts, permissions, persistence, external services, generated code, production rollout, legacy compatibility, conflicting evidence, or uncertain root cause.

## Read-only examples

| Request | Default level |
|---|---|
| Explain this known file or obvious local behavior | L0 |
| Produce an implementation plan without edits | L1 |
| Analyze this component or generated-code path | L2 |
| Find root cause, analyze logs, or investigate performance | L3 |
| Analyze repo architecture or multi-component PR behavior | L4 |
| Analyze security, migration, release, production, or high-uncertainty risk | L5 |

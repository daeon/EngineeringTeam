# Intake and Risk Classification

**Produce the `## Intake` artifact before deep routing or implementation.** Minimal repo discovery is allowed when needed to classify scope accurately, but do not start broad investigation, specialist routing, or edits before intake is recorded.

Classify every task before routing or implementing.

## Canonical gate ownership

- `references/intake-risk.md` owns task type, mode, autonomy level, and risk mode.
- `references/evidence-ledger.md` owns evidence quality and claim classification.
- `references/advisor-gate.md` owns independent high-risk decision review.
- `references/implementation-gate.md` owns edit authorization and file-change boundaries.

## Step 1: Restate in engineering terms

Capture:
- requested outcome
- known files, symptoms, or components
- constraints from the user
- risk level
- unknowns that must be resolved from the repo
- expected deliverable

## Step 2: Classify task type

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

## Step 3: Select mode, then assign autonomy level

Mode and autonomy are separate decisions:

- **Mode** answers whether the task is read-only or implementation.
- **Autonomy level** answers how much evidence, routing, and review are required.

Do not classify a task as L0 just because it is read-only. Read-only investigations can still be L2, L3, L4, or L5 when they require component mapping, root-cause analysis, performance reasoning, security review, migration analysis, release judgment, or cross-component design work.

See `references/autonomy-ladder.md` for the single-owner L0-L5 definition.

| Level | Meaning | Required before edit |
|---|---|---|
| L0 | Trivial read-only explanation or obvious local inspection with no cross-file claims | Lightweight Repo Atlas + Analysis Report |
| L1 | Plan only or bounded orientation, no repo-wide claims | Repo Atlas |
| L2 | Local patch or bounded component analysis, no behavior/contract change | Component Brief + nearby pattern/test |
| L3 | Behavior, contract, root-cause, debugging, performance, or verification analysis | Contract Graph + regression test or verification path |
| L4 | Multi-component implementation or read-only architecture/design analysis | Impact Map + specialist review |
| L5 | Architecture, migration, security, release, production-sensitive, or high-uncertainty work | Explicit constraints + rollout/rollback plan + skeptic gate |

Escalate level when a task touches or investigates public contracts, permissions, persistence, external services, generated code, production rollout, legacy compatibility, conflicting evidence, or uncertain root cause. At L4+, build an Impact Map (`references/impact-map.md`) before editing or before making broad design claims.

## Step 4: Choose risk mode

| Risk mode | Meaning | Default routing |
|---|---|---|
| `low-risk-local` | Obvious local edit, local explanation, or trivial one-file inspection | Lead only; no advisor |
| `behavior-change` | Local behavior, tests, or contracts may change | Verifier + skeptic as needed; use diagnosis loop for bug-driven changes |
| `cross-component` | Multiple modules, packages, services, or owners | Investigator + architect + skeptic |
| `security-sensitive` | Trust boundary, inputs, sensitive data, filesystem, network, or dependency risk | Security + skeptic; advisor for L5 or uncertainty |
| `migration/compatibility` | Legacy behavior, config/schema/API translation, upgrade or import/export risk | Migration + release + skeptic; advisor for irreversible or ambiguous choices |
| `release/production` | Runtime, rollout, rollback, observability, live system, or production behavior | Release + advisor; human approval before sensitive side effects |
| `uncertain-root-cause` | Investigation has not converged on evidence-backed root cause | Investigator + skeptic + advisor before implementation; feedback loop before hypotheses |
| `conflicting-evidence` | Source, tests, docs, logs, or runtime observations disagree | Investigator + skeptic + advisor before implementation |

## Read-only depth guide

Read-only mode changes the edit posture, not the required rigor.

| Read-only request | Default level |
|---|---|
| Summarize or explain a known file / obvious local fact | L0 |
| Produce a plan or bounded orientation without repo-wide claims | L1 |
| Analyze one component, workflow, generated-code path, or local contract | L2 |
| Investigate a bug, root cause, performance issue, log sequence, or behavioral contract | L3 |
| Analyze architecture, broad design, multi-component impact, PR/diff behavior across areas | L4 |
| Analyze security, migration, release, production, irreversible, or high-uncertainty risk | L5 |

## L0 fast path

When autonomy level is L0, proceed to a lightweight Repo Atlas, then produce an Analysis Report (`templates/analysis-report.md`). Skip agent routing, contract graph, evidence ledger, advisor gate, implementation gate, and verification loop. Context GC still applies.

L0 tasks are limited to simple summaries, local explanations, or obvious one-file inspections with no planned change and no cross-file, behavior, contract, performance, security, migration, release, or production claims.

Do not classify these as L0 by default:

- codebase audits
- architecture surveys
- root-cause investigations
- debugging forensics
- log forensics
- performance investigations
- security reviews
- migration or compatibility analysis
- release or production analysis
- PR or diff reviews involving behavior, API, tests, generated code, or multiple files

For descriptive "understand / map how this repo works" requests, route through `references/analysis-routing.md` to the `codebase-analysis` skill, then assign L1-L4 depth based on breadth and claims. Use a Codebase Analysis Report (`templates/codebase-analysis-report.md`) instead of a generic Analysis Report when the request is more than trivial local explanation.

## Artifact depth by autonomy level

Produce artifacts at the depth the level requires. Do not skip artifacts entirely; produce a minimal valid form when depth is low.

| Level | Repo Atlas | Component Brief | Contract Graph | Evidence Ledger |
|---|---|---|---|---|
| L0 | Lightweight summary inside the Analysis Report | Not required | Not required | Not required |
| L1 | Lightweight repo orientation | Not required unless useful | Not required | Key assumptions only |
| L2 | One paragraph + 3-5 key paths | 5-bullet summary | Affected edges only when contracts are mentioned | Top 3 claims |
| L3 | Full template | Full template | Full edge table | Full table |
| L4+ | Full template + cross-component view | Full template per owner | Full edge table + impact map | Full table + skeptic pass |

## Required output: Intake artifact

Produce this block — even for L0 tasks — it is the routing receipt:

```md
## Intake

- Task:
- Mode: read-only | implementation
- Scope:
- Primary task type:
- Secondary task types:
- Autonomy level:
- Risk mode:
- Initial assumptions:
- Known constraints:
- First areas to inspect:
```

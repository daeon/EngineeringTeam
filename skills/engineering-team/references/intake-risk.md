# Intake and Risk Classification

**Produce the `## Intake` artifact before deep routing or implementation.** Minimal repo discovery is allowed when needed to classify scope accurately, but do not start broad investigation, specialist routing, or edits before intake is recorded.

Classify every task before routing or implementing.

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

## Step 3: Assign autonomy level

See `references/autonomy-ladder.md` for the single-owner L0–L5 definition.

| Level | Meaning | Required before edit |
|---|---|---|
| L0 | Read-only exploration or analysis (no edits) | Lightweight Repo Atlas + Analysis Report |
| L1 | Plan only | Repo Atlas |
| L2 | Local patch, no behavior change | Component Brief + nearby pattern/test |
| L3 | Behavior change | Contract Graph + regression test or verification path |
| L4 | Multi-component change | Impact Map + specialist review |
| L5 | Architecture, migration, security, release, or production-sensitive change | Explicit constraints + rollout/rollback plan + skeptic gate |

Escalate level when a change touches public contracts, auth, permissions, persistence, external services, generated code, production rollout, or legacy compatibility.

## Step 4: Choose risk mode

| Risk mode | Meaning | Default routing |
|---|---|---|
| `low-risk-local` | Obvious local edit or explanation | Lead only; no advisor |
| `behavior-change` | Local behavior, tests, or contracts may change | Verifier + skeptic as needed; use diagnosis loop for bug-driven changes |
| `cross-component` | Multiple modules, packages, services, or owners | Investigator + architect + skeptic |
| `security-sensitive` | Trust boundary, auth, inputs, secrets, shell, filesystem, network, dependency risk | Security + skeptic; advisor for L5 or uncertainty |
| `migration/compatibility` | Legacy behavior, config/schema/API translation, upgrade or import/export risk | Migration + release + skeptic; advisor for irreversible or ambiguous choices |
| `release/production` | Runtime, rollout, rollback, observability, live system, or production behavior | Release + advisor; human approval before sensitive side effects |
| `uncertain-root-cause` | Investigation has not converged on evidence-backed root cause | Investigator + skeptic + advisor before implementation; feedback loop before hypotheses |
| `conflicting-evidence` | Source, tests, docs, logs, or runtime observations disagree | Investigator + skeptic + advisor before implementation |

## L0 fast path

When autonomy level is L0, proceed to a lightweight Repo Atlas, then produce an Analysis Report. Skip agent routing, contract graph, evidence ledger, advisor gate, implementation gate, and verification loop. Context GC still applies.

L0 tasks: codebase audits, feedback requests, "analyze this repo", "what are the risks here?", architecture surveys with no planned change, PR or diff reviews that produce findings only.

## Artifact depth by autonomy level

Produce artifacts at the depth the level requires. Do not skip artifacts entirely; produce a minimal valid form when depth is low.

| Level | Repo Atlas | Component Brief | Contract Graph | Evidence Ledger |
|---|---|---|---|---|
| L0 | Lightweight summary inside the Analysis Report | Not required | Not required | Not required |
| L2 | One paragraph + 3–5 key paths | 5-bullet summary | Affected edges only (2–4 rows) | Top 3 claims |
| L3 | Full template | Full template | Full edge table | Full table |
| L4+ | Full template + cross-component view | Full template per owner | Full edge table + impact map | Full table + skeptic pass |

## Required output: Intake artifact

Produce this block — even for L0 tasks — it is the routing receipt:

```md
## Intake

- Task:
- Scope:
- Primary task type:
- Secondary task types:
- Autonomy level:
- Risk mode:
- Initial assumptions:
- Known constraints:
- First areas to inspect:
```

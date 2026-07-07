# Impact Map

For L4+ multi-component changes, map the blast radius before editing. The Impact Map turns "this touches several components" into an explicit, reviewable list of affected owners, contracts, consumers, and verification per edge. `references/contract-graph.md` owns the canonical edge vocabulary used here.

Build it after the Contract Graph and before the Implementation Gate. It is the cross-component view that the gate and specialist review reference for L4+ work.

## When required

- L4 (multi-component change) and above — see `references/autonomy-ladder.md` and `references/intake-risk.md`.
- Any change whose edits span more than one component or owner, or that modifies a shared contract.

## How to build

1. List each component the change touches (file or directory + owner).
2. For each, record the contract edges entering and leaving it (reuse the Contract Graph).
3. Identify downstream consumers that could break.
4. Assign the specialist lens and the verification for each affected edge.
5. Sequence the edits so the tree stays releasable between steps.

## Artifact: Impact Map

```md
# Impact Map

| Component | Owner | Change | Contract edges touched | Downstream consumers | Specialist lens | Verification | Risk |
|---|---|---|---|---|---|---|---|

## Edit sequence
1.
2.

## Cross-component risks
-

## Rollback boundary
-
```

Keep it compact: one row per affected component, each tied to evidence in the Contract Graph and a check in the Verification Report.

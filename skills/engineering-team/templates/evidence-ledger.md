# Evidence Ledger

Tie every major claim to evidence before it enters the plan. Confidence is one
of: Proven, Plausible, Contradicted, Irrelevant, or Assumption. Anything that
is not Proven or Plausible is not a basis for editing.

House style: use `Claim | Evidence | Confidence | Impact | Next action` for
claim tables. Put the evidence next to the claim; do not bury it in prose.

> Anti-pattern: smuggling a guess into the plan as if it were established fact.

| Claim | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
| Domain requires `discount_fraction` in `[0,1]` | docstring + guard in `src/pricing.py` | Proven | Fix must not change the guard | Preserve consumer contract |

## Rejected or Deferred Claims

| Claim | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  | Evidence that ruled it out or made it insufficient | Contradicted / Irrelevant / Assumption |  | Reject / defer / probe |

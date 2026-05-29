# Evidence Ledger

Tie every major claim to evidence before it enters the plan. Confidence is one
of: Proven, Plausible, Contradicted, Irrelevant, or Assumption. Anything that
is not Proven or Plausible is not a basis for editing.

> Anti-pattern: smuggling a guess into the plan as if it were established fact.

| Claim | Evidence | Confidence | Impact |
|---|---|---:|---|
| <!-- example --> Domain requires `discount_fraction` in `[0,1]` | docstring + guard in `src/pricing.py` | Proven | Fix must not change the guard |

List rejected approaches and the evidence that ruled them out, so reviewers see
what you did not do and why.

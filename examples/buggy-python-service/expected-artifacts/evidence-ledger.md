# Evidence Ledger

| Claim | Evidence | Confidence | Impact |
|---|---|---:|---|
| Domain contract requires `discount_fraction` in `[0,1]` | docstring + guard in `src/pricing.py` `compute_total_cents` | Proven | Defines where the fix must not go |
| `checkout` forwards a percentage, not a fraction | `src/api.py`: `compute_total_cents(items, discount_percent)` | Proven | Identifies the real defect location |
| The guard, not the math, raises the error | traceback ends at the `raise ValueError` in `src/pricing.py` | Proven | Rules out a rounding/arithmetic fix |
| Bug is unguarded by tests for non-zero discounts | `tests/test_api.py` only tests `discount_percent=0` | Proven | Explains why the suite is green |
| Only `checkout` calls `compute_total_cents` | grep across `src/` | Proven | Confirms fixing the boundary is safe and sufficient |
| Fixing at the boundary (`/100`) preserves the contract | domain contract unchanged; only the adapter changes | Plausible (verified by new regression test) | Smallest safe change |

## Rejected approaches

- Loosening the `[0,1]` guard — contradicted by the domain contract claim.
- Clamping the total or dividing inside `compute_total_cents` — breaks every
  caller that already passes a correct fraction.

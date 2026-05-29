# Verification Report

| Command | Result | Relevant Output | Related? | Next Action |
|---|---|---|---|---|
| `python3 -m unittest discover -s tests -v` (before fix) | PASS (5 tests) | suite green despite the latent bug | Yes | Add a failing regression test for a non-zero discount |
| reproduce: `checkout({..., "discount_percent": 20})` (before fix) | FAIL | `ValueError: discount_fraction must be in [0, 1], got 20` | Yes | Confirms the boundary unit mismatch |
| new test `test_checkout_with_discount` (before fix) | FAIL | `ValueError` raised | Yes | Apply boundary fix `discount_percent / 100` in `src/api.py` |
| `python3 -m unittest discover -s tests -v` (after fix) | PASS (6 tests) | 20% discount on 2500 cents → 2000 cents | Yes | Done |

## Failure Attribution
The pre-fix failure is a hidden contract violation at the `checkout → compute_total_cents` boundary (percent vs fraction), not a domain-arithmetic bug. The guard behaved correctly.

## Coverage Gaps
Before the fix, no test exercised a non-zero discount through `checkout`. The
new regression test closes that gap. Consider a property test over discount
percentages 0–100 if the service grows.

## Unverified Risks
None for this example. If additional callers of `compute_total_cents` were
introduced, each would need the same percent→fraction discipline at its own
boundary.

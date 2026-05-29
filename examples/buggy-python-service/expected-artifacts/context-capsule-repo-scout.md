# Context Capsule: Repo Scout

## Scope

Inspected checkout entrypoint, pricing domain function, and tests.

## Findings

| Claim | Evidence | Confidence |
|---|---|---:|
| Discount enters through `checkout(payload)` | `src/api.py` `checkout()` reads `payload["discount_percent"]` | High |
| Domain `compute_total_cents` expects fraction, not percent | `src/pricing.py` docstring + `if not 0.0 <= discount_fraction <= 1.0` guard | High |
| `checkout` passes the percent value directly without converting | `src/api.py`: `compute_total_cents(items, discount_percent)` | High |
| Existing checkout test misses non-zero discount | `tests/test_api.py` only tests `discount_percent=0` | High |

## Paths worth keeping

- `src/api.py`: adapter boundary — where the fix belongs
- `src/pricing.py`: domain contract — `compute_total_cents` with fraction guard
- `tests/test_api.py`: missing regression coverage for non-zero discount

## Paths inspected but not relevant

- None

## Contradictions / risks

- Green suite hides contract mismatch because current checkout test uses zero discount (zero passes the `[0,1]` guard).

## Questions / blockers

- None

## Recommended next action

Convert percent to fraction (`discount_percent / 100`) at the API boundary in `src/api.py` and add a non-zero discount regression test in `tests/test_api.py`.

# Context Capsule: Evidence Skeptic

## Scope

Reviewed proposed fix (percent-to-fraction conversion at API boundary), checked for other callers of `compute_total_cents`, verified test coverage gaps, and assessed whether the fix is complete and safe.

## Findings

| Claim | Evidence | Confidence |
|---|---|---:|
| `compute_total_cents` guard enforces `[0.0, 1.0]`; zero passes but percent values raise | `src/pricing.py` guard: `if not 0.0 <= discount_fraction <= 1.0` | High |
| No other callers of `compute_total_cents` outside `src/api.py` | grep across `src/` | High |
| `tests/test_pricing.py` tests fraction inputs only; does not test percent rejection | `tests/test_pricing.py` | High |
| Fix is complete at the API boundary; domain contract need not change | domain contract in `src/pricing.py` is correct as-is | High |

## Paths worth keeping

- `src/api.py`: only file that needs changing (`discount_percent / 100` before calling `compute_total_cents`)
- `tests/test_api.py`: regression test for non-zero discount must be added here

## Paths inspected but not relevant

- `tests/test_pricing.py`: domain tests are correct; fraction inputs pass

## Contradictions / risks

- None. Proposed fix is consistent with the domain contract and no other callers are affected.

## Questions / blockers

- None

## Recommended next action

Approve fix. Add a regression test in `tests/test_api.py` for a non-zero `discount_percent` before implementing the `/ 100` conversion in `src/api.py`.

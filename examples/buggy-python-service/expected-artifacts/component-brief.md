# Component Brief

## Relevant Component
Checkout pricing path.

## Responsibility
Turn a checkout payload into a discounted total in cents.

## Important Files
- `src/api.py`
- `src/pricing.py`

## Relevant Symbols
- `checkout(payload)` — `src/api.py`
- `compute_total_cents(items, discount_fraction)` — `src/pricing.py`
- `LineItem` — `src/pricing.py`

## Main Call Path
`checkout(payload)` → builds `LineItem`s → `compute_total_cents(items, discount)`.

## Related Tests
- `tests/test_api.py::CheckoutTest::test_checkout_without_discount`
- `tests/test_pricing.py::ComputeTotalCentsTest` (4 tests, including the `[0,1]`
  guard test).

## Similar Existing Patterns
The domain layer guards its own contract and raises `ValueError` on violation;
follow that pattern rather than adding defensive clamping.

## Inputs / Outputs
- Input: `{"items": [...], "discount_percent": 0-100}`.
- Output: `{"total_cents": int}`.

## Side Effects
None.

## Open Questions
Do other callers of `compute_total_cents` exist? (In this example, only
`checkout`. Confirmed by grep.)

## Evidence
- `src/pricing.py` docstring and guard define the `[0,1]` fraction contract.
- `src/api.py` forwards `discount_percent` directly to the domain function.
- `tests/test_api.py` exercises only a `0` discount.

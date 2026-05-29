# EngineeringTeam prompt

```text
Use engineering-team to investigate this bug. Checkout raises
"ValueError: discount_fraction must be in [0, 1], got 20" for a 20% discount.

Map the repo first, find the owning component, trace the discount value from the
request boundary to the domain function, and identify which contract is
violated and where. Do not edit until you can show the contract graph and the
evidence. Then propose the smallest safe fix at the correct boundary and add a
regression test.
```

## Expected EngineeringTeam outcome

1. **Repo Atlas** — small Python service, two layers (`src/api.py` boundary,
   `src/pricing.py` domain), `unittest` suite under `tests/`, run with
   `python3 -m unittest discover -s tests`.
2. **Component Brief** — owning component is the checkout path; key symbols are
   `checkout` and `compute_total_cents`; related tests are `test_api.py` and
   `test_pricing.py`.
3. **Contract Graph** — the edge `checkout -> compute_total_cents` carries a
   discount value. Producer sends a *percentage* (`20`); consumer's contract
   requires a *fraction* (`0.20`). The mismatch is the failure.
4. **Evidence Ledger** — the domain contract is proven by the docstring and the
   guard in `src/pricing.py`; the mismatch is proven by `src/api.py` forwarding
   `discount_percent` directly; the coverage gap is proven by `test_api.py`
   only exercising a `0` discount.
5. **Smallest safe fix** — convert at the boundary in `src/api.py`
   (`discount_percent / 100`); leave the domain contract and guard untouched.
6. **Verification Report** — add a regression test for a non-zero discount,
   then run the full suite and confirm green.

See `../expected-artifacts/` for filled-in versions.

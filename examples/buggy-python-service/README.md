# Example: buggy-python-service

A deliberately small service with one realistic bug hiding behind a **contract
boundary**. It exists to show the difference between a lone agent that patches
the first symptom it sees and the EngineeringTeam workflow that selects the
right expert lenses, traces the contract, gathers evidence, fixes the real
boundary, and verifies.

## The service

```text
src/pricing.py   domain layer: compute_total_cents(items, discount_fraction)
src/api.py       request boundary: checkout(payload)
tests/           unit tests
```

- `compute_total_cents` has an explicit contract: `discount_fraction` must be a
  fraction in `[0.0, 1.0]`. It guards that contract and is well tested.
- `checkout` parses a human-facing payload that carries `discount_percent`
  (a number from 0 to 100) and forwards it to the domain layer.

## The bug

`checkout` forwards `discount_percent` (for example `20`) straight into
`compute_total_cents`, which expects a fraction (`0.20`). The units do not
match across the boundary.

The test suite is **green** because the only checkout test uses a `0` discount,
where percent and fraction happen to coincide. Any non-zero discount raises:

```text
ValueError: discount_fraction must be in [0, 1], got 20
```

## Run it

```bash
cd examples/buggy-python-service
python3 -m unittest discover -s tests -v        # suite is green
python3 -c "from src.api import checkout; print(checkout({'items':[{'name':'w','unit_price_cents':1000,'quantity':2}],'discount_percent':20}))"
```

The second command reproduces the bug.

## Two paths

- `prompts/raw-agent.md` — the prompt a hurried user gives a lone agent. The
  likely outcome is a symptom patch: loosen the `[0, 1]` guard or clamp the
  total, which hides the defect and breaks the domain contract.
- `prompts/engineering-team.md` — the EngineeringTeam prompt. The lead routes
  the right expert lenses, maps the repo, traces the discount contract from `checkout` to
  `compute_total_cents`, identifies the unit mismatch at the boundary, fixes it
  in the adapter (`discount_percent / 100`), and adds a regression test.

## Expected artifacts

`expected-artifacts/` holds filled-in versions of what the EngineeringTeam
workflow should produce for this bug. They are hand-written reference ideals,
not captured agent output — use them to judge the shape and rigor of a real
run, not to diff against it line by line:

- `repo-atlas.md`
- `component-brief.md`
- `contract-graph.md`
- `evidence-ledger.md`
- `verification-report.md`

## The correct fix

Convert units at the boundary, where the percentage is known, and leave the
domain contract intact:

```python
# src/api.py
discount_percent = payload.get("discount_percent", 0)
total_cents = compute_total_cents(items, discount_percent / 100)
```

Then add the missing regression test in `tests/test_api.py` for a non-zero
discount (a 20% discount on a 2500-cent order should yield 2000 cents).

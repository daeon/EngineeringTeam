# Contract Graph

| Edge | Producer | Contract / Data Shape | Consumer | Side Effect | Failure Mode | Coverage | Risk |
|---|---|---|---|---|---|---|---|
| payload → checkout | external caller | `discount_percent` is 0–100 (percentage) | `checkout` (`src/api.py`) | none | malformed payload | `test_api` (0% only) | Low |
| checkout → compute_total_cents | `checkout` | **expects** `discount_fraction` in `[0.0, 1.0]` | `compute_total_cents` (`src/pricing.py`) | none | **unit mismatch: percent passed as fraction → `ValueError` for any non-zero discount** | none for non-zero discount | **High** |
| compute_total_cents → caller | `compute_total_cents` | returns total in cents (int) | `checkout` | none | rounding | `test_pricing` | Low |

## Reading

The failing edge is `checkout → compute_total_cents`. The producer emits a
percentage; the consumer's documented contract requires a fraction. The guard
in `compute_total_cents` correctly rejects `20`. The defect is the missing
conversion in the producer (`src/api.py`), not the guard in the consumer.

The correct seam for the fix is the boundary (`src/api.py`), because that is
where the percentage semantics are known. Changing the consumer would break the
contract for every correct caller.

# Contract Graph

Trace the affected behavior as edges between producers and consumers, not a
list of files. One row per boundary the change touches. The goal is to locate
the *failing edge* and the *correct seam* for the fix.

House style: contract rows lead with the edge, then evidence, confidence,
contract/risk, and next action.

> Anti-pattern: fixing the crash site instead of the boundary whose contract is
> actually violated.

| Edge | Evidence | Confidence | Contract / data shape | Failure mode / next action |
|---|---|---:|---|---|
| checkout → compute_total_cents | Producer: `checkout` (`src/api.py`); Consumer: `compute_total_cents` (`src/pricing.py`); Coverage: none for non-zero discount | Proven | expects fraction `[0,1]`; side effect: none | percent passed as fraction → `ValueError`; edit seam: normalize before consumer |

After the table, name the failing edge and the seam you will edit, and why
editing elsewhere would break other callers. Keep it to a few lines.

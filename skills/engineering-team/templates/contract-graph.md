# Contract Graph

Trace the affected behavior as edges between producers and consumers, not a
list of files. One row per boundary the change touches. The goal is to locate
the *failing edge* and the *correct seam* for the fix.

> Anti-pattern: fixing the crash site instead of the boundary whose contract is
> actually violated.

| Edge | Producer | Contract / Data Shape | Consumer | Side Effect | Failure Mode | Coverage | Risk |
|---|---|---|---|---|---|---|---|
| <!-- example --> checkout → compute_total_cents | `checkout` (src/api.py) | expects fraction `[0,1]` | `compute_total_cents` (src/pricing.py) | none | percent passed as fraction → `ValueError` | none for non-zero discount | High |

After the table, name the failing edge and the seam you will edit, and why
editing elsewhere would break other callers. Keep it to a few lines.

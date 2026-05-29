# Repo Atlas

## System Type
Small order-pricing service split into a request boundary and a pure domain layer.

## Main Languages / Frameworks
Python 3 standard library only. No third-party dependencies.

## Runtime / Build Model
Importable package; no build step. Tests run with `unittest`.

## Main Components
- `src/api.py` — request boundary (`checkout`).
- `src/pricing.py` — domain layer (`LineItem`, `compute_total_cents`).

## Entry Points
`checkout(payload)` in `src/api.py`.

## Test Surfaces
- `tests/test_api.py` — boundary tests.
- `tests/test_pricing.py` — domain tests.

## Domain Context
"Discount" is represented two ways: a human-facing **percentage** (0–100) at the
API, and a **fraction** (`[0.0, 1.0]`) in the domain. Conversion is the
boundary's job.

## Relevant ADRs
None present.

## Generated Code Rules
None. No codegen in this example.

## Config / Schema Sources
The payload shape is documented in the `checkout` docstring; there is no schema file.

## External Integration Points
None. Pure in-process functions.

## Known High-Risk Areas
The percent-to-fraction conversion at the `src/api.py` boundary.

## Repo-Specific Instructions
None beyond the docstring contract on `compute_total_cents`.

## Build / Test Commands
```bash
python3 -m unittest discover -s tests -v
```

## Last Verified
Suite green at 5 tests before the fix.

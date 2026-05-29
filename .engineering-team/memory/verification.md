# Verification Memory

Reusable verification commands and known constraints go here.

Use this format:

```md
## <command or check>

- Status: current | needs-verification | stale
- Purpose:
- Command:
- Expected result:
- Evidence/source paths:
- Last verified:
```

## Full package validation (CI gate)

- Status: current
- Purpose: The narrowest meaningful whole-repo check; mirrors GitHub Actions.
- Command: `npm run validate`
- Expected result: Runs `validate-package.py` + `validate-codex-package.py` + `generate-agents.py --check` + `bump-version.py --check` + `node --check .opencode/plugins/engineering-team.js` + `npm run test:examples`; ends with `OK: multi-harness plugin package structure is valid` and the example unittests passing.
- Evidence/source paths: `package.json` (scripts.validate), `.github/workflows/validate.yml`
- Last verified: 2026-05-29

## Local health superset

- Status: current
- Purpose: Local doctor check before pushing.
- Command: `python3 scripts/doctor.py`
- Expected result: Runs the validators and example tests; reports all checks OK.
- Evidence/source paths: `scripts/doctor.py`
- Last verified: 2026-05-29

## Worked example tests

- Status: current
- Purpose: Exercises the demo service used to show raw-agent vs EngineeringTeam value.
- Command: `cd examples/buggy-python-service && python3 -m unittest discover -s tests -v`
- Expected result: 5 tests pass; the documented contract bug (unit mismatch between `src/api.py` and `src/pricing.py`) is reproducible separately.
- Evidence/source paths: `package.json` (scripts.test:examples), `examples/buggy-python-service/`
- Last verified: 2026-05-29

## Regenerate agents after editing YAML

- Status: current
- Purpose: Keep generated native agents in sync with `agents-src/*.yaml`.
- Command: `npm run generate:agents` (then `npm run check:agents` to confirm no drift)
- Expected result: Generated files updated; `--check` reports no drift.
- Evidence/source paths: `scripts/generate-agents.py`, `package.json`
- Last verified: 2026-05-29

## Environment constraint

- Status: current
- Purpose: Tooling expectations.
- Command: n/a
- Expected result: Python 3 + Node available. CI matrix runs Python 3.11 and 3.12 on Ubuntu with Node 22. No third-party runtime dependencies.
- Evidence/source paths: `.github/workflows/validate.yml`, `package.json`
- Last verified: 2026-05-29

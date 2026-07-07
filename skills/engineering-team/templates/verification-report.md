# Verification Report

Record what you actually ran, narrowest checks first. Every claim of "it works"
needs a command and its output. If a check fails, attribute the failure before
patching again.

House style: every verification row records the command/source as evidence,
confidence in relevance, result/risk, and the next action.

> Anti-pattern: reporting success without a command, or patching on a red test
> without classifying why it is red.

| Check | Evidence | Confidence | Result / risk | Next action |
|---|---|---:|---|---|
| `python3 -m unittest discover -s tests` | Relevant output: 20% discount → 2000 cents | Proven | PASS (6 tests); Related: Yes | Done |

## Failure Attribution

| Failure | Evidence | Confidence | Classification | Next action |
|---|---|---:|---|---|
|  |  |  | wrong impl / wrong test / env / flaky / hidden contract / generated-code mismatch / stale docs / tooling |  |

## Coverage Gaps

| Gap | Evidence | Confidence | Risk | Next action |
|---|---|---:|---|---|
|  |  |  |  |  |

## Unverified Risks

| Risk | Evidence | Confidence | Impact | Next action |
|---|---|---:|---|---|
|  |  | Assumption |  |  |

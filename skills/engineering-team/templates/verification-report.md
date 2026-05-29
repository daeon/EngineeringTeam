# Verification Report

Record what you actually ran, narrowest checks first. Every claim of "it works"
needs a command and its output. If a check fails, attribute the failure before
patching again.

> Anti-pattern: reporting success without a command, or patching on a red test
> without classifying why it is red.

| Command | Result | Relevant Output | Related? | Next Action |
|---|---|---|---|---|
| <!-- example --> `python3 -m unittest discover -s tests` | PASS (6 tests) | 20% discount → 2000 cents | Yes | Done |

## Failure Attribution
<!-- for any failure: wrong impl / wrong test / env / flaky / hidden contract / etc. -->

## Coverage Gaps
<!-- what is still untested near the change -->

## Unverified Risks
<!-- what you could not prove and why -->

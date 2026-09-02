---
name: arena
description: Run multiple isolated candidates on the same artifact, judge them on one hidden rubric, choose a base, graft only the best ideas from alternatives, and verify the synthesized result. Use when one attempt could lock in the wrong shape.
---

# Arena

Use competing artifacts when the shape of the solution matters enough that one model's first answer is a risky commitment.

Arena is not an expert-opinion panel. Every candidate receives the same task and produces the same kind of artifact independently.

## Phases

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## 1. Frame

Define:

- the exact artifact each candidate must produce;
- one task prompt shared verbatim by all candidates;
- 3-6 concrete criteria that describe success;
- the candidate count and role diversity;
- isolated writable locations for every candidate.

Keep the rubric from the candidates when exposure would cause them to optimize for scoring rather than the task itself. The user task is the contract.

Use whole-shape alternatives, not cosmetic variants. If the decision is cheap and reversible, skip Arena.

## 2. Fan out

Run all candidates independently. When the harness supports subagents, prefer parallel execution and use role-based selection such as `fast-builder`, `deep-builder`, or `different-model-family` instead of hard-coded model names.

Every candidate gets:

- the same task;
- the same grounding material;
- its own branch, worktree, temp directory, or output file;
- the same verification expectations.

Candidates may include a short rationale describing alternatives considered and rejected. Do not let them see other candidates before they finish.

If a candidate fails, continue with the remaining candidates and record the dropout.

## 3. Cross-judge

Use one independent judge, preferably from a different model family or reasoning path than the dominant candidate set. The judge sees:

- sanitized candidate labels;
- complete candidate artifacts;
- the common rubric.

The judge scores every candidate in one pass so calibration stays consistent. The judge recommends a base but does not mutate any artifact.

## 4. Pick

The parent or lead reads every candidate end to end and scores the same rubric independently.

Agreement with the judge increases confidence. Disagreement triggers inspection of the criterion, evidence, and candidate rationale; it does not automatically mean the judge is wrong.

Prefer the artifact a future maintainer can extend with the least hidden coupling and smallest unnecessary surface.

## 5. Graft

Review losing candidates for ideas worth preserving. Usually only one or two ideas deserve to move.

Integrate them deliberately into the chosen base. Do not paste incompatible fragments together. Record:

- what was grafted and from where;
- what was rejected and why;
- where multiple candidates converged independently.

If candidates diverged because the prompt was underspecified, reframe and rerun instead of averaging incompatible designs.

## 6. Verify

Run the synthesized artifact through the real acceptance checks. Arena increases search quality; it does not replace verification.

If verification fails, determine whether the framing was wrong, the base choice was wrong, or a useful candidate insight was missed. Fix the process at that point instead of papering over the final artifact.

## Output

Return one synthesized artifact and one short synthesis record containing:

- rubric;
- candidate labels and concise scores;
- judge recommendation;
- selected base and reason;
- grafts and rejections;
- dropouts;
- final verification result.

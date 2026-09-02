# Evaluation plan

This pack stays experimental until its behavior beats or complements the existing owned skills without creating routing ambiguity.

Use paired, blinded evaluations where practical. The candidate prompt should look like an ordinary user request; do not tell the candidate which skill behavior is being measured. Run multiple realistic fixtures so one cherry-picked task cannot decide promotion.

## Shared promotion gate

A skill can leave `experiments/` only when:

1. at least three materially different fixtures have been exercised;
2. the adapted skill is compared against the relevant baseline (existing owned skill, upstream pstack skill, or no-skill control);
3. important claims are scored from observable output, tool use, artifacts, or transcripts rather than candidate self-report;
4. no material regression appears in safety, correctness, or routing clarity;
5. the improvement is large enough to justify another maintained public skill or mode;
6. the final ownership decision is recorded in a reviewed GitHub change.

Use repetitions for stochastic tasks. Record `INCONCLUSIVE` rather than forcing a winner when differences are within noise or judge disagreement is unresolved.

## `how`

Compare against `thoughtloop/investigate` repository mode and a no-skill control.

Fixtures:

- narrow module walkthrough;
- cross-cutting runtime flow across several files;
- architecture critique request where code has one real issue and several tempting false positives.

Score:

- runtime-flow correctness;
- concrete file/symbol grounding;
- coverage of state and side effects;
- absence of invented historical rationale;
- critique precision and false-positive rate;
- answer usefulness to a maintainer.

Promotion question: does a separate `how` skill add enough focused value to justify overlap with `investigate`, or should its mechanics become an `investigate` mode/reference?

## `why`

Compare against generic repository research and `how` used incorrectly as a rationale tool.

Fixtures:

- decision with explicit PR/ticket rationale;
- decision whose rationale is split between commit history and a design document;
- plausible-looking code shape where the real historical reason is different or unknown.

Score:

- source-category coverage when sources are available;
- citation accuracy;
- separation of direct evidence from inference;
- contradictions and null results surfaced;
- hallucinated intent rate;
- confidence calibration.

Promotion question: does it reliably recover rationale that source-only investigation misses?

## `blast-radius`

Compare against current `review` and a normal caller search.

Fixtures:

- a small internal refactor with hidden serialization compatibility;
- asynchronous lifecycle/order change with non-obvious downstream timing risk;
- scary-looking change that is actually safe because of one executable invariant.

Score:

- discovery of the decisive safety invariant;
- hidden dependencies beyond direct symbol references;
- evidence level reached for material claims;
- false-positive risk volume;
- quality of the repeatable pre-merge proof.

Promotion question: separate skill versus `review` mode. Prefer folding into `review` if the standalone trigger adds no measurable routing benefit.

## `arena`

Compare against a single strong attempt and an opinion-only expert panel.

Fixtures:

- API/module design with at least two defensible shapes;
- code implementation where candidate approaches have different complexity/correctness tradeoffs;
- documentation or prompt artifact where synthesis can easily become incoherent.

Score:

- diversity of candidate shapes;
- judge/lead agreement and disagreement handling;
- quality of selected base;
- value added by grafted ideas;
- coherence after synthesis;
- final verification result;
- cost versus single-run baseline.

Promotion question: does Arena improve final artifacts enough to justify multi-run cost on one-way-door tasks?

## `unslop`

Compare against the current anti-AI-slop skill, raw model prose, and human-written reference text when available.

Fixtures:

- technical explanation full of generic AI patterns;
- concise PR description where over-editing would lose useful detail;
- prose with a strong author voice that should not be normalized away;
- text containing meaningful uncertainty and normative wording.

Score:

- preservation of facts and obligations;
- reduction in generic/repetitive AI patterns;
- voice preservation;
- unnecessary edit rate;
- human preference in blind side-by-side review.

Promotion question: keep, merge with the existing anti-slop skill, or discard. Do not maintain two skills with the same responsibility unless evaluation proves distinct modes.

## `technical-writing`

Compare against no-skill developer writing, `unslop` alone, and `standard-english` on tasks that do and do not require formal governance.

Fixtures:

- tutorial;
- task-focused how-to;
- API/reference page;
- architecture explanation;
- PR description;
- standards-sensitive requirement where the correct behavior is to defer governing language decisions to `standard-english`.

Score:

- correct document mode;
- information findability;
- command/path/symbol accuracy;
- ambiguity rate;
- preservation of constraints and exceptions;
- routing discipline with `standard-english`;
- maintainers' blind preference.

Promotion question: does this add practical developer-document structure without duplicating standards governance?

## Evidence record

Store each completed experiment with:

- fixture and prompt;
- control and candidate revision SHAs;
- runner identities or role labels;
- observable outputs and artifact paths;
- judge rubric and verdict;
- deterministic checks;
- disagreements and limitations;
- promotion recommendation.

Do not promote on "looks better." Preserve the failed cases; they define the boundary of the skill.

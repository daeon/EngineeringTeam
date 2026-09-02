---
name: why
description: Reconstruct why code, behavior, thresholds, or architecture exists by searching source history and available organizational evidence. Separate direct evidence, inference, competing hypotheses, and gaps. Use `how` for runtime behavior.
---

# Why

Investigate motivation and historical constraints without reverse-engineering intent from code shape.

## Evidence posture

Evidence comes before narrative. Historical records are incomplete and sometimes contradictory, so confidence must match the record.

Treat these as distinct:

- **Direct evidence:** a PR, commit, ticket, design document, chat message, incident, metric, or comment explicitly states the reason.
- **Inference:** several observations support a reason, but no source states it directly.
- **Hypothesis:** a plausible explanation still missing decisive evidence.
- **Gap:** a relevant source was unavailable, searched with no result, or did not answer the question.

Never turn inference into fact because it makes the story cleaner.

## Workflow

1. **Anchor in code.** Identify the exact files, symbols, lines, recent commits, linked PRs, and ticket IDs around the target.
2. **Build an evidence map.** Search every relevant source category that the environment actually exposes:
   - source control and code review;
   - issue or ticket tracker;
   - long-form docs, RFCs, ADRs, and postmortems;
   - team chat;
   - infrastructure observability and incident history;
   - error or exception tracking;
   - product analytics or warehouse data.
3. **Fan out by source when useful.** Give one read-only investigator one evidence category. Do not give investigators mutation capability merely because a connector bundles reads and writes; prefer capability-restricted tools when available.
4. **Record null results.** "Searched Jira for the threshold and found no rationale" is useful evidence. Do not omit unsuccessful searches.
5. **Triangulate.** Surface contradictions, chronology changes, rejected alternatives, thresholds derived from data, and reasons that may no longer apply.
6. **Test competing stories.** For each plausible explanation, ask what evidence should exist if it were true and whether that evidence was searched.
7. **Calibrate the conclusion.** Use confident language only for explicit evidence. Mark indirect conclusions as likely, possible, or unresolved.

## Output

- **Question.** The exact rationale being investigated.
- **Code anchor.** Files, symbols, lines, commits, PRs, or tickets that define the target.
- **Direct evidence.** Cited facts about motivation, constraints, alternatives, or incidents.
- **Reasonable inferences.** Each inference includes the evidence chain that supports it.
- **Competing hypotheses.** Include evidence for and against when more than one explanation survives.
- **What we do not know.** Missing or contradictory evidence and unavailable sources.
- **Sources consulted.** Include categories that returned nothing.

Do not answer "how does it execute?" here unless the runtime path is needed to understand the historical question. Route detailed behavior to `how`.

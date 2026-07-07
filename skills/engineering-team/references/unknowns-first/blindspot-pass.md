# Blindspot Pass

Use this phase to surface hidden assumptions before repo mapping or implementation hardens around them.

## Known knowns

List facts already backed by the user request, source files, tests, docs, logs, or command output.

```md
## Known knowns

| Fact | Evidence | Confidence |
|---|---|---:|
```

## Known unknowns

List questions that are visible and answerable through repo inspection, targeted probes, or user clarification.

```md
## Known unknowns

| Question | Best evidence source | Owner | Blocks edit? |
|---|---|---|---|
```

## Unknown knowns

Look for repository knowledge that may already exist but is easy to miss:

- local instructions such as `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or skill docs
- project memory, ADRs, domain docs, examples, fixtures, generated-code comments
- tests that encode behavior more clearly than docs
- scripts that define supported commands or packaging rules

Record these as Repo Atlas notes or Component Brief evidence.

## Unknown unknowns

Name plausible failure classes even when evidence is incomplete:

- hidden consumers of the contract
- generated-code drift
- stale docs or examples
- environment-specific behavior
- security, migration, or release side effects
- tests that pass without exercising the changed behavior

Label these as assumptions or residual risk unless a cheap probe resolves them.

## Hidden assumptions

```md
## Hidden assumptions

| Assumption | Why it might be false | Cheap falsifier | If false |
|---|---|---|---|
```

## Cheap probes

Prefer probes that are fast, reversible, and evidence-rich:

- search related terms and call sites
- inspect nearby tests or fixtures
- run a narrow validator or unit test
- compare generated and source files in check mode
- read the smallest relevant reference or ADR

Record completed probes in the Evidence Ledger or Run Ledger.

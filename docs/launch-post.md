# Launch Post

Draft copy for announcing EngineeringTeam. Adjust tone per channel.

## Short version

```md
I got tired of asking one AI coding agent to guess its way through real repos.

So I built EngineeringTeam: a repo-first workflow layer that gives the agent a
lead engineer and a selectively routed panel of software engineering experts.
For each task it picks the right specialists, makes them understand the repo,
contracts, evidence, and risk, then either makes the targeted implementation or hands
back a reviewable diagnosis.

It works across Claude Code, Codex, Cursor, Gemini CLI, OpenCode, and GitHub
custom agents.
```

## Longer version

```md
AI coding agents are fast, but speed isn't judgment. Real software work needs a
team shape: a lead to frame the problem, a codebase investigator to find
ownership, a verification engineer to define proof, an evidence skeptic to
challenge unsupported claims, and domain specialists for security, performance,
migration, architecture, or release risk when the task actually needs them.

EngineeringTeam is a repo-first workflow layer that makes one coding agent
operate like that coordinated engineering panel. The lead engineer chooses the
smallest useful team for the request, orients the panel on source-backed repo
context, traces affected contracts, gathers evidence, and gates implementation
before edits are allowed.

The product promise is not a choice between "make a code change" and "understand the
codebase." It is: pick the right experts for the job, build shared understanding,
and then take the smallest safe next step — a PR-ready patch, a read-only
diagnosis, a test strategy, a performance probe plan, or a handoff.

It produces compact, reviewable artifacts as it works — a repo atlas, component
brief, contract graph, evidence ledger, and verification report — so you can see
which experts were needed, what they concluded, and whether the final change or
diagnosis is supported by evidence.

No runtime service. No network calls. No session-start magic. Works across
Claude Code, Codex, Cursor, Gemini CLI, OpenCode, and GitHub custom agents.

There's a runnable example with a hidden-contract bug that shows the difference
between a lone agent patching the crash site and an expert panel finding the real
boundary, proving the contract mismatch, and fixing only the adapter.
```

## Talking points

- The core frame: one coding agent, operated like a coordinated engineering team.
- Expert routing is selective: smallest useful panel, not a fixed committee.
- The demo: a green test suite that still hides a contract bug.
- The artifacts make team reasoning inspectable and reviewable.
- One source of truth generates agents for every harness.
- Conservative safety posture: see `SECURITY.md`.

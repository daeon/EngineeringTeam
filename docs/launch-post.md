# Launch Post

Draft copy for announcing EngineeringTeam. Adjust tone per channel.

## Short version

```md
I got tired of AI coding agents editing before they understood the repo.

So I built EngineeringTeam: a repo-first workflow layer that makes the agent map
the codebase, trace contracts, gather evidence, route specialists only when
needed, and verify before claiming success.

It works across Claude Code, Codex, Cursor, Gemini CLI, OpenCode, and GitHub
custom agents.
```

## Longer version

```md
AI coding agents are fast, but speed isn't judgment. On real codebases the hard
part isn't typing code — it's finding the owning component, understanding the
call path, preserving contracts, and proving the change works.

EngineeringTeam is a repo-first workflow layer for AI coding agents. The rule:
no non-trivial edit until the agent can answer where the behavior enters the
system, where it's transformed, where it leaves, which contracts are affected,
what evidence supports the diagnosis, and what proves the fix.

It produces compact, reviewable artifacts as it works — a repo atlas, a contract
graph, an evidence ledger, and a verification report — so you can see whether
the agent actually understood the code path, not just whether the diff looks
plausible. Specialist agents (security, architecture, performance, migration,
release, verification) are selective, not mandatory.

No runtime service. No network calls. No session-start magic. Works across
Claude Code, Codex, Cursor, Gemini CLI, OpenCode, and GitHub custom agents.

There's a runnable example with a hidden-contract bug that shows the difference
between a raw agent patching the crash site and EngineeringTeam fixing the real
boundary with evidence.
```

## Talking points

- The demo: a green test suite that still hides a contract bug.
- The artifacts make agent reasoning inspectable and reviewable.
- One source of truth generates agents for every harness.
- Conservative safety posture: see `SECURITY.md`.

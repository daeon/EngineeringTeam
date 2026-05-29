# Harness Support

EngineeringTeam uses one canonical skill bundle and several harness-specific manifests. This keeps the workflow consistent while allowing each coding-agent environment to install it in its native way.

## Shared Skill Bundle

The canonical skill lives at:

```text
skills/engineering-team/SKILL.md
```

Supporting materials live beside it:

```text
skills/engineering-team/references/
skills/engineering-team/templates/
skills/engineering-team/scripts/
skills/engineering-team/assets/
```

## Claude Code

Claude Code reads:

```text
.claude-plugin/plugin.json
.claude-plugin/marketplace.json
agents/*.md
skills/engineering-team/
```

The Markdown agents under `agents/` provide specialist role definitions for Claude-compatible agent systems.

## Codex

Codex reads:

```text
.codex-plugin/plugin.json
skills/engineering-team/
.codex/agents/*.toml
```

Codex custom agents can also be installed into a target project:

```bash
python3 skills/engineering-team/scripts/install-custom-agents.py --scope project --repo .
```

## Cursor

Cursor reads:

```text
.cursor-plugin/plugin.json
agents/*.md
skills/engineering-team/
```

The plugin exposes the same EngineeringTeam skill and specialist roles to Cursor.

## Gemini CLI

Gemini reads:

```text
gemini-extension.json
GEMINI.md
AGENTS.md
```

`GEMINI.md` imports the shared repository guidance and tells Gemini to adapt the EngineeringTeam workflow to its available skill/tool interface.

## OpenCode

OpenCode reads:

```text
.opencode/plugins/engineering-team.js
```

The OpenCode plugin appends the repository's `skills/` directory to `config.skills.paths`. It does not inject session-start context. Users invoke `engineering-team` manually.

## GitHub Copilot custom agents (experimental)

GitHub-style custom agents are generated under:

```text
.github/agents/*.md
```

Each file is a concise, harness-neutral specialist definition with a role name, when-to-use guidance, expected output, evidence requirements, and safety/edit boundaries. They are generated from `agents-src/*.yaml`, so they stay in sync with the other harness outputs.

Install them into a target repository:

```bash
python3 scripts/install.py --target github --scope project --repo /path/to/repo
```

## Generated agents

Native agent definitions for every harness are generated from one source of truth: `agents-src/*.yaml`. Regenerate after editing a source file:

```bash
python3 scripts/generate-agents.py
```

Check for drift (also run in CI):

```bash
python3 scripts/generate-agents.py --check
```

Generation produces:

```text
agents/*.md                                                   Claude / Cursor
.codex/agents/*.toml                                          Codex
skills/engineering-team/assets/agents/*.toml                  Codex (bundled)
skills/engineering-team/references/codex-custom-agents/*.toml Codex (reference)
.github/agents/*.md                                           GitHub Copilot
```

## Version Sync

Version-bearing files are declared in `.version-bump.json`.

Check version consistency:

```bash
bash scripts/bump-version.sh --check
```

Bump all declared versions:

```bash
bash scripts/bump-version.sh 0.6.0
```

## CI

GitHub Actions runs the same command used locally:

```bash
npm run validate
```

which expands to:

```bash
python3 skills/engineering-team/scripts/validate-package.py
python3 scripts/validate-codex-package.py
python3 scripts/generate-agents.py --check
bash scripts/bump-version.sh --check
node --check .opencode/plugins/engineering-team.js
```

This catches broken manifests, stale generated agents, version drift, OpenCode JS syntax errors, and package-structure problems before release. The workflow runs on a Python 3.11 / 3.12 matrix with Node 22.

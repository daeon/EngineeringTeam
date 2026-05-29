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

GitHub Actions runs:

```bash
node --check .opencode/plugins/engineering-team.js
bash scripts/bump-version.sh --check
python3 skills/engineering-team/scripts/validate-package.py
python3 scripts/validate-codex-package.py
```

This catches broken manifests, stale paths, syntax errors, and package drift before release.

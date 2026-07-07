# Release Checklist

## Pre-release

- [ ] `npm run validate` passes locally.
- [ ] `python3 scripts/doctor.py` reports 0 failures.
- [ ] Generated agents are current (`python3 scripts/generate-agents.py --check`).
- [ ] Versions are in sync (`python3 scripts/bump-version.py --check`).
- [ ] `CHANGELOG.md` has an entry for this version.
- [ ] README quick start and install commands are accurate.
- [ ] Example suite is green (`cd examples/buggy-python-service && python3 -m unittest discover -s tests`).
- [ ] CI is green on `main`.

## Version bump

- [ ] `python3 scripts/bump-version.py <new-version>`
- [ ] `python3 scripts/bump-version.py --check`
- [ ] Move `Unreleased` notes under the new version in `CHANGELOG.md`.

## Publish

- [ ] Tag the release.
- [ ] Verify the local marketplace install flow for Claude Code and Cursor.
- [ ] Verify `python3 scripts/install.py --target codex --scope project --repo .`
      and `--target github` against a scratch repo.

## Suggested GitHub topics

```text
ai-agents
coding-agents
codex
claude-code
cursor
github-copilot
agentic-coding
software-engineering
repo-intelligence
developer-tools
```

## Post-release

- [ ] Publish `docs/internal/launch-post.md` (adjust as needed).
- [ ] Confirm badges in `README.md` resolve.

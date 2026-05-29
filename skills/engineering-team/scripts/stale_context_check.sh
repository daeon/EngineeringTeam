#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"
cd "$ROOT"
echo "# Stale Context Check"
echo
echo "## Candidate durable context files"
find . -maxdepth 4 -type f \( -name 'AGENTS.md' -o -name 'CLAUDE.md' -o -name 'README.md' -o -name '*architecture*' -o -name '*design*' -o -path '*/skills/*/SKILL.md' \) \
  -not -path './node_modules/*' -not -path './vendor/*' | sort
echo
echo "## Recently changed source files"
git log --name-only --pretty=format: --since='90 days ago' 2>/dev/null | sed '/^$/d' | sort | uniq | head -300 || true

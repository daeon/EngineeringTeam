#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"
cd "$ROOT"
echo "# Repo Snapshot"
echo
echo "## Root"
pwd
echo
echo "## Top-level files"
find . -maxdepth 2 -type f \( -name 'AGENTS.md' -o -name 'CLAUDE.md' -o -name 'README*' -o -name 'CONTRIBUTING*' -o -name 'package.json' -o -name 'pnpm-lock.yaml' -o -name 'go.mod' -o -name 'Cargo.toml' -o -name 'pyproject.toml' -o -name 'Makefile' -o -name '.gitignore' -o -name '*.sln' -o -name 'pom.xml' -o -name 'build.gradle*' \) | sort
echo
echo "## Directories"
find . -maxdepth 2 -type d | sed 's#^./##' | sort | head -200
echo
echo "## Git status"
git status --short 2>/dev/null || true

#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"
cd "$ROOT"
echo "# Changed Surface"
echo
echo "## Changed files"
git diff --name-only 2>/dev/null || true
echo
echo "## Staged files"
git diff --cached --name-only 2>/dev/null || true
echo
echo "## Public-surface-looking changes"
git diff --unified=0 2>/dev/null | grep -E '^(\+|-)\s*(export |public |interface |type |class |func |def |function |const )' || true

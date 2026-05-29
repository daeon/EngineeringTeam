#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"
cd "$ROOT"
echo "# Test Discovery"
echo
echo "## Test files"
find . -type f \( -name '*test*' -o -name '*spec*' -o -name '*_test.go' -o -name 'pytest.ini' -o -name 'jest.config.*' -o -name 'vitest.config.*' \) \
  -not -path './node_modules/*' -not -path './vendor/*' -not -path './dist/*' -not -path './build/*' | sort | head -300
echo
echo "## Likely commands"
for f in package.json pnpm-lock.yaml go.mod Cargo.toml pyproject.toml Makefile; do
  [ -f "$f" ] && echo "found $f"
done

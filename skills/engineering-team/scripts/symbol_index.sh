#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-.}"
cd "$ROOT"
echo "# Lightweight Symbol Index"
echo
if command -v rg >/dev/null 2>&1; then
  echo "## Likely definitions"
  rg -n --glob '!node_modules' --glob '!vendor' --glob '!dist' --glob '!build' \
    '^(export |func |type |class |interface |def |const |let |var |public |private |protected |static |async function|function )' . || true
else
  echo "ripgrep not found"
fi

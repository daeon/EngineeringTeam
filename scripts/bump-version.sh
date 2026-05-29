#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
CONFIG="${REPO_ROOT}/.version-bump.json"

usage() {
  echo "Usage: bump-version.sh <new-version> | --check | --audit"
}

python_check() {
  python3 - "$CONFIG" <<'PY'
import json
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
repo = config_path.parent
config = json.loads(config_path.read_text())
versions = []
missing = False

print("Version check:")
print()
for item in config["files"]:
    path = repo / item["path"]
    field = item["field"]
    if not path.exists():
        print(f"  {item['path']} ({field})  MISSING")
        missing = True
        continue
    data = json.loads(path.read_text())
    value = data
    for part in field.split("."):
        value = value[int(part)] if part.isdigit() else value[part]
    versions.append(str(value))
    print(f"  {item['path']} ({field})  {value}")

print()
if missing:
    sys.exit(1)
unique = sorted(set(versions))
if len(unique) != 1:
    print("DRIFT DETECTED - versions are not in sync:")
    for version in unique:
        print(f"  {version} ({versions.count(version)} files)")
    sys.exit(1)
print(f"All declared files are in sync at {unique[0]}")
PY
}

python_bump() {
  local new_version="$1"
  python3 - "$CONFIG" "$new_version" <<'PY'
import json
import sys
from pathlib import Path

config_path = Path(sys.argv[1])
new_version = sys.argv[2]
repo = config_path.parent
config = json.loads(config_path.read_text())

for item in config["files"]:
    path = repo / item["path"]
    field = item["field"]
    data = json.loads(path.read_text())
    target = data
    parts = field.split(".")
    for part in parts[:-1]:
        target = target[int(part)] if part.isdigit() else target[part]
    last = parts[-1]
    old = target[int(last)] if last.isdigit() else target[last]
    if last.isdigit():
        target[int(last)] = new_version
    else:
        target[last] = new_version
    path.write_text(json.dumps(data, indent=2) + "\n")
    print(f"{item['path']} ({field}): {old} -> {new_version}")
PY
}

case "${1:-}" in
  --check)
    python_check
    ;;
  --audit)
    python_check
    echo
    echo "Audit is limited to declared version fields in this lightweight script."
    ;;
  --help|-h|"")
    usage
    ;;
  --*)
    echo "error: unknown flag '$1'" >&2
    usage >&2
    exit 1
    ;;
  *)
    if [[ ! "$1" =~ ^[0-9]+\.[0-9]+\.[0-9]+ ]]; then
      echo "error: '$1' does not look like a version (expected X.Y.Z)" >&2
      exit 1
    fi
    python_bump "$1"
    echo
    python_check
    ;;
esac

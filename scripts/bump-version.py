#!/usr/bin/env python3
"""Keep version fields in sync across all harness manifests.

Version-bearing files are declared in .version-bump.json.

Usage:
  python3 scripts/bump-version.py --check         check that all declared files are in sync
  python3 scripts/bump-version.py --audit         like --check, with an audit note
  python3 scripts/bump-version.py <X.Y.Z>         bump all declared files to <X.Y.Z>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG = REPO_ROOT / ".version-bump.json"


def _get(data: dict, field: str):
    value = data
    for part in field.split("."):
        value = value[int(part)] if part.isdigit() else value[part]
    return value


def _set(data: dict, field: str, new_version: str) -> str:
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
    return str(old)


def check() -> int:
    config = json.loads(CONFIG.read_text())
    versions: list[str] = []
    missing = False
    print("Version check:")
    print()
    for item in config["files"]:
        path = REPO_ROOT / item["path"]
        field = item["field"]
        if not path.exists():
            print(f"  {item['path']} ({field})  MISSING")
            missing = True
            continue
        value = _get(json.loads(path.read_text()), field)
        versions.append(str(value))
        print(f"  {item['path']} ({field})  {value}")
    print()
    if missing:
        return 1
    unique = sorted(set(versions))
    if len(unique) != 1:
        print("DRIFT DETECTED - versions are not in sync:")
        for version in unique:
            print(f"  {version} ({versions.count(version)} files)")
        return 1
    print(f"All declared files are in sync at {unique[0]}")
    return 0


def bump(new_version: str) -> int:
    config = json.loads(CONFIG.read_text())
    for item in config["files"]:
        path = REPO_ROOT / item["path"]
        field = item["field"]
        data = json.loads(path.read_text())
        old = _set(data, field, new_version)
        path.write_text(json.dumps(data, indent=2) + "\n")
        print(f"{item['path']} ({field}): {old} -> {new_version}")
    print()
    return check()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Keep version fields in sync across harness manifests.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python3 scripts/bump-version.py --check\n"
            "  python3 scripts/bump-version.py 0.2.0\n"
        ),
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="check that all declared files are in sync")
    group.add_argument("--audit", action="store_true", help="like --check, with an audit note")
    group.add_argument("version", nargs="?", help="new version to write (e.g. 0.2.0)")
    args = parser.parse_args()

    if args.check:
        return check()
    if args.audit:
        rc = check()
        print()
        print("Audit is limited to declared version fields in .version-bump.json.")
        return rc
    if args.version:
        if not re.match(r"^\d+\.\d+\.\d+", args.version):
            print(f"error: {args.version!r} does not look like a version (expected X.Y.Z)", file=sys.stderr)
            return 1
        return bump(args.version)
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())

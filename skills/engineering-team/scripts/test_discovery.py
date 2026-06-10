#!/usr/bin/env python3
"""Discover test files and likely test commands.

Portable replacement for the former test_discovery.sh.
Usage: python3 test_discovery.py [root]
"""

from __future__ import annotations

import sys
from pathlib import Path

SKIP_DIRS = {"node_modules", "vendor", "dist", "build", ".git", "__pycache__"}
MANIFEST_FILES = ["package.json", "pnpm-lock.yaml", "go.mod", "Cargo.toml", "pyproject.toml", "Makefile"]
MAX_RESULTS = 300


def looks_like_test(name: str) -> bool:
    lowered = name.lower()
    return (
        "test" in lowered
        or "spec" in lowered
        or name == "pytest.ini"
        or lowered.startswith(("jest.config.", "vitest.config."))
    )


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    print("# Test Discovery\n")
    print("## Test files")
    results = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if SKIP_DIRS.intersection(rel.parts) or not path.is_file():
            continue
        if looks_like_test(rel.name):
            results.append(rel.as_posix())
            if len(results) >= MAX_RESULTS:
                break
    print("\n".join(results))

    print("\n## Likely commands")
    for name in MANIFEST_FILES:
        if (root / name).is_file():
            print(f"found {name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

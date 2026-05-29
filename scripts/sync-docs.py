#!/usr/bin/env python3
"""Keep CLAUDE.md in sync with AGENTS.md (single source of truth).

Claude Code reads CLAUDE.md; every other harness reads AGENTS.md. The two must
stay identical, so AGENTS.md is the source and CLAUDE.md is generated from it.
This removes the drift risk of maintaining two byte-identical files by hand.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "AGENTS.md"
TARGET = REPO_ROOT / "CLAUDE.md"


def check() -> int:
    if not SOURCE.exists():
        print("missing AGENTS.md")
        return 1
    if not TARGET.exists() or TARGET.read_text() != SOURCE.read_text():
        print("CLAUDE.md is out of sync with AGENTS.md; run: python3 scripts/sync-docs.py")
        return 1
    print("CLAUDE.md is in sync with AGENTS.md.")
    return 0


def sync() -> None:
    if not SOURCE.exists():
        raise SystemExit("missing AGENTS.md")
    TARGET.write_text(SOURCE.read_text())
    print("Synced CLAUDE.md from AGENTS.md.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if CLAUDE.md is out of sync with AGENTS.md")
    args = parser.parse_args()

    if args.check:
        return check()
    sync()
    return 0


if __name__ == "__main__":
    sys.exit(main())

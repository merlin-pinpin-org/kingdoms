#!/usr/bin/env python3
"""Session checklist, run mechanically (docs/CONVENTIONS.md).

Fail-closed check of everything a session must leave consistent across the
three Kingdoms repositories:

- docs validation: scripts/validate_docs.py --check (mods docs, docstrings,
  Mermaid syntax) against the kingdoms-services clone;
- roadmap drift: scripts/sync_roadmap.py --check (issue states vs ROADMAP.md);
- dependency-graph drift: scripts/sync_dependencies.py --dry-run against the
  committed docs/DEPENDENCIES.md (open issues, size/priority labels).

Exit code is non-zero when any check fails; each failure line names the exact
artefact to fix. The script never writes anything — it reports.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPOS = ("kingdoms", "kingdoms-infra", "kingdoms-services")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run_check(name: str, cmd: list[str]) -> list[str]:
    """Run one check; return its failure lines (empty when it passes)."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"PASS  {name}")
        return []
    print(f"FAIL  {name}")
    lines = (result.stdout + result.stderr).strip().splitlines()
    return [f"{name}: {line}" for line in lines if line]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--source",
        required=True,
        help="kingdoms-services source root (src/kingdoms)",
    )
    parser.add_argument(
        "--config",
        required=True,
        help="kingdoms-services config root (config)",
    )
    args = parser.parse_args()

    root = repo_root()
    checks: list[list[str]] = [
        run_check(
            "docs validation",
            [
                "python3",
                str(root / "scripts" / "validate_docs.py"),
                "--check",
                "--source",
                args.source,
                "--config",
                args.config,
            ],
        ),
        run_check(
            "roadmap drift",
            ["python3", str(root / "scripts" / "sync_roadmap.py"), "--check"],
        ),
    ]

    deps_out = Path("/tmp") / "kingdoms-dependencies-check.md"
    deps_result = subprocess.run(
        [
            "python3",
            str(root / "scripts" / "sync_dependencies.py"),
            "--out",
            str(deps_out),
        ],
        capture_output=True,
        text=True,
    )
    committed = (root / "docs" / "DEPENDENCIES.md").read_text()
    generated = deps_out.read_text() if deps_out.exists() else ""
    deps_out.unlink(missing_ok=True)
    if deps_result.returncode == 0 and generated == committed:
        print("PASS  dependency-graph drift")
    else:
        print("FAIL  dependency-graph drift")
        checks.append(
            ["dependency-graph: docs/DEPENDENCIES.md is out of date"
             " — run scripts/sync_dependencies.py and commit the result"]
        )

    failures = [line for group in checks for line in group]
    if failures:
        print("\nThe following need fixing before ending the session:")
        for line in failures:
            print(f"- {line}")
        return 1
    print("\nAll session checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

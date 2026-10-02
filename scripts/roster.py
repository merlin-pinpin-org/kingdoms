#!/usr/bin/env python3
"""Canonical CONTRIBUTORS.md roster parser and authority checks.

One module, used everywhere a decision depends on who may do what:
- CLI (this file): `roster.py check <login> <capability> [--pr-author <login>]`
- Library: `from roster import Roster` (scripts and workflows).

The authority matrix lives in CONTRIBUTORS.md (the doc is the truth);
this module encodes the keyword->role rules from that matrix. Changing
the rules is a roster PR: edit the matrix, mirror the change here, and
the maintainers review both in the same PR.

Capabilities (from the authority matrix):
  deploy       -> requestor rostered (vibe or better); never prod-like
  env-control  -> ops (any env) or dev (test only)
  release      -> dev or platform
  rollback     -> ops
  sync-teams   -> platform
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field

ROLE_LEVELS = {"none": 0, "vibe": 1, "mod": 2, "dev": 3, "platform": 3, "ops": 3}

CAPABILITY_RULES: dict[str, dict] = {
    "deploy": {"min": "vibe", "deny_envs_prod": True, "help": "deploy a PR to a non-prod env"},
    "env-control": {"roles": ["ops", "dev"], "test_only_roles": ["dev"], "help": "start/stop/restart/status an env"},
    "release": {"roles": ["dev", "platform"], "help": "tag and release"},
    "rollback": {"roles": ["ops"], "help": "revert a pin"},
    "sync-teams": {"roles": ["platform"], "help": "run the roster sync"},
}


@dataclass
class Person:
    login: str
    alias: str = ""
    email: str = ""
    cla: str = "none"
    teams: list[str] = field(default_factory=list)
    roles: list[str] = field(default_factory=list)
    owns: str = ""
    agent_scope: str = ""


MEMBER_ROW = re.compile(r"^\|\s*@([A-Za-z0-9-]+)\s*\|")


def parse_roster(path: str) -> dict[str, Person]:
    people: dict[str, Person] = {}
    section = ""
    with open(path) as fh:
        for line in fh:
            if line.startswith("## "):
                section = line[3:].strip()
                continue
            if section != "Contributors" or not MEMBER_ROW.match(line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 9 or cells[0].lstrip("@") == "Login":
                continue
            login = cells[0].lstrip("@")
            people[login] = Person(
                login=login,
                alias=cells[1],
                email=cells[2],
                cla=cells[4],
                teams=[t.strip().strip("`") for t in cells[5].split(",") if t.strip()],
                roles=[r.strip() for r in re.split(r",(?![^(]*\))", cells[6]) if r.strip()],
                owns=cells[7],
                agent_scope=cells[8],
            )
    return people


def check(person: Person | None, capability: str, env: str = "", pr_author: Person | None = None) -> tuple[bool, str]:
    """Return (allowed, reason). Mirrors the authority matrix exactly."""
    rule = CAPABILITY_RULES.get(capability)
    if not rule:
        return False, f"unknown capability: {capability}"
    if person is None:
        return False, "requestor has no roster entry (CONTRIBUTORS.md) — ask a maintainer for onboarding"
    roles = {re.split(r"[(,]", r)[0].strip() for r in person.roles}
    roles = {r for r in roles if r and r != ")"}

    if "roles" in rule:
        if not roles & set(rule["roles"]):
            return False, f"{person.login} roles {sorted(roles) or ['none']} do not grant '{capability}' (needs one of {rule['roles']}, per the authority matrix)"
        if env == "prod" and "test_only_roles" in rule:
            if roles & set(rule["test_only_roles"]) and not roles & (set(rule["roles"]) - set(rule["test_only_roles"])):
                return False, f"'{capability}' on prod requires ops (the authority matrix)"
    elif "min" in rule:
        granted = any(ROLE_LEVELS.get(r, 0) >= ROLE_LEVELS[rule["min"]] for r in roles)
        if not granted:
            return False, f"{person.login} roles {sorted(roles) or ['none']} do not grant '{capability}' (needs {rule['min']}+, per the authority matrix)"

    # CLA is a precondition for any mutating action
    if not person.cla.lower().startswith("accepted"):
        return False, f"{person.login} has no accepted CLA on record (roster says: {person.cla})"

    # Agent-mediated actions: the PR author's agent-scope must cover it too
    if pr_author is not None:
        scope = pr_author.agent_scope.lower()
        if capability in ("deploy", "rollback", "env-control", "release", "sync-teams"):
            if "fully on their behalf" not in scope and capability in ("deploy", "env-control") and "deploy" not in scope and "drive" not in scope:
                return False, f"PR author {pr_author.login}'s agent-scope does not cover '{capability}': \"{pr_author.agent_scope}\""
    return True, f"{person.login} ({', '.join(sorted(roles)) or 'no roles'}) may '{capability}'{f' on {env}' if env else ''}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--roster", default="CONTRIBUTORS.md")
    parser.add_argument("login")
    parser.add_argument("capability", choices=list(CAPABILITY_RULES))
    parser.add_argument("--env", default="")
    parser.add_argument("--pr-author", default="")
    args = parser.parse_args()

    roster = parse_roster(args.roster)
    ok, reason = check(
        roster.get(args.login),
        args.capability,
        env=args.env,
        pr_author=roster.get(args.pr_author) if args.pr_author else None,
    )
    print(json.dumps({"allowed": ok, "reason": reason}))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

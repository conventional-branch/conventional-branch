#!/usr/bin/env python3
"""Conformance test for the Conventional Branch specification.

Runs four checks, all driven by the canonical machine-readable spec
(static/spec.json) so the docs, the registry and the grammar cannot drift
apart silently:

  1. Fixtures    — every case in tests/fixtures.json matches the spec regex.
  2. Docs table  — the valid/invalid examples table in content/_index.md
                   agrees with the spec regex (the docs validate themselves).
  3. Consistency — the regex accepts every declared type/alias and trunk
                   branch, and every AI agent prefix in data/agents.yaml is a
                   declared type (no registry/spec drift).
  4. Badge       — the version rendered in static/badge.svg is the version
                   spec.json declares, so the adoption badge cannot go stale.

Exits non-zero if anything disagrees. Standard library only — no deps.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "static" / "spec.json"
FIXTURES = ROOT / "tests" / "fixtures.json"
SPEC_PAGE = ROOT / "content" / "_index.md"
AGENTS = ROOT / "data" / "agents.yaml"
BADGE = ROOT / "static" / "badge.svg"


def load_spec():
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    pattern = re.compile(spec["grammar"]["regex"])
    return spec, pattern


def check_fixtures(pattern):
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    failures = []
    for case in data["cases"]:
        branch, expected = case["branch"], case["valid"]
        actual = pattern.fullmatch(branch) is not None
        if actual != expected:
            failures.append(
                f"{branch!r}: spec says {'valid' if actual else 'invalid'}, "
                f"fixture expects {'valid' if expected else 'invalid'} "
                f"({case.get('reason', '')})"
            )
    return len(data["cases"]), failures


# Rows look like: | `branch-name` | ✅ | Notes |
ROW = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*(✅|❌)\s*\|")


def check_docs_table(pattern):
    failures = []
    count = 0
    for line in SPEC_PAGE.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if not m:
            continue
        branch, mark = m.group(1), m.group(2)
        count += 1
        expected = mark == "✅"
        actual = pattern.fullmatch(branch) is not None
        if actual != expected:
            failures.append(
                f"{branch!r}: docs table marks it {'valid' if expected else 'invalid'}, "
                f"spec regex says {'valid' if actual else 'invalid'}"
            )
    if count == 0:
        failures.append("no example rows found in content/_index.md — parser out of date?")
    return count, failures


def agent_prefixes():
    # Minimal, dependency-free parse of the `- prefix: <name>` entries.
    prefixes = []
    for line in AGENTS.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*-\s*prefix:\s*([A-Za-z0-9]+)", line)
        if m:
            prefixes.append(m.group(1))
    return prefixes


def check_consistency(spec, pattern):
    failures = []
    declared = {t["type"] for t in spec["types"]}

    # Every declared type and alias must be accepted with a valid description.
    for t in spec["types"]:
        for name in [t["type"], *t.get("aliases", [])]:
            if not pattern.fullmatch(f"{name}/valid-desc"):
                failures.append(f"type/alias {name!r} declared but rejected by the spec regex")

    # Every trunk branch must be accepted on its own.
    for trunk in spec["trunkBranches"]:
        if not pattern.fullmatch(trunk):
            failures.append(f"trunk branch {trunk!r} rejected by the spec regex")

    # Every registered AI agent prefix must be a declared type (no drift).
    for prefix in agent_prefixes():
        if prefix not in declared:
            failures.append(
                f"agent prefix {prefix!r} in data/agents.yaml is not a declared type in spec.json"
            )
    return failures


# The badge spells the version out four times: the accessible name, the <title>,
# and the two <text> layers that make up the drop shadow and the fill.
BADGE_VERSION = re.compile(
    r'aria-label="Conventional Branch ([^"]+)"'
    r"|<title>Conventional Branch ([^<]+)</title>"
    r"|<text[^>]*>(\d+\.\d+\.\d+)</text>"
)
BADGE_VERSION_COUNT = 4


def check_badge_version(spec):
    expected = spec["version"]
    rendered = [
        next(g for g in m.groups() if g)
        for m in BADGE_VERSION.finditer(BADGE.read_text(encoding="utf-8"))
    ]
    failures = [
        f"static/badge.svg renders version {v!r}, spec.json declares {expected!r}"
        for v in sorted(set(rendered))
        if v != expected
    ]
    if len(rendered) != BADGE_VERSION_COUNT:
        failures.append(
            f"expected {BADGE_VERSION_COUNT} version strings in static/badge.svg, "
            f"found {len(rendered)} — badge markup out of date?"
        )
    return failures


def main():
    spec, pattern = load_spec()
    ok = True

    n, failures = check_fixtures(pattern)
    ok &= not failures
    print(f"fixtures:    {n - len(failures)}/{n} passed")
    for f in failures:
        print(f"  ✗ {f}")

    n, failures = check_docs_table(pattern)
    ok &= not failures
    print(f"docs table:  {n - len(failures)}/{n} examples agree with the spec")
    for f in failures:
        print(f"  ✗ {f}")

    failures = check_consistency(spec, pattern)
    ok &= not failures
    print(f"consistency: {'ok' if not failures else str(len(failures)) + ' problem(s)'}")
    for f in failures:
        print(f"  ✗ {f}")

    failures = check_badge_version(spec)
    ok &= not failures
    print(f"badge:       {'ok' if not failures else str(len(failures)) + ' problem(s)'}")
    for f in failures:
        print(f"  ✗ {f}")

    print("\nAll conformance checks passed." if ok else "\nConformance checks FAILED.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

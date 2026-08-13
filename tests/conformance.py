#!/usr/bin/env python3
"""Conformance test for the Conventional Branch specification.

Runs seven checks, all driven by the canonical machine-readable spec
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
  5. Schema      — spec.json, and every frozen copy of it, satisfies
                   static/schema/v1/spec.schema.json.
  6. Integrations— every regex in the copy-pasteable configuration on
                   content/enforce/index.md is the spec's own, character for
                   character, so published configs cannot silently rot.
  7. Versioning  — the version spec.json declares has a frozen, byte-identical
                   copy under static/v<version>/, so the permanent endpoint
                   downstream tools pin to cannot be forgotten on a release.

Exits non-zero if anything disagrees. Standard library only — no deps.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"
SPEC = STATIC / "spec.json"
SCHEMA = STATIC / "schema" / "v1" / "spec.schema.json"
FIXTURES = ROOT / "tests" / "fixtures.json"
SPEC_PAGE = ROOT / "content" / "_index.md"
ENFORCE_PAGE = ROOT / "content" / "enforce" / "index.md"
AGENTS = ROOT / "data" / "agents.yaml"
BADGE = STATIC / "badge.svg"


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


# --- Minimal JSON Schema validator -------------------------------------------
#
# This file is standard library only, so spec.json is validated against
# schema/v1/spec.schema.json by a validator that implements exactly the keywords
# that schema uses — no more. KEYWORDS is what keeps that honest: a keyword the
# validator does not understand must fail the build, never be silently ignored,
# because an ignored assertion is a check that quietly stopped checking.

ASSERTIONS = {
    "type",
    "const",
    "enum",
    "required",
    "properties",
    "additionalProperties",
    "items",
    "minItems",
    "uniqueItems",
    "minLength",
    "pattern",
}
ANNOTATIONS = {"$schema", "$id", "title", "description"}
KEYWORDS = ASSERTIONS | ANNOTATIONS

JSON_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "boolean": bool,
    "number": (int, float),
    "integer": int,
}


def subschemas(schema, path="#"):
    """Yield (path, subschema) for every schema nested inside `schema`."""
    yield path, schema
    for name, sub in schema.get("properties", {}).items():
        yield from subschemas(sub, f"{path}/properties/{name}")
    if isinstance(schema.get("items"), dict):
        yield from subschemas(schema["items"], f"{path}/items")


def check_schema_keywords(schema):
    return [
        f"{path}: schema uses {kw!r}, which tests/conformance.py cannot evaluate — "
        f"implement it in validate() or drop it, but do not let it pass unchecked"
        for path, sub in subschemas(schema)
        for kw in sub
        if kw not in KEYWORDS
    ]


def validate(instance, schema, path="$"):
    """Return a list of validation errors. Empty means the instance conforms."""
    errors = []

    declared = schema.get("type")
    if declared:
        # bool is a subclass of int in Python; JSON Schema keeps them distinct.
        wrong_kind = isinstance(instance, bool) != (declared == "boolean")
        if not isinstance(instance, JSON_TYPES[declared]) or wrong_kind:
            return [f"{path}: expected {declared}, got {type(instance).__name__}"]

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected {schema['const']!r}, got {instance!r}")
    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} is not one of {schema['enum']}")

    if isinstance(instance, str):
        # JSON Schema's `pattern` is an unanchored search, not a full match.
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match /{schema['pattern']}/")
        if len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}: shorter than the minimum {schema['minLength']}")

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            errors.append(f"{path}: fewer than the minimum {schema['minItems']} item(s)")
        if schema.get("uniqueItems"):
            seen = {json.dumps(item, sort_keys=True) for item in instance}
            if len(seen) != len(instance):
                errors.append(f"{path}: items are not unique")
        if isinstance(schema.get("items"), dict):
            for i, item in enumerate(instance):
                errors += validate(item, schema["items"], f"{path}[{i}]")

    if isinstance(instance, dict):
        properties = schema.get("properties", {})
        for name in schema.get("required", []):
            if name not in instance:
                errors.append(f"{path}: missing required property {name!r}")
        if schema.get("additionalProperties") is False:
            for name in instance:
                if name not in properties:
                    errors.append(f"{path}: unexpected property {name!r}")
        for name, sub in properties.items():
            if name in instance:
                errors += validate(instance[name], sub, f"{path}.{name}")

    return errors


def frozen_specs():
    """Every permanent, version-pinned copy of the spec, in path order."""
    return sorted(STATIC.glob("v*/spec.json"))


def check_schema(spec):
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    failures = check_schema_keywords(schema)

    # The schema is served from static/, so its $id has to be the URL it will
    # actually resolve to — a $schema key pointing at a 404 is worse than none.
    served_at = f"{spec['url']}/{SCHEMA.relative_to(STATIC).as_posix()}"
    if schema.get("$id") != served_at:
        failures.append(
            f"{SCHEMA.relative_to(ROOT)} declares $id {schema.get('$id')!r} "
            f"but is served at {served_at!r}"
        )

    failures += [f"static/spec.json {e}" for e in validate(spec, schema)]
    for path in frozen_specs():
        instance = json.loads(path.read_text(encoding="utf-8"))
        failures += [
            f"{path.relative_to(ROOT)} {e}" for e in validate(instance, schema)
        ]
    return failures


# Every copy of the validator on the enforcement page starts one of these two ways.
# A line containing either is claiming to be the spec regex and has to be exactly it.
REGEX_MARKERS = ("^(?:main|master|develop", "^(main|master|develop")


def posix_ere(regex):
    """The spec regex as POSIX ERE, for `grep -E` in the dependency-free hook.

    `(?:` is the only construct in the published expression that POSIX does not
    have, and turning it into a plain group changes nothing about what matches —
    the groups are never referenced. `grep -P` would avoid the translation, but it
    is a GNU extension: on macOS it fails to run, and `! grep -qP` then rejects
    every branch name there is.
    """
    return regex.replace("(?:", "(")


def check_integrations(spec, pattern):
    """The enforcement page hands out copy-pasteable configuration, which is only
    worth publishing if it cannot rot. Each embedded regex must be the spec's own,
    character for character, in whichever of the three encodings its snippet needs.
    The POSIX form is additionally checked to accept exactly the same branch names,
    so the translation cannot quietly change meaning."""
    regex = spec["grammar"]["regex"]
    ere = posix_ere(regex)
    accepted = (regex, json.dumps(regex)[1:-1], ere)
    failures = []
    found = 0

    for number, line in enumerate(ENFORCE_PAGE.read_text(encoding="utf-8").splitlines(), 1):
        if not any(marker in line for marker in REGEX_MARKERS):
            continue
        found += 1
        if not any(form in line for form in accepted):
            failures.append(
                f"content/enforce/index.md:{number}: this regex is not the one in "
                f"spec.json — a config on that page would accept the wrong branches"
            )
    if not found:
        failures.append(
            "content/enforce/index.md: no validator regex found — did the page move, "
            "or did every snippet lose the pattern it is supposed to configure?"
        )

    compiled = re.compile(ere)
    for case in json.loads(FIXTURES.read_text(encoding="utf-8"))["cases"]:
        branch = case["branch"]
        if (compiled.fullmatch(branch) is not None) != (pattern.fullmatch(branch) is not None):
            failures.append(
                f"the POSIX form of the regex disagrees with the spec on {branch!r} — "
                f"the shell hook would not match the specification"
            )
    return found, failures


def check_versioning(spec):
    """Downstream tools pin /v<version>/spec.json, so releasing a new version
    without freezing a copy of it would break the promise that URL makes."""
    failures = []
    version = spec["version"]
    frozen = STATIC / f"v{version}" / "spec.json"

    if not frozen.exists():
        failures.append(
            f"static/spec.json declares version {version} but its permanent copy is "
            f"missing — run: mkdir -p static/v{version} && "
            f"cp static/spec.json static/v{version}/spec.json"
        )
    elif frozen.read_bytes() != SPEC.read_bytes():
        failures.append(
            f"static/v{version}/spec.json differs from static/spec.json — the two "
            f"URLs must serve the same bytes while {version} is the current version"
        )

    for path in frozen_specs():
        declared = json.loads(path.read_text(encoding="utf-8"))["version"]
        expected = path.parent.name[1:]
        if declared != expected:
            failures.append(
                f"{path.relative_to(ROOT)} declares version {declared!r} — a frozen "
                f"copy must keep the version of the directory it is published under"
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

    failures = check_schema(spec)
    ok &= not failures
    n = 1 + len(frozen_specs())
    print(
        f"schema:      {len(failures)} problem(s)"
        if failures
        else f"schema:      ok ({n} document(s) satisfy schema/v1)"
    )
    for f in failures:
        print(f"  ✗ {f}")

    n, failures = check_integrations(spec, pattern)
    ok &= not failures
    print(
        f"integrations: {len(failures)} problem(s)"
        if failures
        else f"integrations: ok ({n} configs embed the spec regex verbatim)"
    )
    for f in failures:
        print(f"  ✗ {f}")

    failures = check_versioning(spec)
    ok &= not failures
    print(f"versioning:  {'ok' if not failures else str(len(failures)) + ' problem(s)'}")
    for f in failures:
        print(f"  ✗ {f}")

    print("\nAll conformance checks passed." if ok else "\nConformance checks FAILED.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

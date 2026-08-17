#!/usr/bin/env python3
"""Conformance test for the Conventional Branch specification.

Runs nine checks, all driven by the canonical machine-readable spec
(static/spec.json) so the docs, the registry and the grammar cannot drift
apart silently:

  1. Fixtures    — every case in tests/fixtures.json matches the spec regex.
  2. Docs table  — the valid/invalid examples table on every language's
                   specification page agrees with the spec regex, and the
                   translations offer the same examples English does (the docs
                   validate themselves, in all eleven languages).
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
  8. Grammar     — the ABNF `type` rule, in spec.json and on every language's
                   page, offers exactly the types spec.json declares, so the
                   grammar a reader sees cannot fall behind the regex.
  9. llms.txt    — the version and the validation regex in static/llms.txt are
                   the ones spec.json declares, so a language model reading it
                   cannot answer from a stale copy of the specification.

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

# The current specification is rendered once per language, and every one of those
# pages carries its own copy of the examples table and of the ABNF grammar. Each
# copy can drift from spec.json on its own, so each one is checked.
#
# The glob is deliberately not recursive: content/v1.0.0/ is a frozen older
# specification with a narrower grammar, and holding it to today's regex would
# report the archive as broken for correctly preserving what 1.0.0 said.
SPEC_PAGES = sorted((ROOT / "content").glob("_index*.md"))
AGENTS = ROOT / "data" / "agents.yaml"
BADGE = STATIC / "badge.svg"
LLMS = STATIC / "llms.txt"


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


def table_rows(path):
    """The examples table on a page, as {branch name: marked valid?}."""
    rows = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line)
        if m:
            rows[m.group(1)] = m.group(2) == "✅"
    return rows


def check_docs_table(pattern):
    failures = []
    count = 0
    reference = table_rows(SPEC_PAGE)

    for path in SPEC_PAGES:
        name = path.relative_to(ROOT)
        rows = table_rows(path)
        count += len(rows)
        if not rows:
            failures.append(f"{name}: no example rows found — parser out of date?")
            continue

        for branch, expected in rows.items():
            actual = pattern.fullmatch(branch) is not None
            if actual != expected:
                failures.append(
                    f"{name}: marks {branch!r} {'valid' if expected else 'invalid'}, "
                    f"spec regex says {'valid' if actual else 'invalid'}"
                )

        # Every row being individually valid is a weaker promise than the tables
        # agreeing: a translation that silently omits an example still passes the
        # loop above. Parity with English is what catches a newly registered
        # prefix that was added to one page and forgotten on the other ten.
        if path == SPEC_PAGE:
            continue
        for branch in sorted(set(reference) - set(rows)):
            failures.append(f"{name}: missing the {branch!r} example content/_index.md has")
        for branch in sorted(set(rows) - set(reference)):
            failures.append(f"{name}: has a {branch!r} example content/_index.md does not")

    return count, failures


# The ABNF `type` rule, wherever it is written out. Alternatives wrap across
# several indented lines on the documentation pages, so the rule runs until the
# next one starts in column zero.
ABNF_TYPE_RULE = re.compile(r"^type\s*=(.*?)(?=^\S)", re.S | re.M)


def abnf_types(text):
    """The alternatives offered by an ABNF `type` rule, or None if there is no rule."""
    m = ABNF_TYPE_RULE.search(text)
    return set(re.findall(r'"([^"]+)"', m.group(1))) if m else None


def check_grammar_block(spec):
    """The grammar is spelled out in spec.json's `abnf` and again on every language
    page. Nothing derives one from the other, so each is checked against the types
    spec.json declares. Without this, a newly registered prefix can be live in the
    regex while the grammar a reader is actually looking at never mentions it."""
    declared = {t["type"] for t in spec["types"]} | {
        a for t in spec["types"] for a in t.get("aliases", [])
    }
    sources = [("static/spec.json", spec["grammar"]["abnf"])] + [
        (str(p.relative_to(ROOT)), p.read_text(encoding="utf-8")) for p in SPEC_PAGES
    ]

    failures = []
    for name, text in sources:
        types = abnf_types(text)
        if types is None:
            failures.append(f"{name}: no ABNF `type` rule found — did the grammar block move?")
            continue
        for missing in sorted(declared - types):
            failures.append(f"{name}: ABNF `type` rule omits {missing!r}, which spec.json declares")
        for extra in sorted(types - declared):
            failures.append(
                f"{name}: ABNF `type` rule offers {extra!r}, which spec.json does not declare"
            )
    return len(sources), failures


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


# llms.txt states the current version in three places, and each is checked on its
# own: a total would let one of them be deleted as long as another was duplicated,
# which passes while the file has quietly stopped saying something it must say.
# Each pattern is deliberately narrow — the file also names `release/v1.2.0` as an
# example description and links the 1.0.0 archive, and neither is a claim about
# what the current version is.
LLMS_VERSIONS = {
    "the title of the link to the specification": re.compile(
        r"Conventional Branch (\d+\.\d+\.\d+)"
    ),
    "the sentence introducing the version": re.compile(
        r"current version is (\d+\.\d+\.\d+)"
    ),
    "the frozen endpoint it tells tools to pin": re.compile(
        r"/v(\d+\.\d+\.\d+)/spec\.json"
    ),
}


def check_llms_txt(spec):
    """static/llms.txt restates the specification for language models, which read
    it instead of reading the site. That makes it the one file whose mistakes get
    answered back to a user as fact, so the two things it can get wrong — which
    version is current, and which branch names are valid — are held to spec.json."""
    text = LLMS.read_text(encoding="utf-8")
    expected = spec["version"]
    regex = spec["grammar"]["regex"]
    failures = []

    found = 0
    for number, line in enumerate(text.splitlines(), 1):
        if not any(marker in line for marker in REGEX_MARKERS):
            continue
        found += 1
        if line.strip() != regex:
            failures.append(
                f"static/llms.txt:{number}: this regex is not the one in spec.json — "
                f"a model reading it would validate the wrong branch names"
            )
    if not found:
        failures.append(
            "static/llms.txt: the validation regex is missing — the file no longer "
            "tells a model how to decide whether a branch name conforms"
        )

    for where, version in LLMS_VERSIONS.items():
        rendered = version.findall(text)
        if len(rendered) != 1:
            failures.append(
                f"static/llms.txt: expected exactly one current-version reference in "
                f"{where}, found {len(rendered)} — file restructured?"
            )
        failures += [
            f"static/llms.txt states version {v!r} in {where}, spec.json declares "
            f"{expected!r}"
            for v in sorted(set(rendered))
            if v != expected
        ]
    return failures


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
    print(
        f"docs table:  {len(failures)} problem(s)"
        if failures
        else f"docs table:  ok ({n} examples across {len(SPEC_PAGES)} languages)"
    )
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

    n, failures = check_grammar_block(spec)
    ok &= not failures
    print(
        f"grammar:     {len(failures)} problem(s)"
        if failures
        else f"grammar:     ok ({n} ABNF type rules match the declared types)"
    )
    for f in failures:
        print(f"  ✗ {f}")

    failures = check_llms_txt(spec)
    ok &= not failures
    print(f"llms.txt:    {'ok' if not failures else str(len(failures)) + ' problem(s)'}")
    for f in failures:
        print(f"  ✗ {f}")

    print("\nAll conformance checks passed." if ok else "\nConformance checks FAILED.")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

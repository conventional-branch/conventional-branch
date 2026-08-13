# Conformance tests

Machine-readable spec and test fixtures for the Conventional Branch specification.

## Files

| File | Purpose |
|---|---|
| [`../static/spec.json`](../static/spec.json) | The canonical machine-readable spec: types, aliases, trunk branches, rules, ABNF, and a single anchored **validation regex**. |
| [`../static/v1.1.0/spec.json`](../static/v1.1.0/spec.json) | A frozen copy of the spec as of 1.1.0. One such copy exists per released version and never changes. |
| [`../static/schema/v1/spec.schema.json`](../static/schema/v1/spec.schema.json) | A JSON Schema (draft 2020-12) describing the structure of `spec.json` itself, so a consumer can verify a document is a well-formed spec before trusting it. |
| [`fixtures.json`](fixtures.json) | Language-agnostic conformance cases — a list of branch names with their expected `valid` result and a reason. Any implementation can load these and assert against its own validator. |
| [`conformance.py`](conformance.py) | The reference check, run in CI. Standard library only. |

## Endpoints and stability

| URL | Guarantee |
|---|---|
| [`/spec.json`](https://conventionalbranch.org/spec.json) | **Latest.** Always the current version. Its content changes when a new version of the specification is released. |
| [`/v1.1.0/spec.json`](https://conventionalbranch.org/v1.1.0/spec.json) | **Permanent.** Frozen at publication and never modified. **Pin this** if a change in the spec should not silently change your tool's behavior. |
| [`/schema/v1/spec.schema.json`](https://conventionalbranch.org/schema/v1/spec.schema.json) | **Permanent.** Schema `v1` only ever gains optional properties; anything that would invalidate a document valid under `v1` ships as `v2` at a new URL. |

Concretely: a new specification version may add a type, extend the grammar, or
add a property to `spec.json`. It will not remove a property, rename one, or
change the meaning of an existing one — those are the changes that would be
published under a new schema version.

## What the check enforces

```bash
python3 tests/conformance.py
```

1. **Fixtures** — every case in `fixtures.json` matches `spec.json`'s regex.
2. **Docs table** — the valid/invalid examples table in `content/_index.md`
   agrees with the regex, so the documentation validates itself.
3. **Consistency** — the regex accepts every declared type/alias and trunk
   branch, and every AI agent prefix in `data/agents.yaml` is a declared type
   (guards against registry/spec drift).
4. **Badge** — the version rendered in `static/badge.svg` is the version
   `spec.json` declares, so the adoption badge cannot go stale.
5. **Schema** — `spec.json` and every frozen copy satisfy `schema/v1`.
6. **Versioning** — the version `spec.json` declares has a byte-identical
   frozen copy under `static/v<version>/`, so a release cannot ship without the
   permanent endpoint that downstream tools pin to.

The check exits non-zero on any disagreement and runs on every pull request via
[`.github/workflows/conformance.yml`](../.github/workflows/conformance.yml).

`conformance.py` has no dependencies, which means it carries a small JSON Schema
validator implementing exactly the keywords `spec.schema.json` uses. A keyword
it cannot evaluate fails the build rather than being skipped — a silently
ignored assertion is a check that has stopped checking.

## Using the spec in your own tooling

The regex in `spec.json` is anchored and implements the full ABNF grammar. Pin a
version so a future release cannot change how your tool behaves without you
choosing it:

```python
import json, re, urllib.request

SPEC = "https://conventionalbranch.org/v1.1.0/spec.json"  # pinned, never changes

spec = json.load(urllib.request.urlopen(SPEC))
valid = re.compile(spec["grammar"]["regex"])

print(bool(valid.fullmatch("feature/add-login-page")))  # True
print(bool(valid.fullmatch("Feature/Add-Login")))       # False
```

Better still, vendor the file. It is a few kilobytes, it is licensed CC BY 4.0,
and a copy in your repository is one less network call at validation time.

When you add support for the spec, please also run your validator against
`fixtures.json` so behavior stays consistent across implementations.

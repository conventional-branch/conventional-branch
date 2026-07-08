# Conformance tests

Machine-readable spec and test fixtures for the Conventional Branch specification.

## Files

| File | Purpose |
|---|---|
| [`../static/spec.json`](../static/spec.json) | The canonical machine-readable spec: types, aliases, trunk branches, rules, ABNF, and a single anchored **validation regex**. Served at [`conventionalbranch.org/spec.json`](https://conventionalbranch.org/spec.json). |
| [`fixtures.json`](fixtures.json) | Language-agnostic conformance cases — a list of branch names with their expected `valid` result and a reason. Any implementation can load these and assert against its own validator. |
| [`conformance.py`](conformance.py) | The reference check, run in CI. Standard library only. |

## What the check enforces

```
python3 tests/conformance.py
```

1. **Fixtures** — every case in `fixtures.json` matches `spec.json`'s regex.
2. **Docs table** — the valid/invalid examples table in `content/_index.md`
   agrees with the regex, so the documentation validates itself.
3. **Consistency** — the regex accepts every declared type/alias and trunk
   branch, and every AI agent prefix in `data/agents.yaml` is a declared type
   (guards against registry/spec drift).

The check exits non-zero on any disagreement and runs on every pull request via
[`.github/workflows/conformance.yml`](../.github/workflows/conformance.yml).

## Using the spec in your own tooling

The regex in `spec.json` is anchored and implements the full ABNF grammar:

```python
import json, re, urllib.request

spec = json.load(urllib.request.urlopen("https://conventionalbranch.org/spec.json"))
valid = re.compile(spec["grammar"]["regex"])

print(bool(valid.fullmatch("feature/add-login-page")))  # True
print(bool(valid.fullmatch("Feature/Add-Login")))       # False
```

When you add support for the spec, please also run your validator against
`fixtures.json` so behavior stays consistent across implementations.

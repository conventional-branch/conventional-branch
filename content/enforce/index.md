---
type: about
draft: false
seoTitle: "Enforce Git Branch Naming — Conventional Branch"
seoDescription: "Copy-pasteable branch name validation for GitHub rulesets, GitLab push rules, Bitbucket Pipelines and a dependency-free Git hook, using the published regex."
---

# Enforcing Conventional Branch

Copy-pasteable configuration for validating branch names against the specification.

Enforcement happens at two layers, and they solve different problems. A **server-side**
rule cannot be bypassed, but the contributor only finds out when they push. A **local**
check is instant and can be run before a branch exists, but anyone can skip it. Most
teams want one of each: the server rule is the contract, the local check is the
courtesy.

Every regular expression below is the one published in
[`spec.json`](https://conventionalbranch.org/spec.json), copied verbatim, and a
conformance check fails the build if this page and the specification ever disagree. The
expression is deliberately written in a portable subset — no backreferences, no
lookaround — so it compiles under RE2 as well as PCRE, which is what lets the same
string work in GitHub, GitLab, Python, JavaScript, and Go alike.

That check covers the expressions, not the prose. What each platform charges for, and
which of them can block a push rather than merely report one, is true as written but
verified by hand — if you find it out of date, please
[say so](https://github.com/conventional-branch/conventional-branch/issues).

It already permits `main`, `master` and `develop` unprefixed, so you do not need to
carve out exceptions for your trunk branches.

## GitHub

### Rulesets

A ruleset rejects a non-conforming branch outright, and on github.com it is the only
thing that does. The `branch_name_pattern` rule takes a regular expression directly.

```json
{
  "name": "Conventional Branch",
  "target": "branch",
  "enforcement": "active",
  "conditions": {
    "ref_name": {
      "include": ["~ALL"],
      "exclude": []
    }
  },
  "rules": [
    {
      "type": "branch_name_pattern",
      "parameters": {
        "name": "Branch names must follow the Conventional Branch specification",
        "negate": false,
        "operator": "regex",
        "pattern": "^(?:main|master|develop|(?:feature|feat|bugfix|fix|hotfix|release|chore|ai|copilot|cursor|claude|codex)/[a-z0-9]+(?:\\.[a-z0-9]+)*(?:-[a-z0-9]+(?:\\.[a-z0-9]+)*)*)$"
      }
    }
  ]
}
```

Save it as `conventional-branch.json` and import it under **Settings → Rules → Rulesets
→ New ruleset → Import a ruleset**, or apply it from the command line:

```bash
gh api repos/OWNER/REPO/rulesets --method POST --input conventional-branch.json
```

Start with `"enforcement": "evaluate"` to see what the rule would have rejected without
blocking anyone, then switch to `"active"`.

Rulesets are available on public repositories with every plan, and on private
repositories with GitHub Pro, Team, and Enterprise Cloud.

### GitHub Actions

A pull request check, for when a ruleset is not an option or you want the failure
explained in the PR:

```yaml
name: Branch name

on: pull_request

jobs:
  conventional-branch:
    runs-on: ubuntu-latest
    steps:
      - name: Validate the branch name
        env:
          BRANCH: ${{ github.head_ref }}
        run: |
          curl -sSfLo spec.json https://conventionalbranch.org/v1.1.0/spec.json
          python3 - <<'PY'
          import json, os, re, sys

          spec = json.load(open("spec.json"))
          branch = os.environ["BRANCH"]

          if re.fullmatch(spec["grammar"]["regex"], branch):
              print(f"{branch}: ok")
              sys.exit(0)

          types = ", ".join(f"{t['type']}/" for t in spec["types"])
          print(f"::error::'{branch}' does not follow the Conventional Branch "
                f"specification. Expected <type>/<description>, where type is one "
                f"of: {types}. See https://conventionalbranch.org/")
          sys.exit(1)
          PY
```

The URL is the version-pinned one on purpose: a future release of the specification
cannot change what your pipeline accepts until you choose to bump it.

## GitLab

Push rules reject the branch at `pre-receive`, before it reaches the server.

Under **Settings → Repository → Push rules → Branch name**, paste:

```text
^(?:main|master|develop|(?:feature|feat|bugfix|fix|hotfix|release|chore|ai|copilot|cursor|claude|codex)/[a-z0-9]+(?:\.[a-z0-9]+)*(?:-[a-z0-9]+(?:\.[a-z0-9]+)*)*)$
```

Three things worth knowing before you rely on it:

- **Push rules require GitLab Premium or Ultimate.** On the Free tier, use the CI job
  below instead.
- GitLab evaluates the expression in multiline mode. It makes no difference to a branch
  name, which cannot contain a newline, but if you ever extend the pattern you can turn
  it off with a leading `(?-m)`.
- Your default branch is always allowed, whether or not the pattern matches it.

For the Free tier, the same check as a CI job:

```yaml
conventional-branch:
  image: python:3-alpine
  rules:
    - if: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME
  script:
    - apk add --no-cache curl
    - curl -sSfLo spec.json https://conventionalbranch.org/v1.1.0/spec.json
    - |
      python3 -c '
      import json, os, re, sys
      spec = json.load(open("spec.json"))
      branch = os.environ["CI_MERGE_REQUEST_SOURCE_BRANCH_NAME"]
      if not re.fullmatch(spec["grammar"]["regex"], branch):
          sys.exit(f"{branch} does not follow https://conventionalbranch.org/")
      print(f"{branch}: ok")
      '
```

## Bitbucket

Bitbucket **Data Center** runs pre-receive hooks, so the rule can be enforced on the
server. Bitbucket **Cloud** does not run arbitrary server-side hooks — the check has to
live in Pipelines, which means it reports a failure rather than refusing the push.

```yaml
pipelines:
  pull-requests:
    '**':
      - step:
          name: Branch name
          image: python:3-alpine
          script:
            - apk add --no-cache curl
            - curl -sSfLo spec.json https://conventionalbranch.org/v1.1.0/spec.json
            - |
              python3 -c '
              import json, os, re, sys
              spec = json.load(open("spec.json"))
              branch = os.environ["BITBUCKET_BRANCH"]
              if not re.fullmatch(spec["grammar"]["regex"], branch):
                  sys.exit(f"{branch} does not follow https://conventionalbranch.org/")
              print(f"{branch}: ok")
              '
```

## Local checks

### A hook with no dependencies

`pre-push` is the last local moment where a bad branch name can still be caught,
and this needs nothing installed. Save this as `.git/hooks/pre-push` and make it
executable:

```bash
#!/bin/sh
# Reject a push from a branch that does not follow the Conventional Branch
# specification. https://conventionalbranch.org/

pattern='^(main|master|develop|(feature|feat|bugfix|fix|hotfix|release|chore|ai|copilot|cursor|claude|codex)/[a-z0-9]+(\.[a-z0-9]+)*(-[a-z0-9]+(\.[a-z0-9]+)*)*)$'
branch=$(git symbolic-ref --short HEAD)

if ! printf '%s' "$branch" | grep -qE "$pattern"; then
  echo "Branch '$branch' does not follow the Conventional Branch specification." >&2
  echo "Expected <type>/<description>, for example feature/add-login-page." >&2
  echo "See https://conventionalbranch.org/" >&2
  exit 1
fi
```

This is the only place on this page where the expression differs from `spec.json`, and
only in that the non-capturing groups `(?:` are written as plain `(`. POSIX `grep -E`
does not understand `(?:`, and `grep -P` is a GNU extension that macOS does not ship —
on a Mac it would fail to run and reject *every* branch. The conformance check verifies
that this form is the mechanical translation of the published expression and that it
accepts exactly the same branch names.

Git hooks are not copied by `git clone`. To share them with the team, commit the script
to the repository and point Git at it once:

```bash
git config core.hooksPath .githooks
```

### A branching alias

Enforcement tells people they are wrong. An alias makes it easier to be right:

```ini
[alias]
    feature = "!f() { git switch -c \"feature/$(printf '%s' \"$*\" | tr 'A-Z _' 'a-z--')\"; }; f"
    bugfix  = "!f() { git switch -c \"bugfix/$(printf '%s' \"$*\" | tr 'A-Z _' 'a-z--')\"; }; f"
    hotfix  = "!f() { git switch -c \"hotfix/$(printf '%s' \"$*\" | tr 'A-Z _' 'a-z--')\"; }; f"
    chore   = "!f() { git switch -c \"chore/$(printf '%s' \"$*\" | tr 'A-Z _' 'a-z--')\"; }; f"
```

```bash
git feature add login page   # creates and switches to feature/add-login-page
git feature Fix_Header       # creates and switches to feature/fix-header
```

The `tr` handles the three ways people usually get it wrong without noticing:
uppercase, underscores, and words typed with spaces instead of hyphens. It is a
convenience rather than a check — a description with other punctuation in it still
gets through, which is what the hook above is for.

## AI coding agents

Agents open pull requests now, which makes their branch names your branch names. Two
ways to teach them the convention.

### The agent skill

```bash
npx skills add conventional-branch/conventional-branch --skill conventional-branch
```

### A snippet for `AGENTS.md` or `CLAUDE.md`

Several projects on the [adopters list](https://conventionalbranch.org/about/#projects-using-conventional-branch)
already document the convention this way rather than for people. Paste it into whichever
instruction file your tooling reads:

```markdown
## Branch naming

Branch names follow the [Conventional Branch](https://conventionalbranch.org/)
specification: `<type>/<description>`, lowercase, hyphen-separated.

Types: `feature/` (or `feat/`), `bugfix/` (or `fix/`), `hotfix/`, `release/`, `chore/`.
`main`, `master` and `develop` take no prefix.

Examples: `feature/add-login-page`, `bugfix/fix-header-overflow`, `release/v1.2.0`.

When you create a branch yourself rather than at a person's direction, prefix it with
your own agent name instead — `claude/`, `codex/`, `copilot/`, `cursor/`, or the
vendor-neutral `ai/` — so the branch records who wrote it.
```

## Any other platform

The portable artifact is the regular expression, and the most reliable way to get it is
from the specification itself rather than by copying it out of a document:

```python
import json, re, urllib.request

SPEC = "https://conventionalbranch.org/v1.1.0/spec.json"  # pinned, never changes

spec = json.load(urllib.request.urlopen(SPEC))
valid = re.compile(spec["grammar"]["regex"])

print(bool(valid.fullmatch("feature/add-login-page")))  # True
```

If you are implementing validation in a tool, run it against
[`fixtures.json`](https://github.com/conventional-branch/conventional-branch/blob/main/tests/fixtures.json)
as well, so your behavior matches every other implementation.

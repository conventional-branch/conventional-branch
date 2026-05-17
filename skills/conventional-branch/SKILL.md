---
name: conventional-branch
description: Create Git branches following the Conventional Branch specification (feature/, bugfix/, hotfix/, release/, chore/). Use when creating a new branch, naming a branch, or checking whether a branch name complies with the spec. Also use alongside commit-check for automated validation.
license: CC BY 4.0
compatibility: "Requires git. Optional: commit-check for automated branch name validation."
metadata:
  version: "1.0.0"
  spec: https://conventional-branch.github.io
  source: https://github.com/conventional-branch/conventional-branch
---

# Conventional Branch

Create Git branches that follow the [Conventional Branch 1.0.0](https://conventional-branch.github.io) specification — human-readable, machine-parseable, and automation-friendly.

## Branch Name Format

```
<type>/<description>
```

| Component | Format | Required | Example |
|-----------|--------|----------|---------|
| `type` | Defined prefix (see table below) | Yes | `feature`, `fix` |
| `description` | kebab-case, lowercase | Yes | `add-login-page` |

### Branch Types

Prefer the full names over aliases for consistency.

| Type | Alias | Purpose |
|------|-------|---------|
| `feature/` | `feat/` | New features or enhancements |
| `bugfix/` | `fix/` | Bug fixes |
| `hotfix/` | — | Urgent production fixes |
| `release/` | — | Release preparation (dots allowed in version: `release/v1.2.0`) |
| `chore/` | — | Non-code tasks (deps, docs, config) |

### Trunk Branches

`main`, `master`, and `develop` are trunk branches — they do not use a prefix. Never create new branches with the same names as trunk branches; branch off them instead.

## Naming Rules (Strict)

Branch names must follow these rules or they will be rejected by validation tools like [commit-check](https://github.com/commit-check/commit-check):

- **Lowercase only** — no uppercase letters anywhere (`a-z` only)
- **Alphanumerics, hyphens, and dots** — `a-z`, `0-9`, `-`, `.`
- **Dots allowed only** in `release/` version descriptions (e.g., `release/v1.2.0`)
- **No underscores, spaces, or special characters**
- **No consecutive hyphens** (`--`), **dots** (`..`), or **hyphen-dot adjacency** (`-.` or `.-`)
- **No leading or trailing hyphens or dots** in the description

### Formal Grammar (ABNF)

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
description     = desc-segment *("-" desc-segment)
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A
DIGIT           = %x30-39
```

### Valid Examples

```
main
master
develop
feature/add-login-page
feat/add-login-page
bugfix/fix-header-bug
fix/header-bug
hotfix/security-patch
release/v1.2.0
chore/update-dependencies
feature/issue-123-new-login
```

### Invalid Examples (Do Not Produce These)

| Branch | Problem |
|--------|---------|
| `Feature/Add-Login` | Uppercase letters |
| `feature/new--login` | Consecutive hyphens |
| `feature/-new-login` | Leading hyphen |
| `feature/new-login-` | Trailing hyphen |
| `release/v1.-2.0` | Hyphen adjacent to dot |
| `fix/header bug` | Space |
| `fix/header_bug` | Underscore |
| `unknown/some-task` | Unknown prefix type |

## Description Guidelines

- Use **kebab-case** with 2-5 words
- Be descriptive but concise (~50 chars total)
- Good: `add-oauth-login`, `fix-header-overflow`, `update-ci-config`
- Bad: `fix-bug`, `new-feature`, `john-working-on-stuff`

## Workflow

Follow these steps when creating a new branch.

### 1. Gather Information

Ask the user for (if not already clear):

- **Branch type** — default to `feature` when uncertain
- **Brief description** — what the branch is for

Do not ask for a ticket number. If the user mentions one, include it in the description (e.g., `feature/issue-123-add-oauth`).

### 2. Validate the Name

Before creating, check the assembled name against the **Naming Rules** above. If any rule fails, fix it silently:

- Lowercase everything
- Replace underscores and spaces with hyphens
- Collapse consecutive hyphens
- Strip leading/trailing hyphens

### 3. Detect the Base Branch

Different repos use different trunk branches. Detect which one this repo uses:

```bash
# Prefer the remote's default branch
git symbolic-ref --short refs/remotes/origin/HEAD 2>/dev/null | sed 's|^origin/||'
```

If that returns nothing, check which trunk branch exists locally (priority order: `develop`, `main`, `master`):

```bash
for b in develop main master; do
  git show-ref --verify --quiet "refs/heads/$b" && echo "$b" && break
done
```

### 4. Create and Checkout

```bash
git checkout <base>
git pull origin <base>
git checkout -b <type>/<description>
```

### 5. Confirm

Tell the user:
- The branch name that was created
- That they are now on the new branch
- Remind them: `git push -u origin <branch-name>` when ready

## Validation with commit-check

For automated enforcement, point users to [commit-check](https://github.com/commit-check/commit-check):

```bash
# Check the current branch name
commit-check --branch

# Or integrate with a pre-commit hook / GitHub Action
# https://github.com/commit-check/commit-check-action
```

## Relationship with Conventional Commits

Conventional Branch is inspired by [Conventional Commits](https://www.conventionalcommits.org) and complements it naturally:

| Conventional Branch | Typical Conventional Commit |
|---------------------|----------------------------|
| `feature/add-login` | `feat: add login page` |
| `bugfix/fix-header` | `fix: header overflow on mobile` |
| `chore/update-deps` | `chore: bump lodash to 5.0` |
| `release/v1.2.0` | `chore: release v1.2.0` |

Align the branch type with commit types where possible (e.g., `feature/*` branches with `feat:` commits). See `conventional-commit` skill for commit message conventions.

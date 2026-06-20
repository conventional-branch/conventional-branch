---
draft: false
aliases: ["/en/"]
layout: single
---

# Conventional Branch 1.0.0

## Summary

Conventional Branch refers to a structured and standardized naming convention for Git branches which aims to make branch more readable and actionable. We've suggested some branch prefixes you might want to use but you can also specify your own naming convention. A consistent naming convention makes it easier to identify branches by type.

### Key Points

1. **Purpose-driven Branch Names**: Each branch name clearly indicates its purpose, making it easy for all developers to understand what the branch is for.
2. **Integration with CI/CD**: By using consistent branch names, it can help automated systems (like Continuous Integration/Continuous Deployment pipelines) to trigger specific actions based on the branch type (e.g., auto-deployment from release branches).
3. **Team Collaboration**: It encourages collaboration within teams by making branch purpose explicit, reducing misunderstandings, and making it easier for team members to switch between tasks without confusion.

## Specification

### Branch Naming Prefixes

The branch specification supports the following prefixes and should be structured as:

---

```text
<type>/<description>
```

- **`main`**: The main development branch (e.g., `main`, `master`, or `develop`)
- **`feature/`** (or **`feat/`**): For new features (e.g., `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (or **`fix/`**): For bug fixes (e.g., `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: For urgent fixes (e.g., `hotfix/security-patch`)
- **`release/`**: For branches preparing a release (e.g., `release/v1.2.0`)
- **`chore/`**: For non-code tasks like dependency, docs updates (e.g., `chore/update-dependencies`)

---

### Basic Rules

1. **Use Lowercase Alphanumerics, Hyphens, and Dots**: Always use lowercase letters (`a-z`), numbers (`0-9`), and hyphens (`-`) to separate words. Avoid special characters, underscores, or spaces. For release branches, dots (`.`) may be used in the description to represent version numbers (e.g., `release/v1.2.0`).
2. **No Consecutive, Leading, or Trailing Hyphens or Dots**: Ensure that hyphens and dots do not appear consecutively (e.g., `feature/new--login`, `release/v1.-2.0`), nor at the start or end of the description (e.g., `feature/-new-login`, `release/v1.2.0.`).
3. **Keep It Clear and Concise**: The branch name should be descriptive yet concise, clearly indicating the purpose of the work.
4. **Include Ticket Numbers**: If applicable, include the ticket number from your project management tool to make tracking easier. For example, for a ticket `issue-123`, the branch name could be `feature/issue-123-new-login`.

### AI Agent Prefixes (Optional)

> This is an **optional, opt-in extension**. Projects that do not enable it see no change in behavior, and every existing branch name remains valid.

AI coding agents increasingly create branches automatically, and several tools already namespace those branches with their own prefix:

| Agent | Prefix | Example |
|---|---|---|
| GitHub Copilot coding agent | `copilot/` | `copilot/add-theme-switcher` |
| Cursor (background / cloud agent) | `cursor/` | `cursor/refactor-cache-layer` |
| Devin | `devin/` | `devin/1712345678-fix-login` |
| Claude (community convention) | `claude/` | `claude/update-readme` |

To capture **who** created a branch (a human or a specific agent), an optional *actor* segment may lead the branch name, directly before the description:

```text
<actor>/<description>
```

For agent-created branches, the actor takes the place of the type segment: where a conventional branch reads `<type>/<description>`, an agent branch reads `<actor>/<description>`. This mirrors what agents emit in practice (e.g. `copilot/add-theme-switcher`) — the convention simply adapts the familiar `<type>/<description>` shape to record the author instead of the change kind.

Rules for the actor segment:

1. **Opt-in and declared**: A project must declare the actors it recognizes. Undeclared first segments remain invalid (so `unknown/some-task` is still rejected), which keeps the convention strict by default. With no actors configured, the specification behaves exactly as before.
2. **`human` is implicit**: Omitting the actor segment implies a human author; `human/` need not be written explicitly. Existing `<type>/<description>` names are therefore unchanged.
3. **Open, not hardcoded**: The specification defines the actor *mechanism* and offers a recommended list; it does not bake vendor names into the grammar. Projects declare their own set as new agents emerge.
4. **Same character rules**: An actor follows the same conventions as other segments — lowercase letters, digits, and internal hyphens.

A project might, for example, declare:

```yaml
actors:
  - human
  - copilot
  - cursor
  - claude
```

Other actors a project may choose to recognize include `devin`, `aider`, `codex`, and `jules`.

### Formal Grammar

The following Augmented Backus-Naur Form (ABNF) grammar formally defines valid branch names. The core grammar is `trunk-branch` and `prefixed-branch`. The `actor-branch` rule is the optional extension described in [AI Agent Prefixes](#ai-agent-prefixes-optional) and applies **only when a project declares actors**.

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
description     = desc-segment *("-" desc-segment)
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; lowercase a-z
DIGIT           = %x30-39   ; 0-9

; Optional extension — only when a project declares actors (see "AI Agent Prefixes"):
actor-branch    = actor "/" description
actor           = 1*(ALPHA / DIGIT) *("-" 1*(ALPHA / DIGIT))  ; a declared actor id
```

> Note: Consecutive hyphens or dots, and hyphens or dots at the start or end of the description, are not permitted. The `actor-branch` rule is an opt-in extension: an actor segment is recognized only when declared by the project (see [AI Agent Prefixes](#ai-agent-prefixes-optional)); undeclared prefixes remain invalid.

### Examples

| Branch Name | Valid | Notes |
|---|---|---|
| `main` | ✅ | Trunk branch |
| `master` | ✅ | Trunk branch |
| `develop` | ✅ | Trunk branch |
| `feature/add-login-page` | ✅ | New feature |
| `feat/add-login-page` | ✅ | Short alias for feature |
| `bugfix/fix-header-bug` | ✅ | Bug fix |
| `fix/header-bug` | ✅ | Short alias for bugfix |
| `hotfix/security-patch` | ✅ | Urgent fix |
| `release/v1.2.0` | ✅ | Release with version |
| `chore/update-dependencies` | ✅ | Non-code task |
| `feature/issue-123-new-login` | ✅ | Feature with ticket number |
| `copilot/add-theme-switcher` | ✅ | Optional actor + description (`copilot` declared) |
| `cursor/refactor-cache-layer` | ✅ | Optional actor + description (`cursor` declared) |
| `human/fix-header-bug` | ✅ | Explicit human actor (optional) |
| `Feature/Add-Login` | ❌ | Uppercase letters not allowed |
| `feature/new--login` | ❌ | Consecutive hyphens not allowed |
| `feature/-new-login` | ❌ | Leading hyphen in description |
| `feature/new-login-` | ❌ | Trailing hyphen in description |
| `release/v1.-2.0` | ❌ | Hyphen adjacent to dot |
| `fix/header bug` | ❌ | Spaces not allowed |
| `fix/header_bug` | ❌ | Underscores not allowed |
| `unknown/some-task` | ❌ | Unknown prefix: not a type, and not a declared actor |

## Conclusion

- **Clear Communication**: The branch name alone provides a clear understanding of its purpose the code change.
- **Automation-Friendly**: Easily hooks into automation processes (e.g., different workflows for `feature`, `release`, etc.).
- **Scalability**: Works well in large teams where many developers are working on different tasks simultaneously.

In summary, conventional branch is designed to improve project organization, communication, and automation within Git workflows.

## Tooling

{{< tooling compact >}}

## FAQ

### Why aren't branch types as detailed as Conventional Commits (e.g., `build`, `ci`, `docs`, `style`, `refactor`)?

Branches are different from commits—they are temporary and mainly used until merged. Introducing too many types for branches would be unnecessary and would make them harder to manage and remember.

### What tools can be used to automatically identify if a team member does not meet this specification?

You can use [commit-check](https://github.com/commit-check/commit-check) to check branch specification or [commit-check-action](https://github.com/commit-check/commit-check-action) if your codes are hosted on GitHub.

### Can I define my own branch types beyond the ones listed?

Yes. The specification defines a recommended set of types, but teams can define additional custom types to fit their workflow. It is important, however, to document custom types clearly so that all team members and automated tooling are aware of them.

### Should I use the optional AI agent actor prefix?

Only if your team wants to distinguish human-created branches from agent-created ones. The actor prefix is an opt-in extension: it is useful for traceability, auditing, and AI contribution metrics in workflows that mix human and AI-generated branches, but it adds no value—and should be left disabled—for teams that do not need it. When enabled, declare the exact set of actors you recognize so that unexpected prefixes are still flagged.

### How does Conventional Branch relate to Conventional Commits?

Conventional Branch is inspired by [Conventional Commits](https://www.conventionalcommits.org) and follows a similar philosophy: bring human- and machine-readable structure to Git metadata. While Conventional Commits standardizes commit messages, Conventional Branch standardizes branch names. The two specifications complement each other naturally.

### How should I handle long-lived branches like `develop` or `staging`?

Long-lived integration or environment branches that are part of the core specification (see the `trunk-branch` rule in the grammar) such as `main`, `master`, or `develop` are treated as trunk branches and do not require a prefix. Teams may additionally choose to treat other long-lived branches (for example, `staging` or `production`) as “trunk-like” branches by convention, but these are team-specific extensions outside the formal grammar. In all cases, such branches should be named consistently across your project.

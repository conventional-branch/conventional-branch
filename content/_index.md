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

```
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

### Formal Grammar

The following Augmented Backus-Naur Form (ABNF) grammar formally defines valid branch names:

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
```

> Note: Consecutive hyphens or dots, and hyphens or dots at the start or end of the description, are not permitted.

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
| `Feature/Add-Login` | ❌ | Uppercase letters not allowed |
| `feature/new--login` | ❌ | Consecutive hyphens not allowed |
| `feature/-new-login` | ❌ | Leading hyphen in description |
| `feature/new-login-` | ❌ | Trailing hyphen in description |
| `release/v1.-2.0` | ❌ | Hyphen adjacent to dot |
| `fix/header bug` | ❌ | Spaces not allowed |
| `fix/header_bug` | ❌ | Underscores not allowed |
| `unknown/some-task` | ❌ | Unknown prefix type |

## Conclusion

- **Clear Communication**: The branch name alone provides a clear understanding of its purpose the code change.
- **Automation-Friendly**: Easily hooks into automation processes (e.g., different workflows for `feature`, `release`, etc.).
- **Scalability**: Works well in large teams where many developers are working on different tasks simultaneously.

In summary, conventional branch is designed to improve project organization, communication, and automation within Git workflows.

## Tooling

Use these tools to adopt and enforce Conventional Branch in your project:

- [commit-check](https://github.com/commit-check/commit-check): Check branch names, commit messages, and related Git metadata locally.
- [commit-check-action](https://github.com/commit-check/commit-check-action): Validate branch names automatically in GitHub Actions.
- [VSCode Conventional Branch](https://marketplace.visualstudio.com/items?itemName=pshaddel.conventional-branch): Create Conventional Branch names from Visual Studio Code.
- [Conventional Branch Skill](https://github.com/conventional-branch/conventional-branch/blob/main/skills/conventional-branch/SKILL.md): Teach AI coding assistants how to create valid Conventional Branch names.

Install the skill with:

```bash
npx skills add conventional-branch/conventional-branch --skill conventional-branch
```

## FAQ

### Why aren't branch types as detailed as Conventional Commits (e.g., `build`, `ci`, `docs`, `style`, `refactor`)?

Branches are different from commits—they are temporary and mainly used until merged. Introducing too many types for branches would be unnecessary and would make them harder to manage and remember.

### What tools can be used to automatically identify if a team member does not meet this specification?

You can use [commit-check](https://github.com/commit-check/commit-check) to check branch specification or [commit-check-action](https://github.com/commit-check/commit-check-action) if your codes are hosted on GitHub.

### Can I define my own branch types beyond the ones listed?

Yes. The specification defines a recommended set of types, but teams can define additional custom types to fit their workflow. It is important, however, to document custom types clearly so that all team members and automated tooling are aware of them.

### How does Conventional Branch relate to Conventional Commits?

Conventional Branch is inspired by [Conventional Commits](https://www.conventionalcommits.org) and follows a similar philosophy: bring human- and machine-readable structure to Git metadata. While Conventional Commits standardizes commit messages, Conventional Branch standardizes branch names. The two specifications complement each other naturally.

### How should I handle long-lived branches like `develop` or `staging`?

Long-lived integration or environment branches that are part of the core specification (see the `trunk-branch` rule in the grammar) such as `main`, `master`, or `develop` are treated as trunk branches and do not require a prefix. Teams may additionally choose to treat other long-lived branches (for example, `staging` or `production`) as “trunk-like” branches by convention, but these are team-specific extensions outside the formal grammar. In all cases, such branches should be named consistently across your project.

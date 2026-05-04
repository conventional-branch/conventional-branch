# The Conventional Branch Specification

[![Conventional Branch](https://img.shields.io/badge/Conventional%20Branch-Spec-6192c3)](https://github.com/conventional-branch/conventional-branch)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fconventional-branch.github.io%2F&up_color=6192c3)](https://conventional-branch.github.io/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

The Conventional Branch specification defines a naming convention that brings order to your development workflow — whether you're working solo or with a team.

Inspired by [Conventional Commits](https://www.conventionalcommits.org), Conventional Branch standardizes Git branch names so they are human-readable, machine-parseable, and automation-friendly.

## 🚀 Quick Start

Branch names follow this structure:

```
<type>/<description>
```

| Type | Purpose | Example |
|---|---|---|
| `feature/` or `feat/` | New features | `feature/add-login-page` |
| `bugfix/` or `fix/` | Bug fixes | `fix/header-bug` |
| `hotfix/` | Urgent fixes | `hotfix/security-patch` |
| `release/` | Release preparation | `release/v1.2.0` |
| `chore/` | Non-code tasks | `chore/update-dependencies` |

Trunk branches (`main`, `master`, `develop`) do not require a prefix.

## 🌍 Multilingual Documentation

We currently support documentation in multiple languages:

[English](https://conventional-branch.github.io/) ·
[简体中文](https://conventional-branch.github.io/zh/) ·
[繁體中文](https://conventional-branch.github.io/zh-hant/) ·
[日本語](https://conventional-branch.github.io/ja/) ·
[Deutsch](https://conventional-branch.github.io/de/) ·
[Español](https://conventional-branch.github.io/es/) ·
[Français](https://conventional-branch.github.io/fr/) ·
[Polski](https://conventional-branch.github.io/pl/) ·
[Português (Brasil)](https://conventional-branch.github.io/pt-br/) ·
[Русский](https://conventional-branch.github.io/ru/) ·
[ภาษาไทย](https://conventional-branch.github.io/th/)

If your language is not listed, we welcome contributions to add it!

## 🔧 Tooling

Enforce the specification automatically in your project:

| Tool | Description |
|---|---|
| [commit-check](https://github.com/commit-check/commit-check) | CLI tool to check branch names, commit messages, and more |
| [commit-check-action](https://github.com/commit-check/commit-check-action) | GitHub Action for automated branch name validation |
| [VSCode Conventional Branch](https://marketplace.visualstudio.com/items?itemName=pshaddel.conventional-branch) | VSCode extension for branch name auto-completion |

## 🎉 Show Your Support

If you find this useful, consider giving it a ⭐️ on [GitHub](https://github.com/conventional-branch/conventional-branch)! Your support helps others discover and adopt the spec.

## 🛡 Badges!

Let others know your project follows the Conventional Branch spec. Add this badge to your repository README:

```markdown
[![Conventional Branch](https://img.shields.io/badge/Conventional%20Branch-Spec-6192c3)](https://github.com/conventional-branch/conventional-branch)
```

## 🤝 Contributing

We welcome contributions from the community!  
Whether it's fixing a typo, improving documentation, or proposing a new branch naming convention — please check out our [contributing guidelines](CONTRIBUTING.md).

No contribution is too small. Thank you for helping us grow! 💙

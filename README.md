# The Conventional Branch Specification

[![Conventional Branch](https://conventionalbranch.org/badge.svg)](https://conventionalbranch.org/)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fconventionalbranch.org%2F&up_color=6699CC)](https://conventionalbranch.org/)
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
| `ai/` | Generic AI agent prefix | `ai/refactor-auth-flow` |
| `copilot/` | GitHub Copilot | `copilot/add-login-page` |
| `cursor/` | Cursor | `cursor/fix-header-bug` |
| `claude/` | Claude Code by Anthropic | `claude/security-patch` |
| `codex/` | OpenAI Codex | `codex/optimize-query` |

Trunk branches (`main`, `master`, `develop`) do not require a prefix.

## 🌍 Multilingual Documentation

We currently support documentation in multiple languages:

[English](https://conventionalbranch.org/) ·
[简体中文](https://conventionalbranch.org/zh/) ·
[繁體中文](https://conventionalbranch.org/zh-hant/) ·
[日本語](https://conventionalbranch.org/ja/) ·
[Deutsch](https://conventionalbranch.org/de/) ·
[Español](https://conventionalbranch.org/es/) ·
[Français](https://conventionalbranch.org/fr/) ·
[Polski](https://conventionalbranch.org/pl/) ·
[Português (Brasil)](https://conventionalbranch.org/pt-br/) ·
[Русский](https://conventionalbranch.org/ru/) ·
[ภาษาไทย](https://conventionalbranch.org/th/)

If your language is not listed, we welcome contributions to add it!

## 🔧 Tooling

Enforce the specification automatically in your project:

| Tool | Description |
|---|---|
| [commit-check](https://github.com/commit-check/commit-check) | CLI tool to check branch names, commit messages, and more |
| [commit-check-action](https://github.com/commit-check/commit-check-action) | GitHub Action for automated branch name validation |
| [Conventional Branch Skill](skills/conventional-branch/SKILL.md) | Agent skill for AI coding assistants (Claude Code, Cursor, Pi, etc.) |

Install the skill to teach your AI agent how to create properly named branches:

```bash
npx skills add conventional-branch/conventional-branch --skill conventional-branch
```

## 🤖 Machine-Readable Spec

The specification is published in a machine-readable form so tools don't have to parse Markdown:

- **[`spec.json`](static/spec.json)** ([hosted](https://conventionalbranch.org/spec.json)) — types, aliases, trunk branches, rules, the ABNF grammar, and a single anchored **validation regex**.
- **[`tests/fixtures.json`](tests/fixtures.json)** — language-agnostic valid/invalid conformance cases any implementation can run against.

A [conformance test](tests/README.md) runs in CI and checks the fixtures, the examples table in the docs, and the agent registry all against `spec.json`, so they can't drift apart.

## 🏢 Used By

Projects and organizations adopting Conventional Branch, including [Ledger](https://github.com/LedgerHQ/ledger-live), [Sanity](https://github.com/sanity-io/sdk), [Ansible](https://github.com/ansible/metrics-utility), [Texas Instruments](https://github.com/TexasInstruments/processor-sdk-doc), and the [Government of British Columbia](https://github.com/bcgov/nr-pies). See the [full list](https://conventionalbranch.org/about/#projects-using-conventional-branch) and add your project via pull request.

## 🎉 Show Your Support

If you find this useful, consider giving it a ⭐️ on [GitHub](https://github.com/conventional-branch/conventional-branch)! Your support helps others discover and adopt the spec.

## 🛡 Badges!

Let others know your project follows the Conventional Branch spec. Pick whichever
of the two suits your README — they carry the same colors and version.

**Hosted** — includes the branch mark, and one short line to paste:

```markdown
[![Conventional Branch](https://conventionalbranch.org/badge.svg)](https://conventionalbranch.org/)
```

In HTML, for READMEs that aren't Markdown:

```html
<a href="https://conventionalbranch.org/">
  <img alt="Conventional Branch 1.1.0" src="https://conventionalbranch.org/badge.svg">
</a>
```

**[shields.io](https://shields.io)** — no mark, but you can restyle it:

```markdown
[![Conventional Branch](https://img.shields.io/badge/Conventional%20Branch-1.1.0-6699CC)](https://conventionalbranch.org/)
```

Append `&style=` to change the shape — `flat` (the default), `flat-square`,
`plastic` or `for-the-badge`.

`#6699CC` is the site's own `$color-primary`. The grey half is left on shields'
default so the badge sits comfortably next to the other badges in your README.

## 🤝 Contributing

We welcome contributions from the community!  
Whether it's fixing a typo, improving documentation, or proposing a new branch naming convention — please check out our [contributing guidelines](CONTRIBUTING.md).

No contribution is too small. Thank you for helping us grow! 💙

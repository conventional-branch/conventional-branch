# The Conventional Branch Specification

[![Conventional Branch](https://conventionalbranch.org/badge.svg)](https://conventionalbranch.org/)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fconventionalbranch.org%2F&up_color=6699CC)](https://conventionalbranch.org/)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**A specification for Git branch names that are human-readable, machine-parseable, and automation-friendly.**

Conventional Branch defines a small branch naming convention, `<type>/<description>`, in which every branch declares its own purpose. That turns a branch name into something your CI/CD pipelines, review policies, and tooling can act on directly, instead of a team habit that has to be explained to each new contributor and enforced by hand in code review.

The convention is published as a [machine-readable spec](#-machine-readable-spec) with conformance fixtures, so validating branch names is a solved problem for any tool that wants to support it. It is used by [LiteLLM](https://github.com/BerriAI/litellm/blob/main/CONTRIBUTING.md) and across the [Government of British Columbia](https://github.com/bcgov/nr-pies)'s natural resource services, and in projects at the UK's [GCHQ](https://github.com/gchq/Bailo/blob/main/AGENTS.md), [Oak Ridge National Laboratory](https://github.com/ORNLSlicer/ORNLSlicer/blob/develop/docs/contributing/conventional-branch.md) and [ByteDance](https://github.com/ByteDance-Seed/cryofm/blob/main/CONTRIBUTING.md), among [others](#-used-by).

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

- **[`spec.json`](static/spec.json)** — types, aliases, trunk branches, rules, the ABNF grammar, and a single anchored **validation regex**. Served two ways: [`/spec.json`](https://conventionalbranch.org/spec.json) always tracks the latest version, and [`/v1.1.0/spec.json`](https://conventionalbranch.org/v1.1.0/spec.json) is frozen at publication — **pin the versioned URL** so a future release can't change your tool's behavior without you choosing it.
- **[`schema/v1/spec.schema.json`](static/schema/v1/spec.schema.json)** ([hosted](https://conventionalbranch.org/schema/v1/spec.schema.json)) — a JSON Schema describing `spec.json`'s own structure, so you can verify a document is a well-formed spec before trusting it.
- **[`tests/fixtures.json`](tests/fixtures.json)** — language-agnostic valid/invalid conformance cases any implementation can run against.

A [conformance test](tests/README.md) runs in CI and checks the fixtures, the examples table in the docs, the agent registry, and every published spec document against `spec.json` and its schema, so they can't drift apart. The [stability guarantees](tests/README.md#endpoints-and-stability) for each endpoint are written down.

## ⚙️ Enforcing It

Copy-pasteable configuration for GitHub rulesets, GitLab push rules, Bitbucket
Pipelines, a dependency-free Git hook, branch-creation aliases, and a
snippet for `AGENTS.md` / `CLAUDE.md`, at
[conventionalbranch.org/enforce](https://conventionalbranch.org/enforce/). Every regex on
that page is the one in `spec.json`, enforced by the conformance check, so a config
copied from it cannot drift from the specification.

## 🏢 Used By

Alongside the organizations named above, Conventional Branch is adopted by [Texas Instruments](https://github.com/TexasInstruments/processor-sdk-doc), [Ansible](https://github.com/ansible/metrics-utility), [Sanity](https://github.com/sanity-io/sdk), Portugal's state technology agency [ARTE](https://github.com/amagovpt/udata-pt), and [Enedis](https://github.com/Enedis-OSS/tic4eebus), France's largest electricity distributor. See the [full list](https://conventionalbranch.org/about/#projects-using-conventional-branch) and add your project via pull request.

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

## 📄 License and Attribution

Conventional Branch is licensed under [CC BY 4.0](LICENSE).

The specification was derived from [Conventional Commits](https://www.conventionalcommits.org), which is licensed under the same terms. It applies the same idea — human- and machine-readable structure in Git metadata — to branch names rather than commit messages, and the two specifications are designed to be used together. See [NOTICE](NOTICE) for the full attribution, and the [FAQ](https://conventionalbranch.org/#how-does-conventional-branch-relate-to-conventional-commits) for how they relate.

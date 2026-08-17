# Changelog

All notable changes to the Conventional Branch specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

The version number tracks the specification itself; site and tooling changes are listed under the version they serve.

## [1.1.0] - 2026-07-08

### Added
- **AI Agent Source Prefixes**: `ai/`, `copilot/`, `cursor/`, `claude/`, `codex/` — grammar, examples, and FAQ updated to match.
- **Agent prefix registry** ([`data/agents.yaml`](https://github.com/conventional-branch/conventional-branch/blob/main/data/agents.yaml)), with a documented process for registering new prefixes.
- **Machine-readable spec**: [`/spec.json`](https://conventionalbranch.org/spec.json) — types, rules, grammar, and a validation regex, with conformance fixtures for implementers.
- Version switcher on the website.
- **Frozen spec endpoint** (2026-08): [`/v1.1.0/spec.json`](https://conventionalbranch.org/v1.1.0/spec.json) never changes after publication — pin it in tooling.
- **JSON Schema for the spec** (2026-08): [`/schema/v1/spec.schema.json`](https://conventionalbranch.org/schema/v1/spec.schema.json).
- **Enforcement page** (2026-08): [/enforce](https://conventionalbranch.org/enforce/) — copy-pasteable configs for GitHub, GitLab, Bitbucket, Git hooks, and AI coding agents.
- **`llms.txt`** (2026-08): [/llms.txt](https://conventionalbranch.org/llms.txt), the spec summarized for AI assistants.
- **Adoption badge** (2026-08): [`/badge.svg`](https://conventionalbranch.org/badge.svg), self-hosted, always showing the current version.

### Removed
- VSCode Conventional Branch extension delisted from tooling (2026-08).

## [1.0.0] - 2026-06-20

### Added
- Initial release of the Conventional Branch specification.
- Defined branch types: `main`/`master`/`develop`, `feature`/`feat`, `bugfix`/`fix`, `hotfix`, `release`, `chore`.
- Basic naming rules: lowercase, hyphens, and dots for version numbers.
- Formal ABNF grammar definition for branch name validation.
- Valid/invalid examples table in all supported languages.
- Extended FAQ covering custom branch types, relation to Conventional Commits, long-lived branches, and tool integration.

### Languages
- **Simplified Chinese** (2024-09)
- **Brazilian Portuguese** (2025-07)
- **French**, **Japanese**, **German**, **Russian**, **Polish** (2025-09)
- **Traditional Chinese** (2026-02)
- **Spanish** (2026-03)
- **Thai** (2026-05)

### Changed
- Naming rules combined and revised for clarity (2025-03).
- Branch naming specification further refined (2025-09).
- License updated from MIT to **CC-BY-4.0** (2025-12).
- Specification established as industry-standard with dedicated website at [conventionalbranch.org](https://conventionalbranch.org) (2026-04).
- Versioned content structure with version switcher UI for browsing spec versions (2026-06).

[1.1.0]: https://github.com/conventional-branch/conventional-branch/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/conventional-branch/conventional-branch/releases/tag/v1.0.0

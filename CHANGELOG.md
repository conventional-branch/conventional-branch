# Changelog

All notable changes to the Conventional Branch specification will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- **Permanent spec endpoint**: the machine-readable spec is now served both at [`/spec.json`](https://conventionalbranch.org/spec.json) (always the latest version) and at [`/v1.1.0/spec.json`](https://conventionalbranch.org/v1.1.0/spec.json), frozen at publication. Downstream tools can pin the versioned URL so a future release cannot change their behavior unannounced.
- **JSON Schema for `spec.json`**: [`/schema/v1/spec.schema.json`](https://conventionalbranch.org/schema/v1/spec.schema.json) describes the structure of the spec document itself, with written stability guarantees for each endpoint. `spec.json` now carries a `$schema` key.
- Two conformance checks covering the above: every published spec document is validated against the schema, and a release cannot ship without a byte-identical frozen copy of the version it declares.

## [1.1.0] - 2026-07-08

### Added
- **AI Agent Source Prefixes**: `ai/`, `copilot/`, `cursor/`, `claude/`, `codex/` for identifying AI-generated branches.
- FAQ entry explaining the rationale for AI agent source prefixes.
- Updated ABNF grammar to include AI agent source types.
- Updated examples table with AI agent branch name examples.
- Version switcher UI on the specification website.
- **AI agent prefix registry**: a machine-readable `data/agents.yaml` rendered as a table across all languages, with a documented process for registering new agent prefixes.
- **Machine-readable specification**: `spec.json` (types, aliases, rules, ABNF grammar, and a validation regex) served at [conventionalbranch.org/spec.json](https://conventionalbranch.org/spec.json), plus language-agnostic conformance fixtures and a CI check that keeps the spec, docs, and registry in sync.

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

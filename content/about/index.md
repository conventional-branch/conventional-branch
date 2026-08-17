---
type: about
draft: false
seoTitle: "AI Agent Branch Prefixes — Conventional Branch"
seoDescription: "The registry of AI coding agent branch prefixes — ai/, claude/, codex/, copilot/, cursor/ — with tooling, CI/CD patterns and the projects using the specification."
---

# About

The Conventional Branch specification was inspired by [Conventional Commits](https://www.conventionalcommits.org).

## AI Agent Source Prefixes

As AI coding agents increasingly open their own pull requests, Conventional Branch maintains a registry of their branch prefixes so tools and teams can recognize them consistently. This registry is the machine-readable source of truth — the table below is generated from [`data/agents.yaml`](https://github.com/conventional-branch/conventional-branch/blob/main/data/agents.yaml).

{{< agents >}}

Giving each agent a documented prefix (or using the vendor-neutral `ai/`) lets teams do more than just eyeball who opened a PR:

- **Apply review policy by source** — require an extra human approval on agent-generated branches, or auto-assign a reviewer to them.
- **Route CI differently** — run a heavier security, license, or lint suite on `ai/`, `copilot/`, `claude/`, … branches before they reach a human reviewer.
- **Attribute activity and cost** — measure how much work each agent produces by filtering branches and PRs on their prefix.
- **Automate housekeeping** — auto-label PRs, apply branch-protection rules, or trigger notifications based on the prefix.

Building an agent that opens PRs? [Register its prefix](https://github.com/conventional-branch/conventional-branch/blob/main/CONTRIBUTING.md#registering-a-new-ai-agent-prefix) so reviewers and tooling recognize it out of the box.

## Tooling for Conventional Branch

{{< tooling full >}}

## Projects Using Conventional Branch

Roughly ordered by how widely recognized the organization is, so the list is useful
to skim.

* [gchq/Bailo](https://github.com/gchq/Bailo/blob/main/AGENTS.md): Machine learning lifecycle management, by GCHQ, the UK's intelligence, security and cyber agency.
* [ORNLSlicer/ORNLSlicer](https://github.com/ORNLSlicer/ORNLSlicer/blob/develop/docs/contributing/conventional-branch.md): Toolpath planning and slicing for additive manufacturing, developed at Oak Ridge National Laboratory.
* [ByteDance-Seed/cryofm](https://github.com/ByteDance-Seed/cryofm/blob/main/CONTRIBUTING.md): Generative foundation model for cryo-EM density maps, by ByteDance Seed.
* [bcgov/nr-pies](https://github.com/bcgov/nr-pies): Natural Resource Permitting Information Exchange by the Government of British Columbia.
* [amagovpt/udata-pt](https://github.com/amagovpt/udata-pt/blob/main/CLAUDE.md): Portugal's open data platform, by ARTE, the state agency for technological reform.
* [TexasInstruments/processor-sdk-doc](https://github.com/TexasInstruments/processor-sdk-doc): Texas Instruments Processor SDK documentation.
* [Enedis-OSS/tic4eebus](https://github.com/Enedis-OSS/tic4eebus/blob/main/CONTRIBUTING.md): EEBUS OPEV use case by Enedis, France's largest electricity distributor.
* [BerriAI/litellm](https://github.com/BerriAI/litellm/blob/main/CONTRIBUTING.md): A high-performance LLM proxy supporting 100+ models with spending tracking and guardrails.
* [ansible/metrics-utility](https://github.com/ansible/metrics-utility/blob/devel/docs/CONTRIBUTING.md): Standalone utility for github.com/ansible/awx.
* [sanity-io/sdk](https://github.com/sanity-io/sdk/blob/main/CONTRIBUTING.md): Sanity App SDK.
* [cuga-project/cuga-agent](https://github.com/cuga-project/cuga-agent/blob/main/CONTRIBUTING.md): CUGA, an open-source generalist agent harness for the enterprise.
* [TailGrids/tailgrids](https://github.com/TailGrids/tailgrids/blob/main/CONTRIBUTING.md): Open-source React UI library built with Tailwind CSS.
* [lightonai/lighton-python-sdk](https://github.com/lightonai/lighton-python-sdk/blob/main/CONTRIBUTING.md): Python SDK for the LightOn API.
* [ippontech/iroco2](https://github.com/ippontech/iroco2/blob/main/contribute/CONTRIBUTING.md): IroCO2, a tool for estimating and reducing the carbon footprint of cloud infrastructure, by Ippon Technologies.
* [Technica-Engineering/FLYNC](https://github.com/Technica-Engineering/FLYNC/blob/main/CONTRIBUTING.md): Flexible YAML-based vehicle network configuration, by Technica Engineering.
* [stellio-hub/stellio-context-broker](https://github.com/stellio-hub/stellio-context-broker/blob/develop/docs/contributing/development_guide.md): Stellio, an NGSI-LD compatible context broker.
* [Curiosum](https://github.com/curiosum-dev): Building apps for innovators.
* [ZeusAutomacao/DFe.NET](https://github.com/ZeusAutomacao/DFe.NET): Biblioteca em C# para emissão e impressão de NFe, NFCe, MDF-e e CT-e.
* [commit-check](https://github.com/commit-check): A free, powerful tool that enforces commit metadata, branch naming, and more.
* [fau-advanced-separations/CADET-Process](https://github.com/fau-advanced-separations/CADET-Process/blob/dev/CONTRIBUTING.md): A framework for modelling and optimizing advanced chromatographic processes, by Advanced Separations @ FAU.
* [devsoc-unsw/structs.sh](https://github.com/devsoc-unsw/structs.sh/blob/dev/docs/docs/contributing.md): An educational data structures and algorithms platform, by the UNSW Software Development Society.
* [CSES-Open-Source/TritonScript](https://github.com/CSES-Open-Source/TritonScript/blob/main/CONTRIBUTING.md): Open source project by the Computer Science and Engineering Society at UC San Diego.
* [RLinf/RLinf](https://github.com/RLinf/RLinf): Reinforcement Learning Infrastructure for Agentic AI.
* [soma-smart/framefox](https://github.com/soma-smart/framefox/blob/main/CONTRIBUTING.md): Python web framework built on FastAPI, MVC and SQLModel.
* [keyteki/keyteki](https://github.com/keyteki/keyteki/blob/master/AGENTS.md): The engine behind The Crucible Online, for playing KeyForge in the browser.
* [karol-broda/snitch](https://github.com/karol-broda/snitch/blob/master/CONTRIBUTING.md): A prettier way to inspect network connections.
* [jal-co/shieldcn](https://github.com/jal-co/shieldcn): Beautiful README badges inspired by shadcn/ui.
* [dunossauro/fastapi-do-zero](https://github.com/dunossauro/fastapi-do-zero/blob/main/aulas/contribua/contribua.md): Curso básico de FastAPI em português.
* _[... and more projects using Conventional Branch](https://github.com/search?q=conventional-branch.github.io&type=code&p=1)._

[![Conventional Branch](https://conventionalbranch.org/badge.svg)](https://conventionalbranch.org/)

_Want your project on this list?_ [Send a pull request](https://github.com/conventional-branch/conventional-branch/pulls).

## CI/CD Integration

Because the branch name already encodes its purpose, CI/CD pipelines can key their behavior off the prefix directly, without any extra metadata or configuration lookup. In GitHub Actions, that means an `if: startsWith(...)` condition per job:

```yaml
jobs:
  test:
    if: startsWith(github.head_ref, 'feature/') || startsWith(github.head_ref, 'bugfix/')
    runs-on: ubuntu-latest
    steps:
      - run: npm test

  security-review:
    if: startsWith(github.head_ref, 'hotfix/')
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/security-scan.sh

  release-candidate:
    if: startsWith(github.head_ref, 'release/')
    runs-on: ubuntu-latest
    steps:
      - run: ./scripts/build-release-candidate.sh
```

A common mapping of prefixes to pipeline behavior:

| Branch prefix | Typical CI/CD behavior |
|---|---|
| `feature/*` | Run the full test suite; deploy a preview environment |
| `bugfix/*` | Run regression tests |
| `hotfix/*` | Require a security scan or extra approval before merge |
| `release/*` | Trigger the release-candidate pipeline; deploy to staging |
| `chore/*` | Skip preview deployment |

Other CI/CD platforms support the same pattern using their own equivalent of a branch-name condition (e.g., GitLab CI's `rules: - if:`, or a shell check against `$CI_COMMIT_REF_NAME`). Conventional Branch only standardizes the branch name — the mapping above is a starting point to adapt to your own pipeline.

## How to Adopt

1. **Communicate the convention** to your team and add it to your contributing guidelines.
2. **Enforce it automatically** using one of the tools listed above.
3. **Add the badge** to your repository README to signal adoption:

   [![Conventional Branch](https://conventionalbranch.org/badge.svg)](https://conventionalbranch.org/)

   ```markdown
   [![Conventional Branch](https://conventionalbranch.org/badge.svg)](https://conventionalbranch.org/)
   ```

   Or in HTML:

   ```html
   <a href="https://conventionalbranch.org/">
     <img alt="Conventional Branch 1.1.0" src="https://conventionalbranch.org/badge.svg">
   </a>
   ```

   Prefer to generate it yourself, or want a different shape? The
   [shields.io](https://shields.io) equivalent carries the same colors and
   version, and takes `&style=flat-square`, `&style=plastic` or
   `&style=for-the-badge`:

   ```markdown
   [![Conventional Branch](https://img.shields.io/badge/Conventional%20Branch-1.1.0-6699CC)](https://conventionalbranch.org/)
   ```

4. **Configure your CI/CD** to trigger different workflows based on branch prefix (e.g., auto-deploy on `release/` branches) — see [CI/CD Integration](#cicd-integration) above.

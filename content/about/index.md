---
type: about
draft: false
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

* [BerriAI/litellm](https://github.com/BerriAI/litellm/blob/main/CONTRIBUTING.md): A high-performance LLM proxy supporting 100+ models with spending tracking and guardrails.
* [karol-broda/snitch](https://github.com/karol-broda/snitch/blob/master/CONTRIBUTING.md): A prettier way to inspect network connections.
* [ansible/metrics-utility](https://github.com/ansible/metrics-utility/blob/devel/docs/CONTRIBUTING.md): Standalone utility for github.com/ansible/awx.
* [sanity-io/sdk](https://github.com/sanity-io/sdk/blob/main/CONTRIBUTING.md): Sanity App SDK.
* [TexasInstruments/processor-sdk-doc](https://github.com/TexasInstruments/processor-sdk-doc): Texas Instruments Processor SDK documentation.
* [dunossauro/fastapi-do-zero](https://github.com/dunossauro/fastapi-do-zero/blob/main/aulas/contribua/contribua.md): Curso básico de FastAPI em português.
* [Enedis-OSS/tic4eebus](https://github.com/Enedis-OSS/tic4eebus/blob/main/CONTRIBUTING.md): EEBUS OPEV use case by Enedis, France's largest electricity distributor.
* [bcgov/nr-pies](https://github.com/bcgov/nr-pies): Natural Resource Permitting Information Exchange by the Government of British Columbia.
* [commit-check](https://github.com/commit-check): A free, powerful tool that enforces commit metadata, branch naming, and more.
* [ZeusAutomacao/DFe.NET](https://github.com/ZeusAutomacao/DFe.NET): Biblioteca em C# para emissão e impressão de NFe, NFCe, MDF-e e CT-e.
* [RLinf/RLinf](https://github.com/RLinf/RLinf): Reinforcement Learning Infrastructure for Agentic AI.
* [Curiosum](https://github.com/curiosum-dev): Building apps for innovators.
* [jal-co/shieldcn](https://github.com/jal-co/shieldcn): Beautiful README badges inspired by shadcn/ui.
* [LedgerHQ/ledger-live](https://github.com/LedgerHQ/ledger-live/blob/main/CONTRIBUTING.md): Mono-repository for packages related to Ledger Live and its JavaScript ecosystem.
* _[... and more projects using Conventional Branch](https://github.com/search?q=conventional-branch.github.io&type=code&p=1)._

[![Conventional Branch](https://img.shields.io/badge/Conventional%20Branch-Spec-6192c3)](https://github.com/conventional-branch/conventional-branch)

_Want your project on this list?_ [Send a pull request](https://github.com/conventional-branch/conventional-branch/pulls).

## How to Adopt

1. **Communicate the convention** to your team and add it to your contributing guidelines.
2. **Enforce it automatically** using one of the tools listed above.
3. **Add the badge** to your repository README to signal adoption.
4. **Configure your CI/CD** to trigger different workflows based on branch prefix (e.g., auto-deploy on `release/` branches).

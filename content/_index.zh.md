---
draft: false
aliases: ["/zh/"]
layout: single
seoTitle: "Git 分支命名规范 — 约定式分支 Conventional Branch"
seoDescription: "Git 分支命名规范：feature/、bugfix/、hotfix/、release/、chore/ 等分支前缀，附正式语法，以及在 GitHub、GitLab 中强制校验的方法。"
---

# 约定式分支 1.2.0

## 概述

约定式分支是指 Git 分支的结构化和标准化命名约定，旨在使分支更具可读性和可操作性。我们建议了一些您可能想要使用的分支前缀，但您也可以指定自己的命名约定。一致的命名约定使按类型识别分支变得更加容易。

### 要点

1. **以目的为导向的分支名称**：每个分支名称都清楚地表明了其目的，使所有开发人员都能轻松了解该分支的用途。
2. **与 CI/CD 集成**：通过使用一致的分支名称，它可以帮助自动化系统（如持续集成/持续部署管道）根据分支类型触发特定操作（例如，从发布分支自动部署）。
3. **团队协作**：它通过明确分支目的来鼓励团队内部的协作，减少误解并使团队成员更容易在任务之间切换而不会产生混淆。

## 规范

### 分支命名前缀

分支规范支持以下前缀，其结构应如下：

---

```
<type>/<description>
```

**用途前缀（Purpose Prefixes）** — 描述工作的意图：
- **`feature/`** (或 **`feat/`**)：用于新功能（例如 `feature/add-login-page`, `feat/add-login-page`）
- **`bugfix/`** (或 **`fix/`**)：用于错误修复（例如 `bugfix/fix-header-bug`, `fix/header-bug`）
- **`hotfix/`**：用于紧急修复（例如 `hotfix/security-patch`）
- **`release/`**：用于准备发布的分支（例如 `release/v1.2.0`）
- **`chore/`**：用于非代码任务，如依赖项、文档更新（例如 `chore/update-dependencies`）

**AI 智能体源前缀（AI Agent Source Prefixes）** — 识别由 AI 编码智能体生成的分支：
{{< agents >}}

该列表已冻结：没有专属前缀的智能体使用 `ai/`。

主干分支（`main`、`master`、`develop`）不使用前缀。

---

### 基本规则

1. **使用小写字母、数字、连字符和点**：分支名称应全部使用小写字母 (`a-z`)、数字 (`0-9`) 及连字符 (`-`) 进行分隔。避免使用特殊字符、下划线或空格。任何分支的描述中都可以使用点 (`.`)，通常用于表示版本号（例如 `release/v1.2.0`、`chore/upgrade-node-v20.11`）。 小写规则的唯一例外是描述开头的工单编号（见第 4 条）。
2. **禁止连续、开头或结尾的连字符或点**：确保连字符和点不能连续出现（例如 `feature/new--login`, `release/v1.-2.0`），也不能出现在描述的开头或结尾（例如 `feature/-new-login`, `release/v1.2.0.`）。
3. **保持清晰简洁**：分支名称应简明扼要，清楚表达工作的内容和目的。
4. **包含工单编号**：如果适用，应包含项目管理工具中的工单编号，以便于追踪。例如，对于工单 `issue-123`，分支名称可以是 `feature/issue-123-new-login`。 工单编号位于描述开头时，可以保留项目管理工具中的大写形式，例如 `feature/PROJ-123-new-login`；描述的其余部分仍须小写。

### 形式文法

以下 ABNF（扩充巴科斯-诺尔范式）文法正式定义了有效的分支名称：

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
                / "ai" / "agents" / "copilot" / "cursor"
                / "claude" / "codex"
description     = (ticket-key / desc-segment) *("-" desc-segment)
ticket-key      = UPPER *(UPPER / DIGIT) "-" 1*DIGIT
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; 小写字母 a-z
UPPER           = %x41-5A   ; 大写字母 A-Z，仅用于工单编号
DIGIT           = %x30-39   ; 数字 0-9
```

> 注意：禁止连续的连字符或点，以及出现在描述开头或结尾的连字符或点。

### 示例

| 分支名称 | 有效 | 说明 |
|---|---|---|
| `main` | ✅ | 主干分支 |
| `master` | ✅ | 主干分支 |
| `develop` | ✅ | 主干分支 |
| `feature/add-login-page` | ✅ | 新功能 |
| `feat/add-login-page` | ✅ | feature 的简写形式 |
| `bugfix/fix-header-bug` | ✅ | 错误修复 |
| `fix/header-bug` | ✅ | bugfix 的简写形式 |
| `hotfix/security-patch` | ✅ | 紧急修复 |
| `release/v1.2.0` | ✅ | 含版本号的发布分支 |
| `chore/upgrade-node-v20.11` | ✅ | 非 release 分支中的点 |
| `chore/update-dependencies` | ✅ | 非代码任务 |
| `feature/issue-123-new-login` | ✅ | 含工单编号的功能分支 |
| `feature/PROJ-123-new-login` | ✅ | 描述开头的大写工单编号 |
| `release/PROJ-1234` | ✅ | 描述仅为工单编号 |
| `Feature/Add-Login` | ❌ | 不允许大写字母 |
| `feature/new-login-PROJ-123` | ❌ | 工单编号必须位于描述开头 |
| `feature/Proj-123-new-login` | ❌ | 工单编号必须全部大写 |
| `feature/new--login` | ❌ | 不允许连续连字符 |
| `feature/-new-login` | ❌ | 描述不能以连字符开头 |
| `feature/new-login-` | ❌ | 描述不能以连字符结尾 |
| `release/v1.-2.0` | ❌ | 连字符不能紧邻点号 |
| `fix/header bug` | ❌ | 不允许空格 |
| `fix/header_bug` | ❌ | 不允许下划线 |
| `ai/refactor-auth-flow` | ✅ | 通用 AI 编码智能体前缀 |
| `agents/add-dark-mode-toggle` | ✅ | `ai/` 的别名（VS Code Agents 窗口） |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Anthropic Claude Code |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | 未知的前缀类型 |

## 结论

- **清晰的沟通**：仅凭分支名称就能清楚地了解代码更改的目的。
- **自动化友好**：轻松挂接自动化流程（例如，针对 `feature`, `release` 等的不同工作流程）。
- **可扩展性**：适用于许多开发人员同时处理不同任务的大型团队。

总之，约定式分支旨在改善 Git 工作流程中的项目组织、沟通和自动化。

## 工具

{{< tooling compact >}}

## 常见问题

### 约定式分支与约定式提交（Conventional Commits）有什么关系？

约定式分支的灵感来源于 [Conventional Commits](https://www.conventionalcommits.org)，遵循相似的理念：为 Git 元数据引入人机可读的结构。约定式提交规范化了提交信息，约定式分支规范化了分支名称。两者相辅相成，天然互补。

### 约定式分支发明了这些前缀吗？

没有。`feature/`、`hotfix/`、`release/` 这类前缀在 2010 年前后由 [git-flow](https://github.com/nvie/gitflow) 工具推广开来，也是 [Bitbucket 分支模型](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/)等工具的默认值。约定式分支建立在这一实践之上，而不是要取代它。它补充的是一份人和工具都能共用的精确定义：固定的类型集合、形式文法、发布在 [`spec.json`](/spec.json) 中的校验正则，以及一致性测试用例，让每个校验工具接受的名称完全相同。

### 为什么分支类型不像 Conventional Commits（例如 `build`、`ci`、`docs`、`style`、`refactor`）那么详细？

分支与提交不同 —— 分支是临时的，大部分只出现在合并前。为分支引入过多类型是没有必要的，也会让管理和记忆变得更困难。

### 我可以定义规范列表之外的自定义分支类型吗？

可以，作为团队层面的扩展。文法中列出的类型是所有符合规范的工具都会接受的类型，因此像 `unknown/some-task` 这样的分支按规范本身是无效的。如果团队需要更多类型（例如 `experiment/`），应在校验工具中显式列出它们（例如 [commit-check](/enforce/#commit-check) 的 `allow_branch_types`），并写进文档，让团队成员和自动化工具保持一致。例如，本规范自己的仓库就在 [commit-check 配置](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml)中为 Dependabot 创建的分支添加了 `dependabot/`。

### 为什么分支名称必须小写？

有两个原因。第一，Git 通常把分支引用存成 `.git/refs/heads/` 下的文件，而 macOS 和 Windows 默认的文件系统不区分大小写：`Feature/login` 和 `feature/login` 在这些机器上指向同一个路径，在 Linux 上却是两个不同的分支，所以同时允许两种写法的仓库，在不同克隆中的行为可能不一致。第二，只有一种写法更容易输入、搜索和匹配：按 `release/*` 触发的工具不必再考虑 `Release/*`。

从 v1.2.0 起有一个例外：位于描述开头的工单编号（例如 `PROJ-123`）可以保留 Jira 等工具显示的大写形式。请完全按照工具中的写法书写工单编号，避免同一仓库中同时出现以 `PROJ-123` 和 `proj-123` 命名的分支。

### v1.2.0 与 v1.1.0 的主要区别是什么？

v1.2.0 允许描述以大写工单编号开头，例如 `feature/PROJ-123-new-login`，这在 v1.1.0 中是无效的。它还冻结了 AI 智能体源前缀列表：今后不再添加新的厂商前缀，五个前缀之外的智能体统一使用 `ai/`。所有在 v1.1.0 下有效的分支名称依然有效，没有破坏性变更。

### v1.1.0 与 v1.0.0 的主要区别是什么？

v1.1.0 的主要新特性是引入了 **AI 智能体源前缀（AI Agent Source Prefixes）**（具体原因见下一条常见问题）。同时，版本化网站增加了版本切换器，用户可以浏览 v1.0.0 和 v1.1.0 两种规范。所有现有的 v1.0.0 分支名称仍然完全有效 —— 没有不兼容的变更。

### 为什么要添加 AI 智能体源前缀（AI Agent Source Prefixes）？

AI 编码智能体（GitHub Copilot、Cursor、Claude Code、OpenAI Codex 等）越来越多地被用于生成代码和创建 Pull Request。每个智能体都使用自己的分支前缀（例如 `copilot/`、`cursor/`）。通过在约定式分支规范中标准化这些前缀，我们可以实现：
1. **快速识别** — 审查者和工具可以立即识别 AI 生成的 PR
2. **工具验证** — 诸如 commit-check 之类的工具可以验证 AI 智能体分支是否符合规范
3. **稳定的列表** — 自 v1.2.0 起这五个前缀固定不变，其他智能体使用 `ai/`，文法不会因为新工具的出现而改动

`ai/` 通用前缀适用于没有专用前缀的 AI 智能体，或者适用于倾向于使用供应商无关标识符的团队。这是 **v1.1.0** 发布的关键新特性 —— 版本间变更的完整摘要请参见上一条常见问题。

### 如何处理 `develop` 或 `staging` 等长期存在的分支？

长期存在的集成或环境分支（如 `develop`，以及某些项目约定使用的 `staging`、`production` 等）通常被视为主干分支，不需要前缀，并应在整个项目中保持一致的命名。需要注意的是，在上文给出的 ABNF 语法中，`trunk-branch` 形式规则只包含 `main` / `master` / `develop`；`staging`、`production` 等仅作为各团队可选的长期分支示例，不属于该形式语法的一部分，语法校验工具可按需要在此基础上扩展支持。

### 如果团队成员不符合此规范，可以使用哪些工具来自动识别？

你可以使用 [commit-check](https://github.com/commit-check/commit-check) 来检查分支规范，或者如果你的代码托管在 GitHub 上，则使用 [commit-check-action](https://github.com/commit-check/commit-check-action)。

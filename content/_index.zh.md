---
draft: false
aliases: ["/zh/"]
layout: single
---

# 约定式分支

## 概述

约定式分支是指 Git 分支的结构化和标准化命名约定，旨在使分支更具可读性和可操作性。我们建议了一些您可能想要使用的分支前缀，但您也可以指定自己的命名约定。一致的命名约定使按类型识别分支变得更加容易。

### 要点

1. **以目的为导向的分支名称**：每个分支名称都清楚地表明了其目的，使所有开发人员都能轻松了解该分支的用途。
2. **与 CI/CD 集成**：通过使用一致的分支名称，它可以帮助自动化系统（如持续集成/持续部署管道）根据分支类型触发特定操作（例如，从发布分支自动部署）。
3. **团队协作**：它通过明确分支目的来鼓励团队内部的协作，减少误解并使团队成员更容易在任务之间切换而不会产生混淆。

## 规范

### 分支命名前缀

分支规范通过 `feature/`，`bugfix/`，`hotfix/`，`release/`和`chore/` 来描述，其结构应如下：

---

```
<type>/<description>
```

- **main**：主要开发分支（例如 `main`、`master` 或 `develop`）
- **feature/**：用于新功能（例如 `feature/add-login-page`）
- **bugfix/**：用于错误修复（例如 `bugfix/fix-header-bug`）
- **hotfix/**：用于紧急修复（例如 `hotfix/security-patch`）
- **release/**：用于准备发布的分支（例如 `release/v1.2.0`）
- **chore/**：用于非代码任务，如依赖项、文档更新（例如 `chore/update-dependencies`）

---

### 基本规则

1. **小写字母和连字符分隔**：始终使用小写字母，并使用连字符分隔单词。例如，`feature/new-login` 或 `bugfix/header-styling`。
2. **仅使用字母数字和连字符**：仅使用小写字母 (a-z)、数字 (0-9) 和连字符。避免使用空格、标点符号和下划线等特殊字符。
3. **无连续连字符**：确保连字符单独使用，没有连续的连字符（例如，`feature/new-login`，而不是 `feature/new--login`）。
4. **无尾随连字符**：请勿在分支名称末尾添加连字符。例如，使用 `feature/new-login` 而不是 `feature/new-login-`。
5. **清晰简洁**：使分支名称具有描述性但简洁。名称应清楚地表明正在完成的工作。
6. **包括 Jira（或其他工具）票号**：如果适用，请包括项目管理工具中的票号，以便于跟踪。例如，对于票号 `issue-123`，分支名称可以是 `feature/issue-123-new-login`。

## 结论

- **清晰的沟通**：仅凭分支名称就能清楚地了解代码更改的目的。
- **自动化友好**：轻松挂接自动化流程（例如，针对 `feature`, `release` 等的不同工作流程）。
- **可扩展性**：适用于许多开发人员同时处理不同任务的大型团队。

总之，约定式分支旨在改善 Git 工作流程中的项目组织、沟通和自动化。

## 常见问题

### 如果团队成员不符合此规范，可以使用哪些工具来自动识别？

你可以使用 [commit-check](https://github.com/commit-check/commit-check) 来检查分支规范，或者如果你的代码托管在 GitHub 上，则使用 [commit-check-action](https://github.com/commit-check/commit-check-action)。
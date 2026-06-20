---
draft: false
aliases: ["/zh-hant/"]
layout: single
---

# 約定式分支 1.1.0

## 概述

約定式分支（Conventional Branch）是指針對 Git branch 的結構化、標準化命名慣例，旨在讓 branch 更易讀且更具可操作性。我們提供一些您可能想採用的 branch 前綴建議，但您也可以自行制定命名慣例。一致的命名慣例能讓您更容易依類型辨識 branch。

### 要點

1. **以目的為導向的 branch 名稱**：每個 branch 名稱都清楚表明其目的，讓所有開發人員都能輕鬆理解該 branch 的用途。
2. **與 CI/CD 整合**：透過一致的 branch 命名，它可以協助自動化系統（例如 Continuous Integration/Continuous Deployment 管線）根據 branch 類型觸發特定動作（例如，從 release branch 自動部署）。
3. **團隊協作**：藉由明確標示 branch 的目的，促進團隊協作、降低誤解，並讓成員更容易在不同任務間切換而不致混淆。

## 規範

### branch 命名前綴

此 branch 規範支援以下前綴，並應採用如下結構：

---

```
<type>/<description>
```

**用途前綴（Purpose Prefixes）** — 描述工作的意圖：
- **`feature/`**（或 **`feat/`**）：用於新功能（例如 `feature/add-login-page`、`feat/add-login-page`）
- **`bugfix/`**（或 **`fix/`**）：用於 bug 修復（例如 `bugfix/fix-header-bug`、`fix/header-bug`）
- **`hotfix/`**：用於緊急修復（例如 `hotfix/security-patch`）
- **`release/`**：用於準備發布的 branch（例如 `release/v1.2.0`）
- **`chore/`**：用於非程式碼任務，例如相依套件、文件更新（例如 `chore/update-dependencies`）

**AI 智能體來源前綴（AI Agent Source Prefixes）** — 識別由 AI 編碼智能體產生的分支：
- **`ai/`**：通用 AI 編碼智能體前綴（例如 `ai/refactor-auth-flow`）
- **`copilot/`**：GitHub Copilot（例如 `copilot/add-login-page`）
- **`cursor/`**：Cursor（例如 `cursor/fix-header-bug`）
- **`claude/`**：Anthropic Claude Code（例如 `claude/security-patch`）
- **`codex/`**：OpenAI Codex（例如 `codex/optimize-query`）

主幹分支（`main`、`master`、`develop`）不使用前綴。

---

### 基本規則

1. **使用小寫英數、連字號與點**：一律使用小寫字母（`a-z`）、數字（`0-9`）與連字號（`-`）分隔單字，避免特殊字元、底線或空白。對於 release branch，可在描述中使用點（`.`）表示版本號（例如 `release/v1.2.0`）。
2. **禁止連續、開頭或結尾的連字號或點**：連字號與點不得連續出現（例如 `feature/new--login`、`release/v1.-2.0`），也不得出現在描述的開頭或結尾（例如 `feature/-new-login`、`release/v1.2.0.`）。
3. **保持清楚且精簡**：branch 名稱應在具描述性的同時保持精簡，清楚表達工作的內容與目的。
4. **包含工單編號**：若適用，請包含專案管理工具的工單編號，方便追蹤。例如，對於工單 `issue-123`，branch 名稱可以是 `feature/issue-123-new-login`。

### 形式文法

以下 ABNF（Augmented Backus-Naur Form）文法正式定義了有效的 branch 名稱：

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
                / "ai" / "copilot" / "cursor"
                / "claude" / "codex"
description     = desc-segment *("-" desc-segment)
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; 小寫字母 a-z
DIGIT           = %x30-39   ; 數字 0-9
```

> 注意：禁止連續的連字號或點，以及出現在描述開頭或結尾的連字號或點。

### 示例

| Branch 名稱 | 有效 | 說明 |
|---|---|---|
| `main` | ✅ | 主幹分支 |
| `master` | ✅ | 主幹分支 |
| `develop` | ✅ | 主幹分支 |
| `feature/add-login-page` | ✅ | 新功能 |
| `feat/add-login-page` | ✅ | feature 的簡寫形式 |
| `bugfix/fix-header-bug` | ✅ | Bug 修復 |
| `fix/header-bug` | ✅ | bugfix 的簡寫形式 |
| `hotfix/security-patch` | ✅ | 緊急修復 |
| `release/v1.2.0` | ✅ | 含版本號的發布分支 |
| `chore/update-dependencies` | ✅ | 非程式碼任務 |
| `feature/issue-123-new-login` | ✅ | 含工單編號的功能分支 |
| `Feature/Add-Login` | ❌ | 不允許大寫字母 |
| `feature/new--login` | ❌ | 不允許連續連字號 |
| `feature/-new-login` | ❌ | 描述不能以連字號開頭 |
| `feature/new-login-` | ❌ | 描述不能以連字號結尾 |
| `release/v1.-2.0` | ❌ | 連字號不能緊鄰點號 |
| `fix/header bug` | ❌ | 不允許空格 |
| `fix/header_bug` | ❌ | 不允許底線 |
| `ai/refactor-auth-flow` | ✅ | 通用 AI 編碼智能體前綴 |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Anthropic Claude Code |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | 未知的前綴類型 |

## 結論

- **清楚溝通**：僅從 branch 名稱即可清楚理解此程式碼變更的目的。
- **自動化友善**：容易串接自動化流程（例如針對 `feature`、`release` 等的不同工作流程）。
- **可擴充性**：適用於大型團隊，同時有許多開發人員處理不同任務的情境。

總結來說，Conventional Branch 的設計目標是改善 Git 工作流程中的專案組織、溝通與自動化。

## 工具

{{< tooling compact >}}

## FAQ

### 約定式分支與約定式提交（Conventional Commits）有什麼關係？

約定式分支的靈感來源於 [Conventional Commits](https://www.conventionalcommits.org)，遵循相似的理念：為 Git 中繼資料引入人機可讀的結構。約定式提交規範提交訊息，約定式分支規範 branch 名稱，兩者相輔相成、天然互補。

### 為什麼 branch type 不像 Conventional Commits（例如 `build`、`ci`、`docs`、`style`、`refactor`）那麼詳細？

branch 與 commit 不同——branch 是暫時性的，通常只會使用到 merge 為止。若為 branch 引入過多 type 並無必要，反而會讓管理與記憶變得更困難。

### 我可以定義規範列表之外的自訂 branch type 嗎？

可以。本規範定義了一套推薦的 type，但團隊可根據工作流程定義額外的自訂 type。重要的是，需要將自訂 type 清楚記錄，讓所有團隊成員及自動化工具皆能知悉。

### v1.1.0 與 v1.0.0 的主要差異是什麼？

v1.1.0 的主要新功能是引入了 **AI 智能體來源前綴（AI Agent Source Prefixes）**（具體原因見下一條常見問題）。同時，版本化網站增加了版本切換器，使用者可以瀏覽 v1.0.0 和 v1.1.0 兩種規範。所有現有的 v1.0.0 branch 名稱仍然完全有效 —— 沒有不相容的變更。

### 為什麼要添加 AI 智能體來源前綴（AI Agent Source Prefixes）？

AI 編碼智能體（GitHub Copilot、Cursor、Claude Code、OpenAI Codex 等）越來越多地被用於生成程式碼和建立 Pull Request。每個智能體都使用自己的分支前綴（例如 `copilot/`、`cursor/`）。透過在約定式分支規範中標準化這些前綴，我們可以實現：
1. **快速識別** — 審查者和工具可以立即識別 AI 生成的 PR
2. **工具驗證** — 諸如 commit-check 之類的工具可以驗證 AI 智能體分支是否符合規範
3. **註冊標準** — 新的 AI 智能體可以採用已記錄的前綴，而不是自行建立臨時的模式

`ai/` 通用前綴適用於沒有專用前綴的 AI 智能體，或者適用於傾向於使用供應商中立識別碼的團隊。這是 **v1.1.0** 發佈的關鍵新特性 —— 版本間變更的完整摘要請參見上一條常見問題。

### 如何處理 `develop` 或 `staging` 等長期存在的 branch？

長期存在的整合或環境 branch（例如 `develop`、`staging`、`production`）通常在專案層級被視為主幹分支，不需要前綴，且應在整個專案中保持一致的命名。依照本規範前文所述的 ABNF 正式文法，預設的 `trunk-branch` 僅包含標準主幹名稱（例如 `main`、`master`、`develop`）；其他名稱（如 `staging`、`production`）則屬於專案自訂的延伸，建議在團隊文件中明確記錄，以便工具與成員正確辨識。

### 有哪些工具可以自動識別團隊成員是否符合此規範？

您可以使用 [commit-check](https://github.com/commit-check/commit-check) 檢查 branch 規範；若您的程式碼託管於 GitHub，則可使用 [commit-check-action](https://github.com/commit-check/commit-check-action)。

---
draft: false
aliases: ["/zh-hant/"]
layout: single
seoTitle: "Git 分支命名規範 — 約定式分支 Conventional Branch"
seoDescription: "Git 分支命名規範：feature/、bugfix/、hotfix/、release/、chore/ 等分支前綴，附正式語法，以及在 GitHub、GitLab 中強制檢查的方法。"
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
{{< agents >}}

此列表已凍結：沒有專屬前綴的智能體使用 `ai/`。

主幹分支（`main`、`master`、`develop`）不使用前綴。

---

### 基本規則

1. **使用小寫英數、連字號與點**：一律使用小寫字母（`a-z`）、數字（`0-9`）與連字號（`-`）分隔單字，避免特殊字元、底線或空白。任何 branch 的描述中都可以使用點（`.`），通常用於表示版本號（例如 `release/v1.2.0`、`chore/upgrade-node-v20.11`）。
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
| `chore/upgrade-node-v20.11` | ✅ | 非 release branch 中的點 |
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

### 約定式分支發明了這些前綴嗎？

沒有。`feature/`、`hotfix/`、`release/` 這類前綴約在 2010 年由 [git-flow](https://github.com/nvie/gitflow) 工具推廣開來，也是 [Bitbucket branching model](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/) 等工具的預設值。約定式分支建立在這項實務之上，而非取而代之。它補上的是一份人與工具都能共用的精確定義：固定的 type 集合、形式文法、發布於 [`spec.json`](/spec.json) 的驗證正規表示式，以及一致性測試案例，讓每個驗證工具接受的名稱完全相同。

### 為什麼 branch type 不像 Conventional Commits（例如 `build`、`ci`、`docs`、`style`、`refactor`）那麼詳細？

branch 與 commit 不同——branch 是暫時性的，通常只會使用到 merge 為止。若為 branch 引入過多 type 並無必要，反而會讓管理與記憶變得更困難。

### 我可以定義規範列表之外的自訂 branch type 嗎？

可以，作為團隊層級的擴充。文法中列出的 type 是所有符合規範的工具都會接受的 type，因此像 `unknown/some-task` 這樣的 branch 依規範本身是無效的。若團隊需要更多 type（例如 `experiment/`），應在驗證工具中明確列出（例如 [commit-check](/enforce/#commit-check) 的 `allow_branch_types`），並寫入文件，讓團隊成員與自動化工具保持一致。例如，本規範自己的 repository 就在 [commit-check 設定](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml)中為 Dependabot 建立的 branch 加入了 `dependabot/`。

### 為什麼 branch 名稱必須小寫？

原因有二。第一，Git 通常將 branch 參照存成 `.git/refs/heads/` 下的檔案，而 macOS 與 Windows 預設的檔案系統不區分大小寫：`Feature/login` 與 `feature/login` 在這些機器上指向同一路徑，在 Linux 上卻是兩個不同的 branch，因此同時允許兩種寫法的 repository 在不同 clone 中的行為可能不一致。第二，只有一種寫法更容易輸入、搜尋與比對：依 `release/*` 觸發的工具不必再考慮 `Release/*`。

### v1.1.0 與 v1.0.0 的主要差異是什麼？

v1.1.0 的主要新功能是引入了 **AI 智能體來源前綴（AI Agent Source Prefixes）**（具體原因見下一條常見問題）。同時，版本化網站增加了版本切換器，使用者可以瀏覽 v1.0.0 和 v1.1.0 兩種規範。所有現有的 v1.0.0 branch 名稱仍然完全有效 —— 沒有不相容的變更。

### 為什麼要添加 AI 智能體來源前綴（AI Agent Source Prefixes）？

AI 編碼智能體（GitHub Copilot、Cursor、Claude Code、OpenAI Codex 等）越來越多地被用於生成程式碼和建立 Pull Request。每個智能體都使用自己的分支前綴（例如 `copilot/`、`cursor/`）。透過在約定式分支規範中標準化這些前綴，我們可以實現：
1. **快速識別** — 審查者和工具可以立即識別 AI 生成的 PR
2. **工具驗證** — 諸如 commit-check 之類的工具可以驗證 AI 智能體分支是否符合規範
3. **穩定的列表** — 這五個前綴固定不變，其他智能體使用 `ai/`，文法不會因新工具的出現而變動

`ai/` 通用前綴適用於沒有專用前綴的 AI 智能體，或者適用於傾向於使用供應商中立識別碼的團隊。這是 **v1.1.0** 發佈的關鍵新特性 —— 版本間變更的完整摘要請參見上一條常見問題。

### 如何處理 `develop` 或 `staging` 等長期存在的 branch？

長期存在的整合或環境 branch（例如 `develop`、`staging`、`production`）通常在專案層級被視為主幹分支，不需要前綴，且應在整個專案中保持一致的命名。依照本規範前文所述的 ABNF 正式文法，預設的 `trunk-branch` 僅包含標準主幹名稱（例如 `main`、`master`、`develop`）；其他名稱（如 `staging`、`production`）則屬於專案自訂的延伸，建議在團隊文件中明確記錄，以便工具與成員正確辨識。

### 有哪些工具可以自動識別團隊成員是否符合此規範？

您可以使用 [commit-check](https://github.com/commit-check/commit-check) 檢查 branch 規範；若您的程式碼託管於 GitHub，則可使用 [commit-check-action](https://github.com/commit-check/commit-check-action)。

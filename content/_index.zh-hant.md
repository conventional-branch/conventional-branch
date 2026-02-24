---
draft: false
aliases: ["/zh-hant/"]
layout: single
---

# 約定式分支 1.0.0

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

- **`main`**：主要開發 branch（例如 `main`、`master` 或 `develop`）
- **`feature/`**（或 **`feat/`**）：用於新功能（例如 `feature/add-login-page`、`feat/add-login-page`）
- **`bugfix/`**（或 **`fix/`**）：用於 bug 修復（例如 `bugfix/fix-header-bug`、`fix/header-bug`）
- **`hotfix/`**：用於緊急修復（例如 `hotfix/security-patch`）
- **`release/`**：用於準備發布的 branch（例如 `release/v1.2.0`）
- **`chore/`**：用於非程式碼任務，例如相依套件、文件更新（例如 `chore/update-dependencies`）

---

### 基本規則

1. **使用小寫英數、連字號與點**：一律使用小寫字母（`a-z`）、數字（`0-9`）與連字號（`-`）分隔單字，避免特殊字元、底線或空白。對於 release branch，可在描述中使用點（`.`）表示版本號（例如 `release/v1.2.0`）。
2. **禁止連續、開頭或結尾的連字號或點**：連字號與點不得連續出現（例如 `feature/new--login`、`release/v1.-2.0`），也不得出現在描述的開頭或結尾（例如 `feature/-new-login`、`release/v1.2.0.`）。
3. **保持清楚且精簡**：branch 名稱應在具描述性的同時保持精簡，清楚表達工作的內容與目的。
4. **包含工單編號**：若適用，請包含專案管理工具的工單編號，方便追蹤。例如，對於工單 `issue-123`，branch 名稱可以是 `feature/issue-123-new-login`。

## 結論

- **清楚溝通**：僅從 branch 名稱即可清楚理解此程式碼變更的目的。
- **自動化友善**：容易串接自動化流程（例如針對 `feature`、`release` 等的不同工作流程）。
- **可擴充性**：適用於大型團隊，同時有許多開發人員處理不同任務的情境。

總結來說，Conventional Branch 的設計目標是改善 Git 工作流程中的專案組織、溝通與自動化。

## FAQ

### 為什麼 branch type 不像 Conventional Commits（例如 `build`、`ci`、`docs`、`style`、`refactor`）那麼詳細？

branch 與 commit 不同——branch 是暫時性的，通常只會使用到 merge 為止。若為 branch 引入過多 type 並無必要，反而會讓管理與記憶變得更困難。

### 有哪些工具可以自動識別團隊成員是否符合此規範？

您可以使用 [commit-check](https://github.com/commit-check/commit-check) 檢查 branch 規範；若您的程式碼託管於 GitHub，則可使用 [commit-check-action](https://github.com/commit-check/commit-check-action)。

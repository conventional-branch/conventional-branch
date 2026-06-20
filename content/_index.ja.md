---
draft: false
aliases: ["/ja/"]
layout: single
---

# 慣例的ブランチ 1.1.0

## 要約

慣例的ブランチとは、Git ブランチの構造化された標準的な命名規則を指し、ブランチをより読みやすく実用的にすることを目的としています。使用したいブランチのプレフィックスをいくつか提案していますが、独自の命名規則を指定することもできます。一貫した命名規則により、タイプ別にブランチを識別しやすくなります。

### 重要なポイント

1. **目的主導のブランチ名**: 各ブランチ名はその目的を明確に示し、すべての開発者がそのブランチの用途を理解しやすくします。
2. **CI/CD との統合**: 一貫したブランチ名を使用することで、自動化システム（継続的インテグレーション/継続的デプロイメントパイプラインなど）がブランチタイプに基づいて特定のアクションをトリガーするのに役立ちます（例：リリースブランチからの自動デプロイ）。
3. **チーム連携**: ブランチの目的を明確にすることでチーム内の連携を促進し、誤解を減らし、チームメンバーが混乱することなくタスク間を切り替えやすくします。

## 仕様

### ブランチ命名のプレフィックス

ブランチ仕様は以下のプレフィックスをサポートし、次のような構造にする必要があります：

---

```
<type>/<description>
```

**目的プレフィックス（Purpose Prefixes）** — 作業の意図を説明します：
- **`feature/`**（または **`feat/`**）: 新機能用（例：`feature/add-login-page`、`feat/add-login-page`）
- **`bugfix/`**（または **`fix/`**）: バグ修正用（例：`bugfix/fix-header-bug`、`fix/header-bug`）
- **`hotfix/`**: 緊急修正用（例：`hotfix/security-patch`）
- **`release/`**: リリース準備ブランチ用（例：`release/v1.2.0`）
- **`chore/`**: 依存関係やドキュメント更新などの非コードタスク用（例：`chore/update-dependencies`）

**AI エージェントソースプレフィックス（AI Agent Source Prefixes）** — AI コーディングエージェントによって生成されたブランチを識別します：
- **`ai/`**: 汎用 AI エージェントプレフィックス（例：`ai/refactor-auth-flow`）
- **`copilot/`**: GitHub Copilot（例：`copilot/add-login-page`）
- **`cursor/`**: Cursor（例：`cursor/fix-header-bug`）
- **`claude/`**: Anthropic Claude Code（例：`claude/security-patch`）
- **`codex/`**: OpenAI Codex（例：`codex/optimize-query`）

トランクブランチ（`main`、`master`、`develop`）はプレフィックスを使用しません。

---

### 基本ルール

1. **小文字の英数字、ハイフン、ドットを使用**: 常に小文字（`a-z`）、数字（`0-9`）、ハイフン（`-`）を使用して単語を区切ります。特殊文字、アンダースコア、スペースは避けてください。リリースブランチでは、バージョン番号を表すために説明部分でドット（`.`）を使用できます（例：`release/v1.2.0`）。
2. **連続、先頭、末尾のハイフンやドットは禁止**: ハイフンとドットが連続して表示されないように（例：`feature/new--login`、`release/v1.-2.0`）、説明の先頭や末尾に表示されないようにしてください（例：`feature/-new-login`、`release/v1.2.0.`）。
3. **明確で簡潔に保つ**: ブランチ名は説明的でありながら簡潔で、作業の目的を明確に示す必要があります。
4. **チケット番号を含める**: 該当する場合、プロジェクト管理ツールからのチケット番号を含めて追跡を容易にします。例えば、チケット `issue-123` の場合、ブランチ名は `feature/issue-123-new-login` とすることができます。


### 形式文法

以下の ABNF（拡張バッカス・ナウア記法）文法は、有効なブランチ名を形式的に定義します：

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
ALPHA           = %x61-7A   ; 小文字 a-z
DIGIT           = %x30-39   ; 数字 0-9
```

> 注意：連続するハイフンやドット、および説明の先頭や末尾のハイフンやドットは使用できません。

### 例

| ブランチ名 | 有効 | 備考 |
|---|---|---|
| `main` | ✅ | トランクブランチ |
| `master` | ✅ | トランクブランチ |
| `develop` | ✅ | トランクブランチ |
| `feature/add-login-page` | ✅ | 新機能 |
| `feat/add-login-page` | ✅ | feature の短縮形 |
| `bugfix/fix-header-bug` | ✅ | バグ修正 |
| `fix/header-bug` | ✅ | bugfix の短縮形 |
| `hotfix/security-patch` | ✅ | 緊急修正 |
| `release/v1.2.0` | ✅ | バージョン番号付きリリース |
| `chore/update-dependencies` | ✅ | 非コードタスク |
| `feature/issue-123-new-login` | ✅ | チケット番号付き機能 |
| `Feature/Add-Login` | ❌ | 大文字は使用不可 |
| `feature/new--login` | ❌ | 連続するハイフンは使用不可 |
| `feature/-new-login` | ❌ | 説明をハイフンで始めることは不可 |
| `feature/new-login-` | ❌ | 説明をハイフンで終わらせることは不可 |
| `release/v1.-2.0` | ❌ | ドットに隣接するハイフンは不可 |
| `fix/header bug` | ❌ | スペースは使用不可 |
| `fix/header_bug` | ❌ | アンダースコアは使用不可 |
| `ai/refactor-auth-flow` | ✅ | 汎用 AI エージェントプレフィックス |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Anthropic Claude Code |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | 未知のプレフィックスタイプ |

## 結論

- **明確なコミュニケーション**: ブランチ名だけで、そのコード変更の目的を明確に理解できます。
- **自動化フレンドリー**: 自動化プロセスに簡単にフックできます（例：`feature`、`release` などの異なるワークフロー）。
- **スケーラビリティ**: 多くの開発者が同時に異なるタスクに取り組む大規模なチームでうまく機能します。

要約すると、慣例的ブランチは Git ワークフロー内のプロジェクト組織、コミュニケーション、自動化を改善するために設計されています。

## ツール

{{< tooling compact >}}

## よくある質問

### Conventional Branch と Conventional Commits の関係は？

Conventional Branch は [Conventional Commits](https://www.conventionalcommits.org) に触発され、同様の哲学に基づいています：人間と機械が読めるような構造を Git メタデータに組み込むこと。Conventional Commits がコミットメッセージを標準化するのに対して、Conventional Branch はブランチ名を標準化します。両者は自然に補完し合います。

### なぜブランチの種類はConventional Commits（例：`build`、`ci`、`docs`、`style`、`refactor`）ほど詳細ではないのですか？

ブランチはコミットとは異なり、一時的なもので、主にマージされるまで使用されます。ブランチにあまり多くの種類を導入することは不要で、管理や記憶が難しくなります。

### 仕様に記載されているもの以外に独自のブランチタイプを定義できますか？

はい。この仕様は推奨されるタイプのセットを定義しますが、チームはワークフローに合わせて追加のカスタムタイプを定義することができます。ただし、すべてのチームメンバーと自動化ツールが認識できるよう、カスタムタイプを明確に文書化することが重要です。

### v1.1.0 と v1.0.0 の主な違いは何ですか？

v1.1.0 の主な新機能は **AI エージェントソースプレフィックス（AI Agent Source Prefixes）** の導入です（その理由は次のよくある質問を参照してください）。また、バージョン管理されたウェブサイトにバージョン切り替え機能が追加され、v1.0.0 と v1.1.0 の両方の仕様を参照できます。既存の v1.0.0 ブランチ名はすべて引き続き有効です — 互換性を損なう変更はありません。

### AI エージェントソースプレフィックスを追加する理由は？

AI コーディングエージェント（GitHub Copilot、Cursor、Claude Code、OpenAI Codex など）は、コード生成や Pull Request 作成にますます使用されています。各エージェントは独自のブランチプレフィックス（例：`copilot/`、`cursor/`）を使用しています。Conventional Branch 仕様でこれらのプレフィックスを標準化することで、以下が可能になります：
1. **迅速な識別** — レビュアーとツールは AI 生成 PR を即座に認識できます
2. **ツール検証** — commit-check などのツールが AI エージェントブランチを仕様に照らして検証できます
3. **登録標準** — 新しい AI エージェントはアドホックなパターンを発明する代わりに、文書化されたプレフィックスを採用できます

`ai/` 汎用プレフィックスは、専用プレフィックスを持たない AI エージェント、またはベンダーニュートラルな識別子を好むチームのために利用可能です。これは **v1.1.0** でリリースされた主要な新機能です — バージョン間の変更の完全な概要については、上記のよくある質問を参照してください。

### `develop` や `staging` のような長期存在するブランチはどう扱えばよいですか？

仕様の ABNF では `trunk-branch` は `main` / `master` / `develop` のみを指しますが、運用上、それ以外の長期存在する統合用または環境用ブランチ（例：`staging`、`production`）をプロジェクト独自のトランク相当ブランチとして扱っても構いません（この場合もプレフィックスは不要です）。その際は、これらのブランチ名が仕様の拡張であることを明確に文書化し、プロジェクト全体で一貫した命名を心がけてください。

### チームメンバーがこの仕様を満たしていない場合、自動的に識別するために使用できるツールは何ですか？

[commit-check](https://github.com/commit-check/commit-check) を使用してブランチ仕様をチェックするか、コードが GitHub でホストされている場合は [commit-check-action](https://github.com/commit-check/commit-check-action) を使用できます。

---
draft: false
aliases: ["/ja/"]
layout: single
seoTitle: "Git ブランチ命名規則 — Conventional Branch"
seoDescription: "Git のブランチ名の命名規則：feature/・bugfix/・hotfix/・release/・chore/ などのプレフィックスと正式な文法、GitHub や GitLab で強制する方法。"
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
{{< agents >}}

トランクブランチ（`main`、`master`、`develop`）はプレフィックスを使用しません。

---

### 基本ルール

1. **小文字の英数字、ハイフン、ドットを使用**: 常に小文字（`a-z`）、数字（`0-9`）、ハイフン（`-`）を使用して単語を区切ります。特殊文字、アンダースコア、スペースは避けてください。ドット（`.`）はどのブランチの説明部分でも使用でき、主にバージョン番号を表すために使います（例：`release/v1.2.0`、`chore/upgrade-node-v20.11`）。
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
| `chore/upgrade-node-v20.11` | ✅ | リリース以外のブランチでのドット |
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

### ブランチ名とは何ですか？

ブランチ名とは、Git が開発の流れに付けるラベルで、`main` や `feature/add-login-page` のようなものです。Git はこれを `refs/heads/` 配下の参照（ref）として保持します。Git は幅広い名前を受け付けるため、ブランチ名だけでは、そのブランチで行われている作業について確かなことは何もわかりません。Conventional Branch はブランチ名に `<type>/<description>` という構造を与えます。作業の目的を示すタイプに続けて、小文字の短い説明を置き、単語はハイフンで区切ります。例：

- `feature/add-login-page`
- `bugfix/fix-header-bug`
- `release/v1.2.0`

トランクブランチ（`main`、`master`、`develop`）にはプレフィックスを付けません。

### feature ブランチにはどのような名前を付ければよいですか？

`feature/`、または短縮形の `feat/` で始め、スラッシュの後に機能の内容を書きます。作業にプロジェクト管理ツールのチケットがある場合は、その番号を含めます。例：

- `feature/add-login-page`
- `feat/add-login-page`
- `feature/issue-123-new-login`

### chore ブランチとは何ですか？

`chore/` ブランチは、依存関係やドキュメントの更新といった非コードタスクのためのものです。ブランチのタイプは意図的に Conventional Commits のタイプより少なくしてあるため（下記のよくある質問を参照）、この種のメンテナンス作業は `chore/` にまとめます。例：

- `chore/update-dependencies`
- `chore/upgrade-node-v20.11`
- `chore/update-generated-files`

Renovate など一部の依存関係更新ボットも、このプレフィックスを使うように設定できます。[ボットと自動化](/enforce/#name-them-to-fit)を参照してください。

### release ブランチにはどのような名前を付ければよいですか？

`release/` の後に、そのブランチが準備するもの（通常はバージョン番号）を続けます。ドットは使えますが、説明の先頭や末尾には置けず、ハイフンの隣にも置けません：

- `release/v1.2.0` — 有効
- `release/v1.2.0.` — 無効：末尾のドット
- `release/v1.-2.0` — 無効：ドットに隣接するハイフン

プレフィックスが一貫していれば、パイプラインで `release/*` を対象にした処理も行えます。たとえば、リリースブランチからの自動デプロイです。

### hotfix ブランチにはどのような名前を付ければよいですか？

緊急の修正には `hotfix/` を、緊急でない修正には `bugfix/`（または `fix/`）を使います。何を修正するのかを説明し、チケットがあればその番号を含めます。例：

- `hotfix/security-patch`
- `hotfix/issue-123-security-patch`
- `bugfix/fix-header-bug`（緊急でない修正の場合）

### Conventional Branch と Conventional Commits の関係は？

Conventional Branch は [Conventional Commits](https://www.conventionalcommits.org) に触発され、同様の哲学に基づいています：人間と機械が読めるような構造を Git メタデータに組み込むこと。Conventional Commits がコミットメッセージを標準化するのに対して、Conventional Branch はブランチ名を標準化します。両者は自然に補完し合います。

### Conventional Branch がこれらのプレフィックスを考案したのですか？

いいえ。`feature/`、`hotfix/`、`release/` といったプレフィックスは 2010 年頃に [git-flow](https://github.com/nvie/gitflow) ツールによって広まり、[Bitbucket のブランチモデル](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/)などのツールでも既定値になっています。Conventional Branch はこの慣行を置き換えるのではなく、その上に成り立っています。加えているのは、人とツールが共有できる厳密な定義です。固定されたタイプの集合、形式文法、[`spec.json`](/spec.json) で公開している検証用の正規表現、そして適合性テストケースにより、どの検証ツールでも有効と判定される名前が一致します。

### なぜブランチの種類はConventional Commits（例：`build`、`ci`、`docs`、`style`、`refactor`）ほど詳細ではないのですか？

ブランチはコミットとは異なり、一時的なもので、主にマージされるまで使用されます。ブランチにあまり多くの種類を導入することは不要で、管理や記憶が難しくなります。

### 仕様に記載されているもの以外に独自のブランチタイプを定義できますか？

はい、チーム単位の拡張として可能です。文法に記載されたタイプは、仕様に準拠するすべてのツールが受け入れるものです。そのため `unknown/some-task` のようなブランチは、仕様そのものの上では無効です。追加のタイプ（例：`experiment/`）が必要なチームは、検証ツールにそれを明示的に登録し（例：[commit-check](/enforce/#commit-check) の `allow_branch_types`）、文書化して、チームメンバーと自動化ツールの認識を揃えてください。たとえば、この仕様自身のリポジトリでは、Dependabot が作成するブランチのために [commit-check の設定](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml)に `dependabot/` を追加しています。

### なぜブランチ名は小文字でなければならないのですか？

理由は 2 つあります。第一に、Git は通常ブランチの参照を `.git/refs/heads/` 配下のファイルとして保存しますが、macOS と Windows の既定のファイルシステムは大文字と小文字を区別しません。`Feature/login` と `feature/login` はこれらのマシンでは同じパスになり、Linux では別々のブランチになるため、両方を許すリポジトリはクローンごとに挙動が異なることがあります。第二に、表記が 1 つなら入力・検索・照合が簡単です。`release/*` で動くツールが `Release/*` まで想定する必要がありません。

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

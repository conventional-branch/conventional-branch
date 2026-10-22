---
draft: false
aliases: ["/de/"]
layout: single
seoTitle: "Git Branch-Namenskonvention — Conventional Branch"
seoDescription: "Eine Spezifikation für Git-Branch-Namen: die Präfixe feature/, bugfix/, hotfix/, release/ und chore/, eine formale Grammatik und wie man sie in GitHub und GitLab durchsetzt."
---

# Conventional Branch 1.1.0

## Zusammenfassung

Conventional Branch bezieht sich auf eine strukturierte und standardisierte Namenskonvention für Git-Branches, die darauf abzielt, Branches lesbarer und umsetzbarer zu machen. Wir haben einige Branch-Präfixe vorgeschlagen, die Sie verwenden könnten, aber Sie können auch Ihre eigene Namenskonvention festlegen. Eine einheitliche Namenskonvention erleichtert die Identifizierung von Branches nach Typ.

### Wichtige Punkte

1. **Zweckgerichtete Branch-Namen**: Jeder Branch-Name zeigt deutlich seinen Zweck an, wodurch es für alle Entwickler einfach wird zu verstehen, wofür der Branch gedacht ist.
2. **Integration mit CI/CD**: Durch die Verwendung einheitlicher Branch-Namen können automatisierte Systeme (wie Continuous Integration/Continuous Deployment-Pipelines) dabei helfen, spezifische Aktionen basierend auf dem Branch-Typ auszulösen (z.B. automatische Bereitstellung von Release-Branches).
3. **Team-Zusammenarbeit**: Es fördert die Zusammenarbeit innerhalb von Teams, indem der Branch-Zweck explizit gemacht wird, Missverständnisse reduziert werden und es Teammitgliedern erleichtert wird, zwischen Aufgaben ohne Verwirrung zu wechseln.

## Spezifikation

### Branch-Namens-Präfixe

Die Branch-Spezifikation unterstützt die folgenden Präfixe und sollte wie folgt strukturiert sein:

---

```
<typ>/<beschreibung>
```

**Zweck-Präfixe** — beschreiben die Absicht der Arbeit:
- **`feature/`** (oder **`feat/`**): Für neue Features (z.B. `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (oder **`fix/`**): Für Fehlerbehebungen (z.B. `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: Für dringende Korrekturen (z.B. `hotfix/security-patch`)
- **`release/`**: Für Branches, die ein Release vorbereiten (z.B. `release/v1.2.0`)
- **`chore/`**: Für Nicht-Code-Aufgaben wie Abhängigkeiten, Dokumentation-Updates (z.B. `chore/update-dependencies`)

**AI-Agenten-Quellpräfixe** — identifizieren Branches, die von KI-Codierungsagenten erstellt wurden:
{{< agents >}}

Diese Liste ist abgeschlossen: Ein Agent ohne eigenes Präfix verwendet `ai/`.

Trunk-Branches (`main`, `master`, `develop`) verwenden kein Präfix.

---

### Grundregeln

1. **Verwenden Sie kleine Buchstaben und Zahlen, Bindestriche und Punkte**: Verwenden Sie immer Kleinbuchstaben (`a-z`), Zahlen (`0-9`) und Bindestriche (`-`), um Wörter zu trennen. Vermeiden Sie Sonderzeichen, Unterstriche oder Leerzeichen. Punkte (`.`) sind in jeder Beschreibung erlaubt, typischerweise für Versionsnummern (z.B. `release/v1.2.0`, `chore/upgrade-node-v20.11`).
2. **Keine aufeinanderfolgenden, führenden oder nachfolgenden Bindestriche oder Punkte**: Stellen Sie sicher, dass Bindestriche und Punkte nicht aufeinanderfolgen (z.B. `feature/new--login`, `release/v1.-2.0`), noch am Anfang oder Ende der Beschreibung (z.B. `feature/-new-login`, `release/v1.2.0.`).
3. **Halten Sie es klar und prägnant**: Der Branch-Name sollte beschreibend aber prägnant sein und den Zweck der Arbeit klar angeben.
4. **Ticket-Nummern einbeziehen**: Falls zutreffend, beziehen Sie die Ticket-Nummer aus Ihrem Projektmanagement-Tool ein, um die Verfolgung zu erleichtern. Zum Beispiel könnte für ein Ticket `issue-123` der Branch-Name `feature/issue-123-new-login` lauten.


### Formale Grammatik

Die folgende ABNF-Grammatik (Augmented Backus-Naur Form) definiert formal gültige Branch-Namen:

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
ALPHA           = %x61-7A   ; Kleinbuchstaben a-z
DIGIT           = %x30-39   ; Ziffern 0-9
```

> Hinweis: Aufeinanderfolgende Bindestriche oder Punkte sowie Bindestriche oder Punkte am Anfang oder Ende der Beschreibung sind nicht erlaubt.

### Beispiele

| Branch-Name | Gültig | Hinweise |
|---|---|---|
| `main` | ✅ | Trunk-Branch |
| `master` | ✅ | Trunk-Branch |
| `develop` | ✅ | Trunk-Branch |
| `feature/add-login-page` | ✅ | Neues Feature |
| `feat/add-login-page` | ✅ | Kurzform für feature |
| `bugfix/fix-header-bug` | ✅ | Fehlerbehebung |
| `fix/header-bug` | ✅ | Kurzform für bugfix |
| `hotfix/security-patch` | ✅ | Dringende Korrektur |
| `release/v1.2.0` | ✅ | Release mit Versionsnummer |
| `chore/upgrade-node-v20.11` | ✅ | Punkte außerhalb eines Release-Branches |
| `chore/update-dependencies` | ✅ | Nicht-Code-Aufgabe |
| `feature/issue-123-new-login` | ✅ | Feature mit Ticket-Nummer |
| `Feature/Add-Login` | ❌ | Großbuchstaben nicht erlaubt |
| `feature/new--login` | ❌ | Aufeinanderfolgende Bindestriche nicht erlaubt |
| `feature/-new-login` | ❌ | Beschreibung darf nicht mit Bindestrich beginnen |
| `feature/new-login-` | ❌ | Beschreibung darf nicht mit Bindestrich enden |
| `release/v1.-2.0` | ❌ | Bindestrich neben Punkt nicht erlaubt |
| `fix/header bug` | ❌ | Leerzeichen nicht erlaubt |
| `fix/header_bug` | ❌ | Unterstriche nicht erlaubt |
| `ai/refactor-auth-flow` | ✅ | Generischer KI-Agenten-Präfix |
| `copilot/add-login-page` | ✅ | GitHub Copilot |
| `cursor/fix-header-bug` | ✅ | Cursor |
| `claude/security-patch` | ✅ | Claude Code von Anthropic |
| `codex/optimize-query` | ✅ | OpenAI Codex |
| `unknown/some-task` | ❌ | Unbekannter Präfixtyp |

## Fazit

- **Klare Kommunikation**: Der Branch-Name allein bietet ein klares Verständnis seines Zwecks und der Code-Änderung.
- **Automatisierungsfreundlich**: Lässt sich einfach in Automatisierungsprozesse einbinden (z.B. verschiedene Workflows für `feature`, `release`, etc.).
- **Skalierbarkeit**: Funktioniert gut in großen Teams, wo viele Entwickler gleichzeitig an verschiedenen Aufgaben arbeiten.

Zusammenfassend ist Conventional Branch darauf ausgelegt, die Projektorganisation, Kommunikation und Automatisierung innerhalb von Git-Workflows zu verbessern.

## Werkzeuge

{{< tooling compact >}}

## FAQ

### Was ist ein Branch-Name?

Ein Branch-Name ist die Bezeichnung, die Git einer Entwicklungslinie gibt, etwa `main` oder `feature/add-login-page`; Git speichert ihn als Ref unter `refs/heads/`. Git akzeptiert eine große Bandbreite an Namen, deshalb sagt ein Branch-Name für sich genommen nichts Verlässliches über die Arbeit darauf aus. Conventional Branch gibt ihm eine Struktur, `<typ>/<beschreibung>`: einen Typ, der angibt, wofür die Arbeit gedacht ist, gefolgt von einer kurzen, kleingeschriebenen Beschreibung, deren Wörter durch Bindestriche getrennt sind. Zum Beispiel:

- `feature/add-login-page`
- `bugfix/fix-header-bug`
- `release/v1.2.0`

Trunk-Branches (`main`, `master`, `develop`) erhalten kein Präfix.

### Wie sollte ich einen Feature-Branch benennen?

Beginnen Sie ihn mit `feature/` oder der Kurzform `feat/` und beschreiben Sie das Feature nach dem Schrägstrich. Gibt es für die Arbeit ein Ticket in Ihrem Projektmanagement-Tool, nehmen Sie dessen Nummer auf. Zum Beispiel:

- `feature/add-login-page`
- `feat/add-login-page`
- `feature/issue-123-new-login`

### Was ist ein Chore-Branch?

Ein `chore/`-Branch ist für Nicht-Code-Aufgaben gedacht, etwa das Aktualisieren von Abhängigkeiten oder Dokumentation. Es gibt bewusst weniger Branch-Typen als Typen in Conventional Commits (siehe unten), daher gehört diese Art von Wartung unter `chore/`. Zum Beispiel:

- `chore/update-dependencies`
- `chore/upgrade-node-v20.11`
- `chore/update-generated-files`

Einige Bots für Abhängigkeiten, etwa Renovate, lassen sich ebenfalls so einstellen, dass sie das Präfix verwenden; siehe [Bots und Automatisierung](/enforce/#name-them-to-fit).

### Wie sollte ich einen Release-Branch benennen?

Verwenden Sie `release/`, gefolgt von dem, was der Branch vorbereitet, typischerweise die Versionsnummer. Punkte sind erlaubt, aber nicht am Anfang oder Ende der Beschreibung und nicht neben einem Bindestrich:

- `release/v1.2.0` — gültig
- `release/v1.2.0.` — ungültig: Punkt am Ende
- `release/v1.-2.0` — ungültig: Bindestrich neben einem Punkt

Ein einheitliches Präfix ermöglicht es außerdem einer Pipeline, auf `release/*` zu reagieren, zum Beispiel für die automatische Bereitstellung von Release-Branches.

### Wie sollte ich einen Hotfix-Branch benennen?

Verwenden Sie `hotfix/` für eine dringende Korrektur und `bugfix/` (oder `fix/`) für eine, die nicht dringend ist. Beschreiben Sie, was behoben wird, und nehmen Sie die Ticket-Nummer auf, falls es eine gibt. Zum Beispiel:

- `hotfix/security-patch`
- `hotfix/issue-123-security-patch`
- `bugfix/fix-header-bug` für eine Korrektur, die nicht dringend ist

### Wie verhält sich Conventional Branch zu Conventional Commits?

Conventional Branch wurde von [Conventional Commits](https://www.conventionalcommits.org) inspiriert und verfolgt eine ähnliche Philosophie: menschlich- und maschinenlesbaren Struktur in Git-Metadaten einzubringen. Während Conventional Commits Commit-Nachrichten standardisiert, standardisiert Conventional Branch Branch-Namen. Die beiden Spezifikationen ergänzen sich auf natürliche Weise.

### Hat Conventional Branch diese Präfixe erfunden?

Nein. Präfixe wie `feature/`, `hotfix/` und `release/` wurden um 2010 durch das [git-flow](https://github.com/nvie/gitflow)-Tooling verbreitet und sind Standard in Werkzeugen wie dem [Branching-Modell von Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/configure-a-projects-branching-model/). Conventional Branch baut auf dieser Praxis auf, statt sie zu ersetzen. Es ergänzt eine präzise Definition, die Menschen und Werkzeuge teilen können: eine feste Menge von Typen, eine formale Grammatik, eine in [`spec.json`](/spec.json) veröffentlichte Validierungs-Regex und Konformitätsfälle, damit jeder Validator genau dieselben Namen akzeptiert.

### Warum sind Branch-Typen nicht so detailliert wie Conventional Commits (z. B. `build`, `ci`, `docs`, `style`, `refactor`)?

Branches unterscheiden sich von Commits – sie sind temporär und werden hauptsächlich bis zum Merge verwendet. Zu viele Typen für Branches einzuführen, wäre unnötig und würde sie schwerer zu verwalten und zu merken machen.

### Kann ich eigene Branch-Typen über die aufgeführten hinaus definieren?

Ja, als Erweiterung auf Teamebene. Die Typen in der Grammatik sind die, die jedes konforme Werkzeug akzeptiert; ein Branch wie `unknown/some-task` ist nach der Spezifikation selbst daher ungültig. Braucht ein Team weitere Typen (etwa `experiment/`), sollte es sie in seinem Validator ausdrücklich eintragen (zum Beispiel unter `allow_branch_types` in [commit-check](/enforce/#commit-check)) und dokumentieren, damit Teammitglieder und automatisierte Werkzeuge übereinstimmen. Das Repository der Spezifikation selbst ergänzt zum Beispiel in seiner [commit-check-Konfiguration](https://github.com/conventional-branch/conventional-branch/blob/main/commit-check.toml) `dependabot/` für die Branches, die Dependabot anlegt.

### Warum müssen Branch-Namen kleingeschrieben werden?

Aus zwei Gründen. Erstens speichert Git Branch-Referenzen meist als Dateien unter `.git/refs/heads/`, und die Standard-Dateisysteme von macOS und Windows unterscheiden nicht zwischen Groß- und Kleinschreibung: `Feature/login` und `feature/login` landen dort auf demselben Pfad, unter Linux sind es aber zwei verschiedene Branches. Ein Repository, das beides zulässt, kann sich deshalb von Klon zu Klon unterschiedlich verhalten. Zweitens ist eine einzige Schreibweise leichter zu tippen, zu suchen und abzugleichen: Ein Werkzeug, das auf `release/*` reagiert, muss nicht auch noch `Release/*` berücksichtigen.

### Was sind die Hauptunterschiede zwischen v1.1.0 und v1.0.0?

v1.1.0 führt **AI-Agenten-Quellpräfixe** als wichtigstes neues Feature ein (siehe den nächsten FAQ-Eintrag für die Gründe). Außerdem bietet die versionierte Website einen Versionsumschalter, mit dem Benutzer sowohl die v1.0.0- als auch die v1.1.0-Spezifikation durchsuchen können. Alle vorhandenen v1.0.0-Branch-Namen bleiben vollständig gültig — keine breaking changes.

### Warum AI-Agenten-Quellpräfixe hinzufügen?

KI-Codierungsagenten (GitHub Copilot, Cursor, Claude Code, OpenAI Codex usw.) werden zunehmend zur Codegenerierung und Erstellung von Pull Requests eingesetzt. Jeder Agent verwendet sein eigenes Branch-Präfix (z. B. `copilot/`, `cursor/`). Durch die Standardisierung dieser Präfixe in der Conventional-Branch-Spezifikation ermöglichen wir:
1. **Schnelle Identifikation** — Prüfer und Tools können KI-generierte PRs sofort erkennen
2. **Tool-Validierung** — Tools wie commit-check können KI-Agenten-Branches gegen die Spezifikation validieren
3. **Eine stabile Liste** — die fünf Präfixe stehen fest, und jeder andere Agent verwendet `ai/`, sodass sich die Grammatik nicht mit jedem neuen Werkzeug ändert

Der generische `ai/`-Präfix steht für jeden KI-Agenten ohne dedizierten Präfix zur Verfügung, oder für Teams, die einen anbieterneutralen Identifikator bevorzugen. Dies ist das wichtigste neue Feature, das in **v1.1.0** veröffentlicht wurde — eine vollständige Zusammenfassung der Änderungen zwischen den Versionen finden Sie im FAQ-Eintrag oben.

### Wie soll ich mit langlebigen Branches wie `develop` oder `staging` umgehen?

In der formalen Grammatik dieser Spezifikation sind nur `main`, `master` und `develop` explizit als Trunk-Branches definiert und benötigen kein Präfix. Als projektspezifische Erweiterung können Teams jedoch zusätzliche langlebige Integrations- oder Umgebungs-Branches (z. B. `staging`, `production`) ohne Präfix verwenden, sofern diese konsistent benannt und in den eingesetzten Tools entsprechend konfiguriert bzw. dokumentiert sind.

### Welche Tools können verwendet werden, um automatisch zu identifizieren, ob ein Teammitglied diese Spezifikation nicht erfüllt?

Sie können [commit-check](https://github.com/commit-check/commit-check) verwenden, um die Branch-Spezifikation zu überprüfen, oder [commit-check-action](https://github.com/commit-check/commit-check-action), wenn Ihr Code auf GitHub gehostet wird.

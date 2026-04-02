---
draft: false
aliases: ["/de/"]
layout: single
---

# Conventional Branch 1.0.0

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

- **`main`**: Der Haupt-Entwicklungsbranch (z.B. `main`, `master`, oder `develop`)
- **`feature/`** (oder **`feat/`**): Für neue Features (z.B. `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (oder **`fix/`**): Für Fehlerbehebungen (z.B. `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`**: Für dringende Korrekturen (z.B. `hotfix/security-patch`)
- **`release/`**: Für Branches, die ein Release vorbereiten (z.B. `release/v1.2.0`)
- **`chore/`**: Für Nicht-Code-Aufgaben wie Abhängigkeiten, Dokumentation-Updates (z.B. `chore/update-dependencies`)

---

### Grundregeln

1. **Verwenden Sie kleine Buchstaben und Zahlen, Bindestriche und Punkte**: Verwenden Sie immer Kleinbuchstaben (`a-z`), Zahlen (`0-9`) und Bindestriche (`-`), um Wörter zu trennen. Vermeiden Sie Sonderzeichen, Unterstriche oder Leerzeichen. Für Release-Branches können Punkte (`.`) in der Beschreibung verwendet werden, um Versionsnummern darzustellen (z.B. `release/v1.2.0`).
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
| `chore/update-dependencies` | ✅ | Nicht-Code-Aufgabe |
| `feature/issue-123-new-login` | ✅ | Feature mit Ticket-Nummer |
| `Feature/Add-Login` | ❌ | Großbuchstaben nicht erlaubt |
| `feature/new--login` | ❌ | Aufeinanderfolgende Bindestriche nicht erlaubt |
| `feature/-new-login` | ❌ | Beschreibung darf nicht mit Bindestrich beginnen |
| `feature/new-login-` | ❌ | Beschreibung darf nicht mit Bindestrich enden |
| `release/v1.-2.0` | ❌ | Bindestrich neben Punkt nicht erlaubt |
| `fix/header bug` | ❌ | Leerzeichen nicht erlaubt |
| `fix/header_bug` | ❌ | Unterstriche nicht erlaubt |
| `unknown/some-task` | ❌ | Unbekannter Präfixtyp |

## Fazit

- **Klare Kommunikation**: Der Branch-Name allein bietet ein klares Verständnis seines Zwecks und der Code-Änderung.
- **Automatisierungsfreundlich**: Lässt sich einfach in Automatisierungsprozesse einbinden (z.B. verschiedene Workflows für `feature`, `release`, etc.).
- **Skalierbarkeit**: Funktioniert gut in großen Teams, wo viele Entwickler gleichzeitig an verschiedenen Aufgaben arbeiten.

Zusammenfassend ist Conventional Branch darauf ausgelegt, die Projektorganisation, Kommunikation und Automatisierung innerhalb von Git-Workflows zu verbessern.

## FAQ

### Warum sind Branch-Typen nicht so detailliert wie Conventional Commits (z. B. `build`, `ci`, `docs`, `style`, `refactor`)?

Branches unterscheiden sich von Commits – sie sind temporär und werden hauptsächlich bis zum Merge verwendet. Zu viele Typen für Branches einzuführen, wäre unnötig und würde sie schwerer zu verwalten und zu merken machen.

### Welche Tools können verwendet werden, um automatisch zu identifizieren, ob ein Teammitglied diese Spezifikation nicht erfüllt?

Sie können [commit-check](https://github.com/commit-check/commit-check) verwenden, um die Branch-Spezifikation zu überprüfen, oder [commit-check-action](https://github.com/commit-check/commit-check-action), wenn Ihr Code auf GitHub gehostet wird.

### Kann ich eigene Branch-Typen über die aufgeführten hinaus definieren?

Ja. Die Spezifikation definiert eine empfohlene Menge von Typen, aber Teams können zusätzliche benutzerdefinierte Typen für ihren Workflow definieren. Es ist jedoch wichtig, benutzerdefinierte Typen klar zu dokumentieren, damit alle Teammitglieder und automatisierte Tools davon wissen.

### Wie verhält sich Conventional Branch zu Conventional Commits?

Conventional Branch wurde von [Conventional Commits](https://www.conventionalcommits.org) inspiriert und verfolgt eine ähnliche Philosophie: menschlich- und maschinenlesbaren Struktur in Git-Metadaten einzubringen. Während Conventional Commits Commit-Nachrichten standardisiert, standardisiert Conventional Branch Branch-Namen. Die beiden Spezifikationen ergänzen sich auf natürliche Weise.

### Wie soll ich mit langlebigen Branches wie `develop` oder `staging` umgehen?

Langlebige Integrations- oder Umgebungs-Branches (z. B. `develop`, `staging`, `production`) werden als Trunk-Branches behandelt und benötigen kein Präfix. Sie sollten im gesamten Projekt einheitlich benannt werden.


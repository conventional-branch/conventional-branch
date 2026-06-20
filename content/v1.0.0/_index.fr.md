---
draft: false
layout: single
version: v1.0.0
---

# Conventional Branch 1.0.0

## Résumé

Conventional Branch fait référence à une convention de nommage structurée et standardisée pour les branches Git qui vise à rendre les branches plus lisibles et exploitables. Nous avons suggéré quelques préfixes de branches que vous pourriez vouloir utiliser, mais vous pouvez également spécifier votre propre convention de nommage. Une convention de nommage cohérente facilite l'identification des branches par type.

### Points clés

1. **Noms de branches orientés objectif** : Chaque nom de branche indique clairement son objectif, facilitant la compréhension par tous les développeurs de l'objet de la branche.
2. **Intégration avec CI/CD** : En utilisant des noms de branches cohérents, cela peut aider les systèmes automatisés (comme les pipelines d'intégration continue/déploiement continu) à déclencher des actions spécifiques en fonction du type de branche (par exemple, déploiement automatique depuis les branches de release).
3. **Collaboration d'équipe** : Cela encourage la collaboration au sein des équipes en rendant explicite l'objectif de la branche, réduisant les malentendus et facilitant le passage d'une tâche à l'autre pour les membres de l'équipe sans confusion.

## Spécification

### Préfixes de nommage des branches

La spécification des branches prend en charge les préfixes suivants et doit être structurée comme suit :

---

```
<type>/<description>
```

- **`main`** : La branche de développement principale (par exemple, `main`, `master`, ou `develop`)
- **`feature/`** (ou **`feat/`**) : Pour les nouvelles fonctionnalités (par exemple, `feature/add-login-page`, `feat/add-login-page`)
- **`bugfix/`** (ou **`fix/`**) : Pour les corrections de bugs (par exemple, `bugfix/fix-header-bug`, `fix/header-bug`)
- **`hotfix/`** : Pour les corrections urgentes (par exemple, `hotfix/security-patch`)
- **`release/`** : Pour les branches préparant une release (par exemple, `release/v1.2.0`)
- **`chore/`** : Pour les tâches non liées au code comme les dépendances, les mises à jour de documentation (par exemple, `chore/update-dependencies`)

---

### Règles de base

1. **Utilisez des caractères alphanumériques en minuscules, des tirets et des points** : Utilisez toujours des lettres minuscules (`a-z`), des chiffres (`0-9`), et des tirets (`-`) pour séparer les mots. Évitez les caractères spéciaux, les underscores, ou les espaces. Pour les branches de release, les points (`.`) peuvent être utilisés dans la description pour représenter les numéros de version (par exemple, `release/v1.2.0`).
2. **Pas de tirets ou points consécutifs, en début ou en fin** : Assurez-vous que les tirets et les points n'apparaissent pas de manière consécutive (par exemple, `feature/new--login`, `release/v1.-2.0`), ni au début ou à la fin de la description (par exemple, `feature/-new-login`, `release/v1.2.0.`).
3. **Restez clair et concis** : Le nom de la branche doit être descriptif mais concis, indiquant clairement l'objectif du travail.
4. **Incluez les numéros de ticket** : Le cas échéant, incluez le numéro de ticket de votre outil de gestion de projet pour faciliter le suivi. Par exemple, pour un ticket `issue-123`, le nom de la branche pourrait être `feature/issue-123-new-login`.


### Grammaire formelle

La grammaire ABNF (Augmented Backus-Naur Form) suivante définit formellement les noms de branches valides :

```abnf
branch-name     = trunk-branch / prefixed-branch
trunk-branch    = "main" / "master" / "develop"
prefixed-branch = type "/" description
type            = "feature" / "feat" / "bugfix" / "fix"
                / "hotfix" / "release" / "chore"
description     = desc-segment *("-" desc-segment)
desc-segment    = 1*(ALPHA / DIGIT) *("." 1*(ALPHA / DIGIT))
ALPHA           = %x61-7A   ; lettres minuscules a-z
DIGIT           = %x30-39   ; chiffres 0-9
```

> Remarque : Les tirets ou points consécutifs, ainsi que les tirets ou points en début ou en fin de description, ne sont pas autorisés.

### Exemples

| Nom de branche | Valide | Notes |
|---|---|---|
| `main` | ✅ | Branche principale |
| `master` | ✅ | Branche principale |
| `develop` | ✅ | Branche principale |
| `feature/add-login-page` | ✅ | Nouvelle fonctionnalité |
| `feat/add-login-page` | ✅ | Alias court pour feature |
| `bugfix/fix-header-bug` | ✅ | Correction de bug |
| `fix/header-bug` | ✅ | Alias court pour bugfix |
| `hotfix/security-patch` | ✅ | Correction urgente |
| `release/v1.2.0` | ✅ | Release avec numéro de version |
| `chore/update-dependencies` | ✅ | Tâche non liée au code |
| `feature/issue-123-new-login` | ✅ | Fonctionnalité avec numéro de ticket |
| `Feature/Add-Login` | ❌ | Majuscules non autorisées |
| `feature/new--login` | ❌ | Tirets consécutifs non autorisés |
| `feature/-new-login` | ❌ | La description ne peut pas commencer par un tiret |
| `feature/new-login-` | ❌ | La description ne peut pas se terminer par un tiret |
| `release/v1.-2.0` | ❌ | Tiret adjacent à un point non autorisé |
| `fix/header bug` | ❌ | Espaces non autorisés |
| `fix/header_bug` | ❌ | Underscores non autorisés |
| `unknown/some-task` | ❌ | Type de préfixe inconnu |

## Conclusion

- **Communication claire** : Le nom de la branche seul fournit une compréhension claire de son objectif et du changement de code.
- **Compatible avec l'automatisation** : S'intègre facilement dans les processus d'automatisation (par exemple, différents workflows pour `feature`, `release`, etc.).
- **Évolutivité** : Fonctionne bien dans les grandes équipes où de nombreux développeurs travaillent simultanément sur différentes tâches.

En résumé, conventional branch est conçu pour améliorer l'organisation du projet, la communication et l'automatisation dans les workflows Git.

## Outils

{{< tooling compact >}}

## FAQ

### Pourquoi les types de branches ne sont-ils pas aussi détaillés que les Conventional Commits (par ex. `build`, `ci`, `docs`, `style`, `refactor`) ?

Les branches sont différentes des commits : elles sont temporaires et principalement utilisées jusqu’à leur fusion. Introduire trop de types pour les branches serait inutile et rendrait leur gestion et mémorisation plus difficiles.

### Quels outils peuvent être utilisés pour identifier automatiquement si un membre de l'équipe ne respecte pas cette spécification ?

Vous pouvez utiliser [commit-check](https://github.com/commit-check/commit-check) pour vérifier la spécification des branches ou [commit-check-action](https://github.com/commit-check/commit-check-action) si vos codes sont hébergés sur GitHub.

### Puis-je définir mes propres types de branches au-delà de ceux listés ?

Oui. La spécification définit un ensemble de types recommandés, mais les équipes peuvent définir des types personnalisés supplémentaires pour leur flux de travail. Il est cependant important de documenter clairement les types personnalisés afin que tous les membres de l'équipe et les outils automatisés en soient informés.

### Comment Conventional Branch se rapporte-t-il à Conventional Commits ?

Conventional Branch est inspiré par [Conventional Commits](https://www.conventionalcommits.org) et suit une philosophie similaire : apporter une structure lisible par les humains et les machines aux métadonnées Git. Tandis que Conventional Commits standardise les messages de commit, Conventional Branch standardise les noms de branches. Les deux spécifications se complètent naturellement.

### Comment gérer les branches à longue durée de vie comme `develop` ou `staging` ?

Les branches d'intégration ou d'environnement à longue durée de vie (par ex., `develop` ou, de façon spécifique au projet, `staging`, `production`) sont traitées comme des branches principales et ne nécessitent pas de préfixe. Dans la grammaire formelle ci‑dessus, seules les branches `main`/`master`/`develop` sont normalisées en tant que `trunk-branch` ; d'autres noms comme `staging` ou `production` relèvent d'extensions propres au projet et doivent être documentés et configurés explicitement dans les outils de validation. Elles doivent être nommées de manière cohérente dans tout le projet.

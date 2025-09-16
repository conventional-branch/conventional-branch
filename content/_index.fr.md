---
draft: false
aliases: ["/fr/"]
layout: single
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

## Conclusion

- **Communication claire** : Le nom de la branche seul fournit une compréhension claire de son objectif et du changement de code.
- **Compatible avec l'automatisation** : S'intègre facilement dans les processus d'automatisation (par exemple, différents workflows pour `feature`, `release`, etc.).
- **Évolutivité** : Fonctionne bien dans les grandes équipes où de nombreux développeurs travaillent simultanément sur différentes tâches.

En résumé, conventional branch est conçu pour améliorer l'organisation du projet, la communication et l'automatisation dans les workflows Git.

## FAQ

### Quels outils peuvent être utilisés pour identifier automatiquement si un membre de l'équipe ne respecte pas cette spécification ?

Vous pouvez utiliser [commit-check](https://github.com/commit-check/commit-check) pour vérifier la spécification des branches ou [commit-check-action](https://github.com/commit-check/commit-check-action) si vos codes sont hébergés sur GitHub.
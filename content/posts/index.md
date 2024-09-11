---
draft: false
aliases: ["/en/"]
---

# Conventional Branch 1.0.0

## Summary

The Conventional Branch specification to define a branch based workflow for your project. When you map your workflow to branch types, you can ensure that branches are named consistently by configuring which branch types to make available. We've suggested some branch prefixes you might want to use but you can also specify your own naming convention. A consistent naming convention makes it easier to identify branches by type. You can also define which branches are your development and production branches, which allows us to better suggest source and target branches for creation and pull requests.

## Specification

The branch specification by describing with `feature`, `bugfix`, `release` `hotfix` and it should be structured as follows:

---

```
<type>/<description>
```
---

<br />
The branch contains the following structural elements, to communicate intent to the
consumers of your library:

1. **feature/:** Used for specific feature work or improvements. Generally branches from, and merges back into, the development branch, using pull requests.
2. **bugfix/** Typically used to fix Release branches.
3. **release/** Used for release tasks and long-term maintenance versions. They are branched from the development branch and then merged into the production branch.
4. **hotfix/** Used to quickly fix a Production branch without interrupting changes in the development branch. In a Git-based workflow, changes are usually merged into the production and development branches.

## Examples

### Branch with description

```
feature/support-cmake-build
bugfix/adjust-makefile
hotfix/upgrade-log4j-to-fix-vulnerabilities
```

### Branch with ticket number


```
feature/ABC-1234
bugfix/DEF-2345
hotfix/XYZ-6789
release/XYZ-6789
```

### Branch with version number

```
release/1.1.0
```

## Why Use Conventional Branch

* Communicating the nature of changes to teammates, the public, and other stakeholders.
* Triggering build and publish processes.
* Making it easier for people to contribute to your projects, by allowing them to explore
  a more structured branch history.

## FAQ

### What tools can be used to automatically identify if a team member does not meet this specification?

You can used [conventional-branch](https://github.com/conventional-branch/conventional-branch) to check branch specification or [conventional-branch-action](https://github.com/conventional-branch/conventional-branch-action) if your codes are hosted on GitHub.

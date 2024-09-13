---
draft: false
aliases: ["/en/"]
layout: single
---

# Conventional Branch 1.0.0

## Summary

The Conventional Branch specification to define a branch based workflow for your project. When you map your workflow to branch types, you can ensure that branches are named consistently by configuring which branch types to make available. We've suggested some branch prefixes you might want to use but you can also specify your own naming convention. A consistent naming convention makes it easier to identify branches by type.

## Specification

The branch specification by describing with `feature`, `bugfix`, `release` `hotfix` and it should be structured as follows:

---

```
<type>/<description>
```
---

There are several types of branches that are frequently used in software development. This table explains what each branch type is for, and the typical prefix convention for each branch type. 

|Branch types   | Branch name  | Description  |
|--------------|--------------|--------------|
|Development branch |`main`, `master`, `develop`   |Usually the integration branch for feature work and is often the default branch or a named branch. For pull request workflows, the branch where new feature branches are targeted.   |
|Feature branch     |`feature/`  | Used for specific feature work or improvements. Generally branches from, and merges back into, the development branch, using pull requests.  |
|Bugfix branch      |`bugfix/`   | Typically used to fix issues for any branches.   |
|Hotfix branch      |`hotfix/`   | Used to quickly fix a Production branch without interrupting changes in the development branch. In a Git-based workflow, changes are usually merged into the production and development branches.   |
|Release branch     |`release/`  | Used for release tasks and long-term maintenance versions. They are branched from the development branch and then merged into the production branch.   |

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
* Triggering specific types of build and publish processes.
* Making it easier for people to contribute to your projects, by allowing them to explore a more structured branch history.

## FAQ

### What tools can be used to automatically identify if a team member does not meet this specification?

You can used [commit-check](https://github.com/commit-check/commit-check) to check branch specification or [commit-check-action](https://github.com/commit-check/commit-check-action) if your codes are hosted on GitHub.

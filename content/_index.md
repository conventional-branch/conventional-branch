---
draft: false
aliases: ["/en/"]
layout: single
---

# Conventional Branch 1.0.0

## Summary

Git's Conventional Branch refers to a structured and standardized naming convention for Git branches which aims to make branch more readable and actionable. We've suggested some branch prefixes you might want to use but you can also specify your own naming convention. A consistent naming convention makes it easier to identify branches by type.

## Specification

The branch specification by describing with `feature/`, `bugfix/`, `hotfix/`, `release/` and `chore/` and it should be structured as follows:

---

```
<type>/<description>
```
---

## Key Points of Conventional Branch:

1. **Purpose-driven Branch Names**: Each branch name clearly indicates its purpose, making it easy for all developers to understand what the branch is for. Common formats include:

   - **main**: The main development branch (e.g., `main`, `master`, or `develop`)
   - **feature/**: For new features (e.g., `feature/add-login-page`)
   - **bugfix/**: For bug fixes (e.g., `bugfix/fix-header-bug`)
   - **hotfix/**: For urgent fixes (e.g., `hotfix/security-patch`)
   - **release/**: For branches preparing a release (e.g., `release/v1.2.0`)
   - **chore/**: For non-code tasks like dependency updates (e.g., `chore/update-dependencies`)

2. **Integration with CI/CD**: By using consistent branch names, it can help automated systems (like Continuous Integration/Continuous Deployment pipelines) to trigger specific actions based on the branch type (e.g., auto-deployment from release branches).

3. **Team Collaboration** : It encourages collaboration within teams by making branch purpose explicit, reducing misunderstandings and making it easier for team members to switch between tasks without confusion.

### Benefits:

- **Clear Communication**: The branch name alone provides a clear understanding of its purpose without needing to dig into the code.
- **Improved History**: When used with Conventional Commits, it ensures a clean and organized commit history.
- **Automation-Friendly**: Easily hooks into automation processes (e.g., different workflows for `feature`, `release`, etc.).
- **Scalability**: Works well in large teams where many developers are working on different tasks simultaneously.

In summary, conventional branch naming is designed to improve project organization, communication, and automation within Git workflows.

## FAQ

### What tools can be used to automatically identify if a team member does not meet this specification?

You can used [commit-check](https://github.com/commit-check/commit-check) to check branch specification or [commit-check-action](https://github.com/commit-check/commit-check-action) if your codes are hosted on GitHub.

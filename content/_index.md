---
draft: false
aliases: ["/en/"]
layout: single
---

# Conventional Branch 1.0.0

## Summary

Conventional Branch refers to a structured and standardized naming convention for Git branches which aims to make branch more readable and actionable. We've suggested some branch prefixes you might want to use but you can also specify your own naming convention. A consistent naming convention makes it easier to identify branches by type.

### Key Points

1. **Purpose-driven Branch Names**: Each branch name clearly indicates its purpose, making it easy for all developers to understand what the branch is for.
2. **Integration with CI/CD**: By using consistent branch names, it can help automated systems (like Continuous Integration/Continuous Deployment pipelines) to trigger specific actions based on the branch type (e.g., auto-deployment from release branches).
3. **Team Collaboration** : It encourages collaboration within teams by making branch purpose explicit, reducing misunderstandings and making it easier for team members to switch between tasks without confusion.

## Specification

### Branch Naming Prefixes

The branch specification by describing with `feature/`, `bugfix/`, `hotfix/`, `release/` and `chore/` and it should be structured as follows:

---

```
<type>/<description>
```

- **main**: The main development branch (e.g., `main`, `master`, or `develop`)
- **feature/**: For new features (e.g., `feature/add-login-page`)
- **bugfix/**: For bug fixes (e.g., `bugfix/fix-header-bug`)
- **hotfix/**: For urgent fixes (e.g., `hotfix/security-patch`)
- **release/**: For branches preparing a release (e.g., `release/v1.2.0`)
- **chore/**: For non-code tasks like dependency, docs updates (e.g., `chore/update-dependencies`)

---

### Basic Rules

1. **Lowercase and Hyphen-Separated**: Always use lowercase letters, and separate words with hyphens. For example, `feature/new-login` or `bugfix/header-styling`.
2. **Alphanumeric and Hyphens Only**: Use only lowercase letters (a-z), numbers (0-9), and hyphens. Avoid special characters like spaces, punctuation, and underscores.
3. **No Consecutive Hyphens**: Ensure that hyphens are used singly, with no consecutive hyphens (e.g., `feature/new-login`, not `feature/new--login`).
4. **No Trailing Hyphens**: Do not add a hyphen at the end of the branch name. For instance, use `feature/new-login` instead of `feature/new-login-`.
5. **Clear and Concise**: Make branch names descriptive but concise. The name should clearly indicate the work being done.
6. **Include Jira (or Other Tool) Ticket Numbers**: If applicable, include the ticket number from your project management tool to make tracking easier. For example, for a ticket `issue-123`, the branch name could be `feature/issue-123-new-login`.

## Conclusion

- **Clear Communication**: The branch name alone provides a clear understanding of its purpose the code change.
- **Automation-Friendly**: Easily hooks into automation processes (e.g., different workflows for `feature`, `release`, etc.).
- **Scalability**: Works well in large teams where many developers are working on different tasks simultaneously.

In summary, conventional branch is designed to improve project organization, communication, and automation within Git workflows.

## FAQ

### What tools can be used to automatically identify if a team member does not meet this specification?

You can used [commit-check](https://github.com/commit-check/commit-check) to check branch specification or [commit-check-action](https://github.com/commit-check/commit-check-action) if your codes are hosted on GitHub.

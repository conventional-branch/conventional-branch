# hugo Conventional Branch theme
Copy hugo-conventional-branch-theme inside your my-hugo-site/theme

## config.yaml example
All config params are optionals.
```yaml
baseURL: 'https://conventional-branch.github.io/'
languageCode: en-us
title: Conventional Branch
theme: conventional-branch

# Language
defaultContentLanguageInSubdir: true
defaultContentLanguage: "en"
languages:
  en:
    weight: 1
    languageName: "English"

# Content
params:
  versions:
    current: 1.0.0

  welcome:
    description: A specification made for write standardized and useful commit messages
    image: 'https://path-to-image'
    actions:
    - label: Read the specs
      url: 'https://github.com/conventional-branch/conventional-branch'
    - label: GitHub
      url: 'https://github.com/conventional-branch/conventional-branch'

  license:
    title: License
    action:
      label: Creative Commons - CC BY 3.0
      url: 'https://creativecommons.org/licenses/by/3.0/'

  footer:
    logos:
    - name: github
      url: 'https://github.com/conventional-branch/conventional-branch'
```

## Apply theme changes
Development script
```ssh
npm run start
```

Production script
```ssh
npm run build
```

## Shortcodes
* banner-image
  * src (optional) | default: static/img/git-flow.png
# Conventional Branch theme

The Hugo theme for [conventionalbranch.org](https://conventionalbranch.org/). It keeps the
look the site has had since 2024: every specification page opens with the site's name
and the branch mark in white on a blue gradient, and the text below reads like a README on
GitHub, near-black on white in the reader's system font with bold blue headings. Code and
the checker use a monospace (JetBrains Mono). The brand blue is `$color-primary`,
`#6699CC`, the version half of the adoption badge.

## Pages

- `_default/single.html` renders every language's specification page, current and
  archived: a hero, then the specification beside its outline. On a homepage whose
  language has `landing: true`, the checker, mission and adoption sections
  (`partials/home/`) follow it.
- `about/single.html` renders the About and Enforce pages: a hero from the page's front
  matter (`heroTitle`, `heroLead`), then the
  Markdown beside its outline.

Words come from the site's `i18n/` files, the homepage's lists from `data/home.yaml`, and
the checker's regex and types from `static/spec.json`.

## config.yaml

```yaml
theme: conventional-branch

markup:
  highlight:
    noClasses: false   # code is coloured by the theme's stylesheet

params:
  canonicalBaseURL: https://conventionalbranch.org/
  license:
    action:
      url: https://creativecommons.org/licenses/by/4.0/
  versions:
    current: v1.1.0
    list: ["v1.0.0", "v1.1.0"]

languages:
  en:
    params:
      weight: 1
      languageName: English
      title: Conventional Branch
      description: A specification for adding human and machine readable meaning to branch names
      landing: true      # show the homepage sections; their copy is in i18n/en.yaml
      actions:           # the hero's buttons, the first one primary
      - label: Read the specification
        url: "#spec"
```

## Building the assets

The stylesheet (`static/css/scss/`) and the script (`static/js/`) are compiled here;
the compiled files are not committed.

```sh
npm run start   # watch and rebuild while developing
npm run build   # minified, as CI builds it
```

## Shortcodes

- `banner-image` — `src` (optional), default `static/img/git-flow.png`

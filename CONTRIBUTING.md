# How to Contribute

## Repo Layout

We use [HUGO](https://gohugo.io/) as static site generator, so we use the [directory structure](https://gohugo.io/getting-started/directory-structure/) HUGO proposes.

#### Our implementation

* `./content/_index.md`: the **current** version of the specification, served at the site root (`/`). This is where changes to the in-progress version SHOULD be made.
* `./content/vX.Y.Z/`: archived snapshots of previously released versions (e.g. `./content/v1.0.0/`), browsable via the version switcher. These should not change once released.
* `./content/_index.[lang].md` and `./content/vX.Y.Z/_index.[lang].md`: translations of a given version. The default (English) file has no language code; every other language adds one (e.g. `_index.fr.md`).
* The list of versions and the current version are configured under `params.versions` in `./config.yaml`.

## Contributing

We'd love your help to suggest improvements to the specification, fixing typos, or adding more translations. Please don't hesitate to send a pull request.

### Adding a translation

1. Copy `./content/_index.md` to `./content/_index.[lang].md` (e.g. `_index.es.md`) and translate the content. If you also want the translation available for an archived version, repeat under the matching `./content/vX.Y.Z/` directory.
1. Ensure all files have the appropriate front matter fields required (see other language files as an example).
1. Add the language to the `languages` section of `./config.yaml` (see the existing entries as an example).
1. If your strings touch the tooling section, add the corresponding translations in `./data/tooling.yaml`.

### Registering a new AI agent prefix

The AI agent source prefixes (`ai/`, `copilot/`, `cursor/`, …) are stored in a single registry, [`./data/agents.yaml`](./data/agents.yaml). The specification website and the About page render this file as a table, so a new prefix only needs to be added in one place.

To register an agent:

1. Add an entry to the `agents:` list in `./data/agents.yaml`:
   ```yaml
   - prefix: youragent        # branch prefix, without the trailing slash
     name: Your Agent         # display name shown in the table
     vendor: Your Company     # organization behind the agent ("—" if none)
     homepage: https://...    # canonical product URL (the name links to it)
     since: "1.2.0"           # the spec version that adds the prefix
   ```
2. Keep the list roughly alphabetical after the generic `ai/` entry, and reuse an existing prefix rather than adding a near-duplicate.
3. Add the prefix to the `type` rule of the ABNF grammar and to the examples table in `./content/_index*.md` (and mention it in `CHANGELOG.md`), so the normative grammar stays in sync with the registry. This means **all eleven language files, not just the English one** — the conformance check holds every translation to the same examples and the same grammar, so missing one fails CI rather than shipping a page that contradicts the spec.
4. Add the prefix as a `type` (and update the `grammar.regex`) in [`./static/spec.json`](./static/spec.json), then run `python3 tests/conformance.py` to confirm everything still agrees. CI enforces this.

Guidelines for a good prefix:

- Use the agent's short, lowercase, well-known name (e.g. `copilot`, not `github-copilot`).
- It must satisfy the branch-name grammar: lowercase `a-z`, digits, no separators.
- Prefer registering a dedicated prefix over overloading `ai/`, which stays reserved as the vendor-neutral fallback.

### Adding your project to the adopters list

The "Projects Using Conventional Branch" list on the [About page](./content/about/index.md) is the canonical record of adopters, and a condensed excerpt is mirrored in the README's "Used By" section.

To add your project:

1. Add a bullet to the list in `./content/about/index.md`, linking to the file where your project documents the convention (e.g. your `CONTRIBUTING.md`) and a short one-line description. The link must point at a file that actually documents the convention — the list is evidence, not a directory.
   Entries are removed when that file stops referencing the specification. A project is free to move on, and a list that quietly keeps claiming it is worth less than a shorter honest one.
2. The list is roughly ordered by how widely recognized the organization is, so that it stays useful to skim. Add your entry wherever it fits; maintainers may move it.
3. Open a pull request. If your project is widely recognizable, it may also be added to the shorter curated list in `README.md`, at the maintainers' discretion.

### Changing the grammar or types

The specification has a machine-readable form in [`./static/spec.json`](./static/spec.json) (types, rules, ABNF, and a validation regex) with conformance cases in [`./tests/fixtures.json`](./tests/fixtures.json). If you change the grammar, the types, or the examples table, update `spec.json` and the fixtures to match and run:

```bash
python3 tests/conformance.py
```

It checks the fixtures, the docs examples table, and the agent registry against `spec.json`, and validates `spec.json` against [`./static/schema/v1/spec.schema.json`](./static/schema/v1/spec.schema.json). The same check runs in CI. See [`./tests/README.md`](./tests/README.md) for details.

Adding a property to `spec.json` means adding it to the schema too, otherwise the check rejects it as unexpected. Keep new properties optional: schema `v1` is a stability promise, so a change that would invalidate a document valid under it belongs in a `v2` at a new URL.

### Releasing a new version

The current version lives only at the site root (`./content/_index*.md`) — it is **not** duplicated under `./content/`. To cut a new version (e.g. `v1.2.0`):

1. Snapshot the version you are leaving behind: copy the current root files into `./content/<previous-version>/` (e.g. `./content/v1.1.0/`). This becomes an immutable archive browsable via the version switcher.
1. Edit the root `./content/_index*.md` files to reflect the new version.
1. In `./config.yaml`, append the new version to `params.versions.list` and set `params.versions.current` to it.
1. Bump `version` in [`./static/spec.json`](./static/spec.json) and freeze a copy of it under the new version:
   ```bash
   mkdir -p static/v1.2.0 && cp static/spec.json static/v1.2.0/spec.json
   ```
   Unlike the prose, the machine-readable spec is frozen *forward*, not backward: `./static/v<previous>/spec.json` already exists and must never be edited — downstream tools pin those URLs. `python3 tests/conformance.py` fails if the copy is missing or differs.
1. Update the three current-version references in [`./static/llms.txt`](./static/llms.txt) — the link title, the sentence introducing the version, and the frozen `spec.json` endpoint it tells tools to pin — along with the regex if the grammar changed. `python3 tests/conformance.py` fails if any of them still names the old version, since a language model reads that file and reports what it finds as fact.
1. Add the new endpoint to the `urls` list in [`./.github/workflows/url-check.yml`](./.github/workflows/url-check.yml), so a permanent URL that stops resolving opens an issue.
1. Update `CHANGELOG.md`.

The version switcher links the current version to the site root and every archived version to `/<version>/`, so there is a single source of truth for the live spec.

### Running project locally

There's a docker-compose.yml file ready that will help you to check if the website looks good!
To run it make sure you have [docker-compose installed](https://docs.docker.com/compose/install/#install-compose) on your machine and just use the command `docker-compose up` to make it run locally.

or you can run `make all-dev` to run the project locally.

Once the website will be compiled, you can see the website visiting `http://localhost:1313`

## Pull Requests

Conventional Branch use the [GitHub flow](https://guides.github.com/introduction/flow/) as main versioning workflow

1. Fork the conventional-branch repository
2. Create a new branch for each feature, fix or improvement
3. Send a pull request from each feature branch to the **main** branch

It is very important to separate new features or improvements into separate feature branches, and to send a pull request for each branch.

This allow us to review and pull in new features or improvements individually.

## License

You must agree that your patch will be licensed under the Conventional Branch Specification License, and when we change the license we will assume that you agreed with the change unless you object to the changes in time.

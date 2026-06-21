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

### Releasing a new version

The current version lives only at the site root (`./content/_index*.md`) — it is **not** duplicated under `./content/`. To cut a new version (e.g. `v1.2.0`):

1. Snapshot the version you are leaving behind: copy the current root files into `./content/<previous-version>/` (e.g. `./content/v1.1.0/`). This becomes an immutable archive browsable via the version switcher.
1. Edit the root `./content/_index*.md` files to reflect the new version.
1. In `./config.yaml`, append the new version to `params.versions.list` and set `params.versions.current` to it.
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

# How to Contribute

The contribution guideline is derived from the SlimPHP, Istanbul Code Coverage and Ruby contribution guideline

## Repo Layout

We use [HUGO](https://gohugo.io/) as static site generator, so we use the [directory structure](https://gohugo.io/getting-started/directory-structure/) HUGO proposes.

#### Our implementation

* `./content`: contains all the versions of the specification.
* `./content/next/`: contains the version of the specification (where all the changes SHOULD be made).
* `./content/**/index.[lang].md`: contains the content of the specification, if a language is specified it's a translation.

## Contributing

We'd love your help refining the language of this specification,
fixing typos, or adding more translations. Please don't hesitate
to send a pull request.

### Adding a translation

1. Create a new file in `./content/version/index.[lang].md` using the hugo command `hugo new [version]/index.[lang].md`.
1. Ensure all files have the appropriate fields required (see others as an example)..
1. Add the language to the `config.yaml` file (see others as an example).

### Running project locally

There's a docker-compose.yml file ready that will help you to check if the website looks good!
To run it make sure you have [docker-compose installed](https://docs.docker.com/compose/install/#install-compose) on your machine and just use the command `docker-compose up` to make it run locally.

Once the website will be compiled, you can see the website visiting `http://localhost:1313`

## Contributor Behavior

Be kind to one another. We're striving to make Conventional Branch an inclusive environment that's great for first time open-source contributors.

tldr; we value constructive community interaction, over technical acumen.

## Pull Requests

Conventional Branch use the [GitHub flow](https://guides.github.com/introduction/flow/) as main versioning workflow

1. Fork the Conventional Branch repository
2. Create a new branch for each feature, fix or improvement
3. Send a pull request from each feature branch to the **master** branch

It is very important to separate new features or improvements into separate feature branches, and to send a
pull request for each branch.

This allow us to review and pull in new features or improvements individually.

## Style Guide

All pull requests SHOULD adhere to the [Conventional Branch specification](https://conventionalcommits.org/)

## License

You must agree that your patch will be licensed under the Conventional Commit License, and when we change the license we will assume that you agreed with the change unless you object to the changes in time.
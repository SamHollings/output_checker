# `output_checker`
![Build](https://github.com/SamHollings/output_checker/actions/workflows/ci.yml/badge.svg)
![pylint score](./outputs/ci-cd/pylint.svg "pylint score")
![flake8](./outputs/ci-cd/flake8.svg "flake8 status badge")
![pytest](./outputs/ci-cd/pytest.svg "pytest status badge")
![coverage](./outputs/ci-cd/coverage.svg "coverage status badge")
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


`output_checker` is a tool that allows **analysts** to check if their **code is ok to
export**

## **End Goal**
- Check some repo to ensure it's ok to remove from a secure environment
    - [ ] flag any large files
        - [x] function to calculate file size
    - [ ] flag any long files
        - [x] function to calculate file length
    - [ ] flag any CSVs, or other known data files
    - [ ] flag any images, artifacts etc.
    - [ ] scan files for hardcoded datastructures, e.g. embedded data, tokens
    - [ ] scan files for "entities" e.g. names, or other identifiers
    - [ ] scan notebooks to ensure they have had outputs cleared 
- Check "outputs" to ensure they are ok to remove from a secure environment 
    - [ ] make sure "data" outputs, e.g. CSV/parquet, etc. follow disclosure control rules
    - [ ] scan output files for entities
    - [ ] flag any long files
    - [ ] flag any large files

This will work by:
- pointing a checking function at a given directory and indicating if it contains code or data files
    - [ ] function which scans all files in a directory and applies the necessary checks
- This will return a table detailing each file in which there were problems, and which problems were found
    - [ ] functionality which returns all failures in a tabular form

This repo will also contain test cases to show it works correctly. E.g.
- [ ] example code files with and without harded datastructures, entities, etc.
- [ ] example data files with and without entities, and which pass and fail disclosure control etc.
- [ ] For large and long files - we need functions which can generate these on the fly

## Components

This will contain functions to do a few different checks for both data outputs and code.

**data outputs**:
- [ ] [Statistical Disclosure Control](./src/disclosure_control_check)

**code outputs**: 
- [ ] *ToDo*: Large files
- [ ] *ToDo*: Files which are too long
- [ ] *ToDo*: Entity Recognition
- [ ] *ToDo*: Embedded tables
- [ ] *ToDo*: notebooks without cleared outputs

Initially, we need to make simple functions which address the above, then we can build other functions which will apply them multiple files.

A core part of the use-case is that there is that people can be alerted what issues there are, in which files.

It does this by running a few simple checks. The envisaged workflow is:
```mermaid
graph LR
    A[Statistical Disclosure Control] --> B{Values below a threshold?};
    A --> C{Values not rounded?};
    B -->|Pass| D[Ok to output];
    B -->|Fail| E[Identifies problems];
    C -->|Pass| D[Ok to output];
    C -->|Fail| E[Identifies problems];

    click A "https://github.com/SamHollings/output_checker/tree/main/src/disclosure_control_check" "Disclosure Control code" _blank
```

## Getting started

To start using this project, [first make sure your system meets its
requirements](#requirements).

### Requirements

[```Contributors have some additional requirements!```][contributing]

- Python 3.6.1+ installed
- a `.secrets` file with the [required secrets and
  credentials](#required-secrets-and-credentials)
- [load environment variables][docs-loading-environment-variables] from `.env`

To install the Python requirements, open your terminal and enter:

```shell
pip install -r requirements.txt
```

## Required secrets and credentials

To run this project, [you need a `.secrets` file with secrets/credentials as
environmental variables][docs-loading-environment-variables-secrets]. The
secrets/credentials should have the following environment variable name(s):

| Secret/credential | Environment variable name | Description                                |
|-------------------|---------------------------|--------------------------------------------|
| Secret 1          | `SECRET_VARIABLE_1`       | Plain English description of Secret 1.     |
| Credential 1      | `CREDENTIAL_VARIABLE_1`   | Plain English description of Credential 1. |

Once you've added, [load these environment variables using
`.env`][docs-loading-environment-variables].

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Contributing

[If you want to help us build, and improve `output_checker`, view our
contributing guidelines][contributing].

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing]: ./docs/contributor_guide/CONTRIBUTING.md
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[docs-loading-environment-variables]: ./docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: ./docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials

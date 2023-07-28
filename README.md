# Bytewax Connector Template

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/6073079/195393689-7334098b-a8cd-4aaa-8791-e4556c25713e.png" width="350">
  <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/6073079/194626697-425ade3d-3d72-4b4c-928e-47bad174a376.png" width="350">
  <img alt="Bytewax">
</picture>

This project is a template for creating input connectors for [Bytewax](https://github.com/bytewax/bytewax).

## How to use this template

To create a new connector, click "Use this template" and create a new
repository. Start creating your connector by customizing
`pyproject.toml` to include any dependencies your connector requires, along
with any development dependencies.

For a completed example that uses this template, see [https://github.com/bytewax/bytewax-kafka](bytewax-kafka).

### Development

This template includes an optional set of development dependencies which can be
installed with `pip install .[dev]`. _If you get an error using `zsh` you may need to quote the path like this - `pip install '.[dev]'`_

This template also contains a configuration for using
[pre-commit](https://pre-commit.com/) hooks. You can install the pre-commit
hooks after running `pip install .[dev]` with `pre-commit install`.

### Testing

This project comes with an example `test` directory that uses
[pytest](https://docs.pytest.org/en/7.3.x/).

### Publishing

Included in this project are GitHub actions that will build and publish your
package to [PyPI](https://pypi.org/).

Publishing to PyPI using the GitHub Action configured here uses their
[Trusted Publishing](https://docs.pypi.org/trusted-publishers/)
framework. See the docs for configuring your project on PyPI.

This action is triggered when creating a GitHub
[release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
from a tagged version.

### Documentation

This project contains a GitHub action for building and publishing
documentation to GitHub Pages using
[Sphinx](https://www.sphinx-doc.org/en/master/).

To view the documentation locally, run `make html` from the `docs/` folder.

This action is triggered when creating a GitHub
[release](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)
from a tagged version.

## Building a connector for Bytewax

Included in this project is a skeleton implementation of
[PartitionedInput](https://bytewax.io/apidocs/bytewax.inputs#bytewax.inputs.PartitionedInput)
and
[DynamicInput](https://bytewax.io/apidocs/bytewax.inputs#bytewax.inputs.DynamicInput).

For more information about how to create custom connectors, see our
[API Docs](https://bytewax.io/apidocs/bytewax.inputs) and the [blog
post](https://bytewax.io/blog/custom-input-connector) that details
building a custom connector for Bytewax.

## Important things to keep in mind when building input connectors

### Don't call Python's `time.sleep`

It is important to yield control from your input connector to Bytewax
when processing input. Bytewax's runtime is based on a cooperative
multitasking model. Unless your code yields execution to Bytewax, no
progress will be made in processing items in your dataflow, and
important work like storing state for recovery will not take place.


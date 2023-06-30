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

### Development

This template includes an optional set of development dependencies which can be
installed with `pip install .[dev]`.

This template also contains a configuration for using
[pre-commit](https://pre-commit.com/), you can install the pre-commit
hooks after running `pip install .[dev]` with `pre-commit install`.

### Testing

This project comes with an example `test` directory that uses
[pytest](https://docs.pytest.org/en/7.3.x/).

### Publishing

Included in this project are GitHub actions that will build and publish your
package to [PyPI](https://pypi.org/).

## Building a connector for Bytewax

Included in this project is a skeleton implementation of [PartitionedInput](https://bytewax.io/apidocs/bytewax.inputs#bytewax.inputs.PartitionedInput) and [DynamicInput](https://bytewax.io/apidocs/bytewax.inputs#bytewax.inputs.DynamicInput).

## Important things to keep in mind when building input connectors

### Don't sleep!

It is important to yield control from your input connector to Bytewax
when processing input. Bytewax's runtime is based on a cooperative
multitasking model. Unless your code yields execution to Bytewax, no
progress will be made in processing items in your dataflow, and
important work like storing state for recovery will not take place.

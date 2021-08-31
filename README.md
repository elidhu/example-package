# Example package
A very small example package to demonstrate the `flit` build backend and a `setup.py` free python package.

## Initial package setup
Roughly in this order...

### Create the venv
```
python3 -m venv venv
```

### Activate it
```
source venv/bin/activate
```

### Install flit
This is the build backend, nothing will work without this. This is **INSTEAD** of setuptools. The reason is it provides a much much much simpler configuration for basic python-only packages.
```
pip install flit
```

### Init the package
Use the `flit init` tool (or copy paste an existing `pyproject.toml`)
```
flit init
```

## Develop install
So that all code changes are present in the environment immediately without having to reinstall your package. This is the equivalent of the old `pip install -e .`
```
flit install
```

## Adding new dependencies
Add these to `project.dependencies` in the `pyproject.toml`.

## Running tests
Unittest will auto-discover test files that are named like `test*.py`. See [here](https://docs.python.org/3/library/unittest.html#test-discovery)
```
python -m unittest
```
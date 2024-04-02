# Template

This repository contains setup files for python projects.


# Getting Started

```
>>> conda env create -f env.yaml
```

```
>>> conda activate <environment name>
```

## For Development
```
>>> pip install -e .[dev]
```
### Upload to PYPI
```
>>> python -m build
>>> python -m twine upload dist/*
```

## For Non-Development Purposes
```
>>> pip install -e

# SubsCrypt Python Package
[![Python Test](https://github.com/oxydev/SubsCrypt-python-package/actions/workflows/test.yml/badge.svg)](https://github.com/oxydev/SubsCrypt-python-package/actions/workflows/test.yml)
[![PyPI license](https://img.shields.io/pypi/l/subscrypt.svg)](https://pypi.python.org/pypi/subscrypt/)
[![PyPI version fury.io](https://badge.fury.io/py/subscrypt.svg)](https://pypi.python.org/pypi/subscrypt/)

The python interface for interacting with SubsCrypt Service.

<img src="https://oxydev.github.io/SubsCrypt-docs/images/logo.jpg" width="400">

# Installation

```bash
$> pip install subscrypt
```

# Getting Started

```python
>>> from subscrypt import Subscrypt
>>> subscrypt_client = Subscrypt()
>>> subscrypt_client.is_connected()
True
```

# Docs

This service is a RESTful API and you can see our api documentation [here](http://206.189.154.160:3000/subscrypt-doc).

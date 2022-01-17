# mdut

**mdut** (pronounced "em-doot") is a tool for generating Markdown URL tags.
It ships as both a standalone command-line program and Python library.

[![GitHub Actions](https://github.com/nkantar/mdut/actions/workflows/automated_checks.yml/badge.svg?branch=main)](https://github.com/nkantar/mdut/actions/workflows/code-quality-checks.yml)
[![PyPI version](https://badge.fury.io/py/mdut.svg)](https://badge.fury.io/py/mdut)
[![Unreleased changes](https://img.shields.io/github/commits-since/nkantar/mdut/22.3.1)](https://github.com/nkantar/mdut/blob/main/CHANGELOG.md#unreleased)
[![License: MIT](https://img.shields.io/github/license/nkantar/mdut)](https://github.com/nkantar/mdut/blob/main/LICENSE)


## Examples

Command-line program:

```
# reference style is default
$ mdut https://example.com
Copied to clipboard:
[TODO]: https://example.com "Example Domain"

$ mdut -s inline https://example.com
Copied to clipboard:
[TODO](https://example.com "Example Domain")

$ mdut -s slack https://example.com
Copied to clipboard:
[TODO](https://example.com)
```

Python library:

```python
>>> import mdut
>>> mdut.reference("https://example.com")
'[TODO]: https://example.com "Example Domain"'
>>> mdut.inline("https://example.com")
'[TODO](https://example.com "Example Domain")'
>>> mdut.slack("https://example.com")
'[TODO](https://example.com)'
```


## Installation

If you plan on using mdut on the command-line, you're probably best off installing it via [pipx], like so:

```
pipx install mdut
```

However, if you plan on using mdut as a library in your project, you should probably install it the same way as your other dependencies, for example via pip, Poetry, Pipenv, etc.

```
# pip
pip install mdut

# Poetry
poetry add mdut

# Pipenv
pipenv install mdut
```


[pipx]: https://pypa.github.io/pipx/ "pipx"

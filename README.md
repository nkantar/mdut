# mdut

**mdut** (pronounced "em-doot") is a tool for generating Markdown URL tags.
It ships as both a standalone command-line program and Python library.


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
```

Python library:

```python
>>> import mdut
>>> mdut.reference("https://example.com")
'[TODO]: https://example.com "Example Domain"'
>>> mdut.inline("https://example.com")
'[TODO](https://example.com "Example Domain")'
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

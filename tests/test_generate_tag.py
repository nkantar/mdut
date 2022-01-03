import pytest

from src.mdut import generate_tag


@pytest.mark.parametrize(
    "url,title,tag",
    [
        ("foo", "bar", '[TODO](foo "bar")'),
        ("foo", "", '[TODO](foo "")'),
        ("foo", None, '[TODO](foo "TODO")'),
    ],
)
def test_inline(url, title, tag):
    assert generate_tag(url, title, "inline") == tag

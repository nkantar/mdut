import pytest

from mdut.mdut import generate_tag


@pytest.mark.parametrize(
    "url,title,tag",
    [
        ("foo", "bar", '[TODO]: foo "bar"'),
        ("foo", "", '[TODO]: foo ""'),
        ("foo", None, '[TODO]: foo "TODO"'),
    ],
)
def test_reference(url: str, title: str, tag: str) -> None:
    assert generate_tag(url, title, "reference") == tag


@pytest.mark.parametrize(
    "url,title,tag",
    [
        ("foo", "bar", '[TODO](foo "bar")'),
        ("foo", "", '[TODO](foo "")'),
        ("foo", None, '[TODO](foo "TODO")'),
    ],
)
def test_inline(url: str, title: str, tag: str) -> None:
    assert generate_tag(url, title, "inline") == tag


@pytest.mark.parametrize(
    "url,title,tag",
    [
        ("foo", "bar", "[TODO](foo)"),
        ("foo", "", "[TODO](foo)"),
        ("foo", None, "[TODO](foo)"),
    ],
)
def test_slack(url: str, title: str, tag: str) -> None:
    assert generate_tag(url, title, "slack") == tag

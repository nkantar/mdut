import pytest

from mdut.mdut import extract_title


@pytest.mark.parametrize(
    "html,title",
    [
        ("<html><head><title>foo</title></head></html>", "foo"),
        ("<html><head><title>bar</title>", "bar"),
        ("<html><head><title>baz</head></html>", "baz"),
        ('<html><head><title>b"a“r”f</title></head></html>', 'b\\"a“r”f'),
        (
            (
                "<head><title> \t 2018 Yamaha XSR700 Sport Heritage Motorcycle - Model "
                "Home \t </title></head>"
            ),
            "2018 Yamaha XSR700 Sport Heritage Motorcycle - Model Home",
        ),
    ],
)
def test_valid(html: str, title: str) -> None:
    assert extract_title(html) == title


@pytest.mark.parametrize(
    "html",
    [
        "<html><head></head></html>",
        "<html><body><title>nope</body></html>",
        "foo",
        "",
        None,
        13,
        int,
    ],
)
def test_invalid(html: str) -> None:
    assert extract_title(html) == "TODO"

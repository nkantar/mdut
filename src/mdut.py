from string import Template

from bs4 import BeautifulSoup
import click
import httpx
import pyperclip  # type: ignore


TODO = "TODO"

TAG_STYLES = {
    "inline": Template('[TODO]($url "$title")'),
    "reference": Template('[TODO]: $url "$title"'),
}

DEFAULT_STYLE = "reference"


def fetch_html(url: str) -> str:
    return httpx.get(url).text


def extract_title(html: str) -> str:
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = getattr(getattr(getattr(soup, "head"), "title"), "text") or TODO
    except (AttributeError, TypeError):
        title = TODO
    return title


def generate_tag(url: str, title: str | None, style: str = DEFAULT_STYLE) -> str:
    if title is None:
        title = TODO
    return TAG_STYLES[style].substitute(url=url, title=title)


def markdown_url_tag(url: str, style: str) -> str:
    html = fetch_html(url)
    title = extract_title(html)
    return generate_tag(url, title, style.lower())


@click.command()
@click.option(
    "-s",
    "--style",
    type=click.Choice(list(TAG_STYLES.keys()), case_sensitive=False),
    default=DEFAULT_STYLE,
    help=f'Tag style, default "{DEFAULT_STYLE}".',
)
@click.argument("url")
def mdut(url: str, style: str = DEFAULT_STYLE) -> str:
    """
    Markdown URL tag generator. Supports inline and reference (default) tags.

    Inline: [TODO](http://example.com "Example Domain")

    Reference: [TODO]: http://example.com "Example Domain"
    """
    tag = markdown_url_tag(url, style)
    pyperclip.copy(tag)
    click.echo(f"Copied to clipboard:\n{tag}")
    return tag


if __name__ == "__main__":
    mdut()


def reference(url: str) -> str:
    return markdown_url_tag(url, "reference")


def inline(url: str) -> str:
    return markdown_url_tag(url, "inline")


__all__ = ["reference", "inline"]

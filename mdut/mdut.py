from string import Template
from typing import Optional

from bs4 import BeautifulSoup
import click
import httpx
import pyperclip  # type: ignore


TODO = "TODO"

TAG_STYLES = {
    "reference": Template('[TODO]: $url "$title"'),
    "inline": Template('[TODO]($url "$title")'),
    "slack": Template("[TODO]($url)"),
}

DEFAULT_STYLE = "reference"


def fetch_html(url: str) -> str:
    try:
        text = httpx.get(url).text

        # more and more sites are https-only
        if not text and url.startswith("http://"):
            text = fetch_html(url.replace("http", "https"))

        return text

    # allow being lazy, e.g., just "example.com"
    except httpx.UnsupportedProtocol:
        return fetch_html(f"https://{url}")


def extract_title(html: str) -> str:
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = getattr(getattr(getattr(soup, "head"), "title"), "text") or TODO
    except (AttributeError, TypeError):
        title = TODO
    return title.replace('"', '\\"')


def generate_tag(url: str, title: Optional[str], style: str = DEFAULT_STYLE) -> str:
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
    """Markdown URL tag generator."""
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


def slack(url: str) -> str:
    return markdown_url_tag(url, "slack")


__all__ = ["reference", "inline", "slack"]

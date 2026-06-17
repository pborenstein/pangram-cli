"""Command-line interface for pangram-cli."""

import sys
import click
from dotenv import load_dotenv
from pangram import Pangram
from . import __version__

load_dotenv()


@click.command()
@click.version_option(version=__version__, prog_name="pangram")
@click.argument("text", default="-", required=False)
def main(text: str) -> None:
    """Detect AI-generated text using the Pangram Labs API.

    TEXT can be a string or '-' to read from stdin.
    """
    if text == "-":
        text = sys.stdin.read()

    if not text.strip():
        click.echo("Error: no text provided", err=True)
        sys.exit(1)

    client = Pangram()
    result = client.predict(text)
    click.echo(result)


if __name__ == "__main__":
    main()

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
        click.echo(main.get_help(click.Context(main)))
        sys.exit(0)

    try:
        client = Pangram()
        result = client.predict(text)
    except ValueError:
        click.echo("Error: PANGRAM_API_KEY is not set. Add it to .env or set it in your environment.")
        sys.exit(1)
    click.echo(result["prediction_short"])


if __name__ == "__main__":
    main()

"""Command-line interface for pangram-cli."""

import json
import math
import sys
import click
from dotenv import load_dotenv
from pangram import Pangram
from . import __version__

load_dotenv()


@click.command()
@click.version_option(version=__version__, prog_name="pangram")
@click.option("--json", "output_json", is_flag=True, default=False, help="Output full JSON response.")
@click.argument("text", default="-", required=False)
def main(text: str, output_json: bool) -> None:
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

    if output_json:
        words_total = sum(w.get("word_count", 0) for w in result.get("windows", []))
        result["x-pb-data"] = {
            "words_total": words_total,
            "credit_cost": math.ceil(words_total / 1000),
        }
        click.echo(json.dumps(result, indent=2))
    else:
        click.echo(result["prediction_short"])


if __name__ == "__main__":
    main()

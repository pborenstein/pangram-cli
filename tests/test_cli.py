"""Tests for the pangram CLI."""

from unittest.mock import MagicMock, patch
from click.testing import CliRunner
from pangram_cli.cli import main


def test_empty_input_shows_help() -> None:
    """Empty input prints help and exits cleanly."""
    runner = CliRunner()
    result = runner.invoke(main, input="")
    assert result.exit_code == 0
    assert "Usage:" in result.output


def test_missing_api_key_shows_clean_error() -> None:
    """Missing API key prints a clean message, no traceback."""
    runner = CliRunner()
    with patch("pangram_cli.cli.Pangram") as mock_pangram:
        mock_pangram.side_effect = ValueError("API key is required.")
        result = runner.invoke(main, ["the struggle is real"])
    assert result.exit_code != 0
    assert "PANGRAM_API_KEY" in result.output
    assert "Traceback" not in result.output
    assert "PangramText" not in result.output


def test_json_output() -> None:
    """--json flag prints the full response as JSON."""
    runner = CliRunner()
    mock_response = {"prediction_short": "Human", "fraction_human": 1.0, "windows": []}

    with patch("pangram_cli.cli.Pangram") as mock_pangram:
        mock_pangram.return_value.predict.return_value = mock_response
        result = runner.invoke(main, ["--json", "This is some text."])

    assert result.exit_code == 0
    import json
    parsed = json.loads(result.output)
    assert parsed["prediction_short"] == "Human"


def test_json_output_includes_cost() -> None:
    """--json output includes x-pb-cost field with ceiling credit count."""
    runner = CliRunner()
    mock_response = {
        "prediction_short": "Human",
        "fraction_human": 1.0,
        "windows": [
            {"word_count": 600},
            {"word_count": 450},
        ]
    }

    with patch("pangram_cli.cli.Pangram") as mock_pangram:
        mock_pangram.return_value.predict.return_value = mock_response
        result = runner.invoke(main, ["--json", "Some text."])

    import json
    parsed = json.loads(result.output)
    assert "x-pb-data" in parsed
    assert parsed["x-pb-data"]["words_total"] == 1050
    assert parsed["x-pb-data"]["credit_cost"] == 2  # ceil(1050/1000)


def test_classify_text() -> None:
    """CLI calls predict() with the given text and prints the result."""
    runner = CliRunner()
    with patch("pangram_cli.cli.Pangram") as mock_pangram:
        mock_pangram.return_value.predict.return_value = {"prediction_short": "Human"}
        result = runner.invoke(main, ["This is some text to classify."])

    assert result.exit_code == 0
    assert "Human" in result.output

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


def test_classify_text() -> None:
    """CLI calls predict() with the given text and prints the result."""
    runner = CliRunner()
    with patch("pangram_cli.cli.Pangram") as mock_pangram:
        mock_pangram.return_value.predict.return_value = {"prediction_short": "Human"}
        result = runner.invoke(main, ["This is some text to classify."])

    assert result.exit_code == 0
    assert "Human" in result.output

"""Basic tests for pangram-cli."""

from pangram_cli import __version__


def test_version() -> None:
    assert __version__ is not None
    assert isinstance(__version__, str)

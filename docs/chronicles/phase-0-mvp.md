# Phase 0: MVP

## Entry 1: Project scaffolding (2026-06-17)

**What**: Set up pangram-cli from scratch — package structure, CLI stub, dotenv, tracking docs.

**Why**: MVP goal is a single working command; start minimal and verify end-to-end before adding anything.

**How**:

- `pyproject.toml` with `pangram-sdk`, `click`, `python-dotenv` deps
- `pangram_cli/cli.py` — click command, stdin default, dotenv load
- `.gitignore` includes `.env`
- `docs/` tracking structure initialized

**Decisions**:

- DEC-001: stdin as default via `click.argument(default="-")`
- DEC-002: python-dotenv for API key loading

**Files**: `pyproject.toml`, `pangram_cli/cli.py`, `pangram_cli/__init__.py`, `tests/`, `docs/`

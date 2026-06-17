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

---

## Entry 2: TDD loop to working MVP (2026-06-17)

**What**: Three failing tests written first, then code made to pass. Full end-to-end verified with real API.

**Why**: First real TDD session — write the test, watch it fail, fix the code. Repeated for each behavior.

**How**:

- `test_classify_text`: revealed SDK returns dict not object — fixed `result.classification` → `result["prediction_short"]`
- `test_missing_api_key_shows_clean_error`: replaced traceback with clean message to stdout
- `test_empty_input_shows_help`: replaced `sys.exit(1)` with help text output
- Verified live: `cat wtd-proposal.md | pangram` → `AI` (author's shame)

**Decisions**: None new — DEC-001 and DEC-002 held.

**Files**: `pangram_cli/cli.py`, `tests/test_cli.py` — commit `5df9b30`

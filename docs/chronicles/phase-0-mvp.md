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

---

## Entry 3: --json flag (2026-06-17)

**What**: Added `--json` flag outputting the full Pangram API response as indented JSON.

**Why**: Full response unlocks fraction scores, per-segment windows, confidence levels — pipeable to jq or any downstream tool.

**How**:

- TDD: failing test first, then `--option "output_json"` click flag, then `json.dumps(result, indent=2)`
- Discovered the API includes vault frontmatter in the text — worth stripping in future
- Confirmed live: WTD proposal scores 1.0 fraction_ai, 3 High-confidence AI segments

**Files**: `pangram_cli/cli.py`, `tests/test_cli.py` — commit `bf34e07`

---

## Entry 4: x-pb-data pocket, license, v0.1.0 release (2026-06-17)

**What**: Added `x-pb-data` extension field to `--json` output with `words_total` and `credit_cost`; cut v0.1.0 release to GitHub; added MIT license and README pangram.com links.

**Why**: Cost visibility in JSON output without polluting the API response shape. `x-` prefix signals client-added field. Ceiling division: 1017 words = 2 credits.

**How**:

- TDD: test asserted `x-pb-data.words_total` and `x-pb-data.credit_cost` before implementation
- `math.ceil(words_total / 1000)` for credit count
- `gh repo create` + `gh release create` for v0.1.0
- Noted: frontmatter in vault notes inflates word count — future improvement to strip it

**Decisions**: DEC-003 (x-pb-data namespace)

**Files**: `pangram_cli/cli.py`, `tests/test_cli.py`, `LICENSE`, `README.md`, `CHANGELOG.md`

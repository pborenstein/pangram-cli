# pangram-cli Implementation

CLI tool for detecting AI-generated text using the Pangram Labs API.

## Phase Overview

| Phase | Name | Status |
|-------|------|--------|
| 0 | MVP | Complete |

## Phase 0: MVP

**Goal**: Minimal working CLI — `pangram "text"` or `echo "text" | pangram` returns a classification.

### Tasks

- [x] Project scaffolding (pyproject.toml, package structure, .gitignore)
- [x] `cli.py` with click, stdin support, dotenv loading
- [x] `uv sync` — install deps and verify
- [x] End-to-end test with real API key
- [x] Fix response parsing: SDK returns dict, use `result["prediction_short"]`
- [x] Clean error for missing API key (no traceback)
- [x] Empty input shows help text
- [x] TDD test suite: 3 tests passing
- [x] Initial commits

### Notes

- SDK: `pangram-sdk==0.3.1`
- Auth: `PANGRAM_API_KEY` env var, loaded from `.env` via python-dotenv
- Response is a dict with `prediction_short` (Human/AI/AI-Assisted) and `windows[]` for segments
- Full segment data available for future verbose/JSON output mode

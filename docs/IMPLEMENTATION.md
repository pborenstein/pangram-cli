# pangram-cli Implementation

CLI tool for detecting AI-generated text using the Pangram Labs API.

## Phase Overview

| Phase | Name | Status |
|-------|------|--------|
| 0 | MVP | In Progress |

## Phase 0: MVP

**Goal**: Minimal working CLI — `pangram "text"` or `echo "text" | pangram` returns a classification.

### Tasks

- [x] Project scaffolding (pyproject.toml, package structure, .gitignore)
- [x] `cli.py` with click, stdin support, dotenv loading
- [ ] `uv sync` — install deps and verify
- [ ] End-to-end test with real API key
- [ ] Decide on output format
- [ ] Initial commit

### Notes

- SDK: `pangram-sdk`, installed via pip/uv
- Auth: `PANGRAM_API_KEY` env var, loaded from `.env` via python-dotenv
- The `Pangram()` constructor reads `PANGRAM_API_KEY` automatically if not passed
- MVP intentionally has no bells and whistles — one command, one result

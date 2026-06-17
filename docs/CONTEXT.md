---
phase: 0
phase_name: MVP
updated: 2026-06-17
last_commit: (initial)
---

## Current Focus

Building the MVP CLI: `pangram "text or stdin"` using the Pangram Labs Python SDK.

## Active Tasks

- [ ] Install deps and verify SDK works (`uv sync`)
- [ ] Test `pangram "some text"` end-to-end with a real API key
- [ ] Decide on output format (raw result vs. structured)

## Blockers

Need a Pangram API key in `.env` before end-to-end testing.

## Context

- Entry point: `pangram_cli/cli.py`, registered as `pangram` in pyproject.toml
- `.env` is gitignored; set `PANGRAM_API_KEY=...` there
- `python-dotenv` loads `.env` automatically at startup
- `click.argument("text", default="-")` means bare `pangram` reads stdin

## Next Session

Run `uv sync`, create `.env` with your API key, then `uv run pangram "some text"` to verify end-to-end.

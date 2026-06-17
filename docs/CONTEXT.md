---
phase: 0
phase_name: MVP
updated: 2026-06-17
last_commit: 5df9b30
---

## Current Focus

MVP is complete and working. `pangram "text"` and `cat file | pangram` both work end-to-end.

## Active Tasks

- [x] Install deps and verify SDK works
- [x] Test end-to-end with real API key
- [x] Fix response parsing (dict, not object)
- [x] Clean error for missing API key
- [x] Empty input shows help
- [x] TDD test suite (3 tests passing)

## Blockers

None.

## Context

- SDK returns a dict; use `result["prediction_short"]` for the label (Human/AI/AI-Assisted)
- Full response has segment-level data in `windows[]` — useful for future verbose mode
- `.env` with `PANGRAM_API_KEY` is gitignored; required for real runs
- Tests mock `Pangram` entirely — no API key needed for `uv run pytest`
- Command is `pangram`, not `pangram-cli`

## Next Session

MVP is done. Next: decide what to add — verbose/segment output, `--json` flag, confidence score, or batch mode.

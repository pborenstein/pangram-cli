# pangram-cli Implementation

CLI tool for detecting AI-generated text using the Pangram Labs API.

## Phase Overview

| Phase | Name | Status |
|-------|------|--------|
| 0 | MVP | Complete |
| 1 | Multi-file / Bulk | Planning |

## Phase 0: MVP (Complete)

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
- [x] `--json` flag: full API response as indented JSON
- [x] `x-pb-data` pocket: `words_total`, `credit_cost` (ceil / 1000)
- [x] MIT license + README with pangram.com links
- [x] v0.1.0 released to GitHub
- [ ] v0.2.0 release
- [ ] Strip frontmatter before classify (inflates word count unnecessarily)

### Notes

- SDK: `pangram-sdk==0.3.1`
- Auth: `PANGRAM_API_KEY` env var, loaded from `.env` via python-dotenv
- Response is a dict with `prediction_short` (Human/AI/AI-Assisted/Mixed) and `windows[]` for segments
- `x-pb-data` is our extension namespace — safe to add fields there without conflicting with API

---

## Phase 1: Multi-file / Bulk (Planning)

**Goal**: `pangram file1.md file2.md ...` — submit all files as a bulk job, wait once, print results.

### SDK bulk API notes

- `submit_bulk(text=[...])` — plain list of strings; returns `bulk_id`
- `submit_bulk(items=[{"id": "...", "text": "..."}])` — use filename as `id` so results map back to files
- `wait_for_bulk(bulk_id)` — polls until terminal status: `succeeded`, `failed`, or `partial`
- `get_bulk_results()` — fetches all results into memory; use `get_bulk_results_page()` for large batches
- Terminal status `partial` means some succeeded, some failed — CLI must handle gracefully
- No hard rate limits or item count limits documented; page size max is 1000 items per API call
- `batch_predict()` is deprecated as of August 2026 — it was sequential `predict()` calls, not parallel
- Completion time: "depends on number and length of submitted items and current system load"

### Open questions

- What's the right CLI shape? `pangram file1.md file2.md` or `pangram --bulk file1.md file2.md`?
- Should it also accept a glob? `pangram *.md`
- Output format: one line per file (`filename: Human`) or a table?
- How to handle `partial` — show what succeeded, report failures separately?
- Progress indicator while waiting? (bulk jobs on large batches could take a while)

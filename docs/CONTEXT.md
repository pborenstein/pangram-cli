---
phase: 0
phase_name: MVP
updated: 2026-06-17
last_commit: bf34e07
---

## Current Focus

MVP + --json shipped. Ready to cut v0.1.0 release, then move to Phase 1 (multi-file/bulk).

## Active Tasks

- [x] --json flag: full response output
- [ ] Cut v0.1.0 release

## Blockers

None.

## Context

- `--json` outputs the full dict: prediction_short, fraction_ai/human/ai_assisted, windows[]
- The frontmatter in vault notes is being sent to the API — worth stripping before classify in future
- `batch_predict()` deprecated Aug 2026 — use `submit_bulk()` for multi-file
- Use filename as `id` in bulk items so results map back cleanly

## Next Session

Phase 1: `pangram file1.md file2.md` via bulk API. See IMPLEMENTATION.md for open questions.

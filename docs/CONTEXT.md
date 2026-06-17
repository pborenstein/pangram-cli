---
phase: 0
phase_name: MVP
updated: 2026-06-17
last_commit: 2c3b821
---

## Current Focus

MVP complete with --json and x-pb-data cost tracking. v0.1.0 released to GitHub. Cutting v0.2.0 next.

## Active Tasks

- [x] --json flag
- [x] x-pb-data with words_total and credit_cost
- [x] MIT license
- [x] README links to pangram.com
- [x] v0.1.0 released
- [ ] Cut v0.2.0 release

## Blockers

None.

## Context

- `x-pb-data` is our extension pocket — `words_total` and `credit_cost` (ceiling div by 1000) live there
- Frontmatter in vault notes inflates word count — stripping it before classify is a future improvement
- 1017 words = 2 credits (17 words over the 1000 boundary — painful but correct)
- `batch_predict()` deprecated Aug 2026 — Phase 1 uses `submit_bulk()` with filename as item `id`
- GitHub repo: https://github.com/pborenstein/pangram-cli

## Next Session

Cut v0.2.0, then Phase 1: multi-file bulk support. See IMPLEMENTATION.md for open questions.

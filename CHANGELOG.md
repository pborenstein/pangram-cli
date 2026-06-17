# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-06-17

### Added

- `x-pb-data` field in `--json` output with `words_total` and `credit_cost` (ceiling division by 1000 per Pangram pricing) ([5840126](https://github.com/pborenstein/pangram-cli/commit/5840126))
- MIT license ([2c3b821](https://github.com/pborenstein/pangram-cli/commit/2c3b821))
- README links to pangram.com ([2c3b821](https://github.com/pborenstein/pangram-cli/commit/2c3b821))

## [0.1.0] - 2026-06-17

### Added

- `pangram "text"` and `echo "text" | pangram` — classify text as Human, AI, or AI-Assisted ([bf34e07](https://github.com/pborenstein/pangram-cli/commit/bf34e07))
- `--json` flag outputs full Pangram API response including per-segment scores and confidence ([bf34e07](https://github.com/pborenstein/pangram-cli/commit/bf34e07))
- Clean error message when `PANGRAM_API_KEY` is missing (no traceback) ([5df9b30](https://github.com/pborenstein/pangram-cli/commit/5df9b30))
- Help text shown on empty input ([5df9b30](https://github.com/pborenstein/pangram-cli/commit/5df9b30))
- stdin support — pipe text directly ([5df9b30](https://github.com/pborenstein/pangram-cli/commit/5df9b30))
- `.env` file support via python-dotenv ([e6b37c9](https://github.com/pborenstein/pangram-cli/commit/e6b37c9))

[0.2.0]: https://github.com/pborenstein/pangram-cli/releases/tag/v0.2.0
[0.1.0]: https://github.com/pborenstein/pangram-cli/releases/tag/v0.1.0
[Unreleased]: https://github.com/pborenstein/pangram-cli/compare/v0.2.0...HEAD

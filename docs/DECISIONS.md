# Decisions

Architectural decisions for pangram-cli. Search with `grep -i "keyword" docs/DECISIONS.md`.

## Active Decisions

### DEC-001: stdin as default input (2026-06-17)

**Status**: Active

**Context**: CLI should support both `pangram "text"` and piped input.

**Decision**: Use `click.argument("text", default="-")` — `-` means read from stdin, matching Unix conventions.

**Alternatives considered**: Separate `--text` flag; require explicit `-` for stdin.

**Consequences**: `pangram` with no args reads stdin; `pangram "text"` passes inline. Natural and composable.

---

### DEC-002: python-dotenv for API key (2026-06-17)

**Status**: Active

**Context**: API key must not be committed; needs to be available at runtime.

**Decision**: Load `.env` via `python-dotenv` at startup; `.env` is gitignored.

**Alternatives considered**: Require env var to be set externally (no dotenv); use a config file.

**Consequences**: Simple local dev (`echo "PANGRAM_API_KEY=..." > .env`); production deploys set the env var directly.

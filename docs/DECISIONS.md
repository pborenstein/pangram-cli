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

---

### DEC-003: x-pb-data as extension namespace in JSON output (2026-06-17)

**Status**: Active

**Context**: Wanted to add client-computed fields (word count, credit cost) to `--json` output without mixing them into the API response fields.

**Decision**: Add a single `x-pb-data` dict to the response. `x-` prefix signals "not from the API." All client-added fields go inside this dict.

**Alternatives considered**: Top-level fields (`words_total`, `credit_cost` directly); separate `--stats` flag; stderr output.

**Consequences**: Clean separation between API data and client metadata. Easy to extend without risk of future API field name collisions.

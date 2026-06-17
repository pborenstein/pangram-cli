# pangram-cli

CLI tool for detecting AI-generated text using the [Pangram Labs](https://pangram.com) API.

## Quick Start

```bash
# Install dependencies
uv sync

# Set your API key (get one at https://pangram.com)
echo "PANGRAM_API_KEY=your-key-here" > .env

# Run
pangram "some text to check"
echo "some text" | pangram
cat document.md | pangram --json
```

## Usage

```
pangram [OPTIONS] [TEXT]
```

`TEXT` is optional — omit it or pass `-` to read from stdin.

### Options

| Flag | Description |
|------|-------------|
| `--json` | Output full JSON response (scores, segments, confidence) |
| `--version` | Show version and exit |
| `--help` | Show help and exit |

### Output

Default: one word — `Human`, `AI`, or `AI-Assisted`.

With `--json`: full Pangram response including `fraction_ai`, `fraction_human`, and per-segment `windows[]` with confidence scores.

## API Key

Get an API key at [pangram.com](https://pangram.com). Set it in `.env`:

```
PANGRAM_API_KEY=your-key-here
```

Or export it directly:

```bash
export PANGRAM_API_KEY=your-key-here
```

## Development

```bash
uv sync
uv run pangram --version
uv run pytest
```

## License

MIT — see [LICENSE](./LICENSE).

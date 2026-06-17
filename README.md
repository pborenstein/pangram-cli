# pangram-cli

CLI tool for detecting AI-generated text using the Pangram Labs API.

## Quick Start

```bash
# Install dependencies
uv sync

# Set your API key
echo "PANGRAM_API_KEY=your-key-here" > .env

# Run
pangram "some text to check"
echo "some text" | pangram
```

## Usage

```
pangram [TEXT]
```

`TEXT` is optional — omit it or pass `-` to read from stdin.

## Development

```bash
uv sync
uv run pangram --version
uv run pytest
```

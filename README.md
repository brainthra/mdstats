# mdstats

A simple command line tool to get statistics of markdown files.

## Usage

```bash
mdstats <file_path> 
```

## Development

Sync the project environment with the following command:

```bash
uv sync
```

Run the application:

```bash
uv run mdstats <file_path>
```

### Testing

Run the tests with:

```bash
uv run pytest
```

### Linting

Run the linter with:

```bash
uv run ruff check .
```

### Type Checking

Run the type checker with:

```bash
uv run pyright
```
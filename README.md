# mdstats

A simple command line tool to get statistics of markdown files.

## Usage

```bash
mdstats <file_path> 
```

## Installation

### From PyPI

```bash
uv tool install mdstats
```

Alternatively:
```bash
pipx install mdstats
```

### From source

Clone the repository and create the development environment:

```bash
git clone https://github.com/brainthra/mdstats.git
cd mdstats
uv sync
```

## Development

Clone from the repository and create the development environment.

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
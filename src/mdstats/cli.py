"""Command-line interface for mdstats."""

import argparse
from pathlib import Path

from mdstats.stats import calculate_stats


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="mdstats",
        description="Display statistics for a Markdown file.",
    )

    parser.add_argument(
        "file",
        type=Path,
        help="Markdown file to analyse",
    )

    return parser


def main() -> None:
    """Run the mdstats command-line application."""
    parser = create_parser()
    args = parser.parse_args()

    path: Path = args.file

    if not path.exists():
        parser.error(f"file does not exist: {path}")

    if not path.is_file():
        parser.error(f"path is not a file: {path}")

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.error(f"could not read file: {error}")

    stats = calculate_stats(text)

    print(f"File: {path}")
    print()
    print(f"Lines: {stats.lines}")
    print(f"Words: {stats.words}")
    print(f"Characters: {stats.characters}")
    print(f"Headings: {stats.headings}")
    print(f"Links: {stats.links}")
    print(f"Code blocks: {stats.code_blocks}")

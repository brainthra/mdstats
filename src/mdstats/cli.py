import argparse
from pathlib import Path

from mdstats.stats import calculate_stats


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Display basic statistics for a text file."
    )
    parser.add_argument("file", type=Path)

    args = parser.parse_args()

    text = args.file.read_text()

    stats = calculate_stats(text)

    print(f"Lines: {stats.lines}")
    print(f"Words: {stats.words}")
    print(f"Characters: {stats.characters}")
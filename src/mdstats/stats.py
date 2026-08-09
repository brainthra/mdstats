from dataclasses import dataclass


@dataclass(frozen=True)
class TextStats:
    lines: int
    words: int
    characters: int


def calculate_stats(text: str) -> TextStats:
    return TextStats(
        lines=len(text.splitlines()),
        words=len(text.split()),
        characters=len(text),
    )
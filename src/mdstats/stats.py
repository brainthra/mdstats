import re
from dataclasses import dataclass


@dataclass(frozen=True)
class TextStats:
    lines: int
    words: int
    characters: int
    headings: int
    links: int
    code_blocks: int


def calculate_stats(text: str) -> TextStats:
    return TextStats(
        lines=len(text.splitlines()),
        words=len(text.split()),
        characters=len(text),
        headings=count_headings(text),
        links=count_links(text),
        code_blocks=count_code_blocks(text),
    )


def count_headings(text: str) -> int:
    return sum(1 for line in text.splitlines() if re.match(r"^#{1,6}\s+", line))


def count_links(text: str) -> int:
    return len(re.findall(r"\[[^\]]+\]\([^)]+\)", text))


def count_code_blocks(text: str) -> int:
    fences = sum(1 for line in text.splitlines() if line.strip().startswith("```"))

    return fences // 2

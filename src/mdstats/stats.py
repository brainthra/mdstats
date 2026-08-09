"""Calculate textual and Markdown-specific document statistics."""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class TextStats:
    """Summary statistics calculated from a text document."""

    lines: int
    words: int
    characters: int
    headings: int
    links: int
    code_blocks: int


def calculate_stats(text: str) -> TextStats:
    """Calculate all supported statistics for *text*."""
    return TextStats(
        lines=len(text.splitlines()),
        words=len(text.split()),
        characters=len(text),
        headings=count_headings(text),
        links=count_links(text),
        code_blocks=count_code_blocks(text),
    )


def count_headings(text: str) -> int:
    """Count Markdown headings in *text*."""
    return sum(1 for line in text.splitlines() if re.match(r"^#{1,6}\s+", line))


def count_links(text: str) -> int:
    """Count conventional inline Markdown links in *text*."""
    return len(re.findall(r"\[[^\]]+\]\([^)]+\)", text))


def count_code_blocks(text: str) -> int:
    """Count fenced Markdown code blocks in *text*.

    The implementation counts lines beginning with a triple-backtick fence and
    assumes each block contains an opening and closing fence.
    """
    fences = sum(1 for line in text.splitlines() if line.strip().startswith("```"))

    return fences // 2

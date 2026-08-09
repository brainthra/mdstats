from mdstats.stats import (
    calculate_stats,
    count_code_blocks,
    count_headings,
    count_links,
)


def test_calculate_stats() -> None:
    text = "# Hello\n\nThis is some text.\n"

    stats = calculate_stats(text)

    assert stats.lines == 3
    assert stats.words == 6
    assert stats.characters == len(text)
    assert stats.headings == 1


def test_count_headings() -> None:
    text = """# Heading 1
## Heading 2
Not a heading
### Heading 3
"""

    assert count_headings(text) == 3


def test_count_links() -> None:
    text = """
Visit [Python](https://python.org).

Also visit [GitHub](https://github.com).
"""

    assert count_links(text) == 2


def test_count_code_blocks() -> None:
    text = """Before

```python
print("hello")
```

After
"""
    assert count_code_blocks(text) == 1

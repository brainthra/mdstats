import sys
from pathlib import Path

import pytest

from mdstats.cli import main


def test_cli_outputs_statistics(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    file = tmp_path / "example.md"
    file.write_text("# Hello\n\nSome text.\n", encoding="utf-8")

    monkeypatch.setattr(sys, "argv", ["mdstats", str(file)])

    main()

    output = capsys.readouterr().out

    assert "File:" in output
    assert "Headings: 1" in output


def test_cli_rejects_missing_file(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    file = tmp_path / "missing.md"

    monkeypatch.setattr(sys, "argv", ["mdstats", str(file)])

    with pytest.raises(SystemExit) as error:
        main()

    assert error.value.code == 2

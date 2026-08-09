# Changelog

All notable changes to this project will be documented in this file.

The project follows Semantic Versioning.

## [Unreleased]

## [1.0.0] - 2026-08-09

## Added

- GitHub Actions continuous integration.
- CI testing across supported Python versions.
- CI checks for formatting, linting, typing, tests, and package builds.
- Automated PyPI publication workflow.

## [0.3.0] - 2026-08-09

### Added

- Automated tests with pytest.
- Linting and formatting with Ruff.
- Static type checking with Pyright.
- Development dependency group added.
- Tests for core statistics and CLI behaviour.

## [0.2.0] - 2026-08-09

### Added

- Heading count.
- Markdown link count.
- Fenced code-block count.
- File path in command output.

### Changed

- Improved CLI help and argument handling.
- Added validation for missing and invalid file paths.
- Added user-friendly errors for unreadable files.

## [0.1.0] - 2026-08-09

### Added

- Initial `mdstats` command-line application.
- Basic line, word, and character statistics.
- Initialise project with `uv`.
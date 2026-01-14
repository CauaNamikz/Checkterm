# Checkterm
Checkterm is a powerful and simple-to-use checklist CLI using Python that can evolve into a GUI eventually.

# Current Version
`0.0.1.2026`

# Functions
- Adding, removing and completing entries (filtering them by ID, name, completed [active = 0, state 1] or not [active = 1, state = 0])
- Basic saving/loading system

## Roadmap
- First internal refactor
- More languages
- Entry descriptions
- Multiple checklists and checklist descriptions
- User and group support
- Pomodoro method integration
- Second internal refactor (new branch)
- New installation methods:
  - git clone
  - pip install .
  - PyInstaller standalone build
- Possible rewrite in a more performant / smoother programming language (new branch)
- Eventual GUI rewrite, redesign and purpose rework (separate repository)

Note: even if Checkterm receives an official GUI version, the CLI will continue to be maintained as a stable base for other checklist-related projects for anyone.

# Version structure
Checkterm uses a custom versioning format. Example:
`1.2.9.2027`

Meaning:
- `1` → major version identifier (large or breaking changes)
- `2` → minor version identifier (new features, non-breaking)
- `9` → patch version identifier (small fixes and improvements)
- `2027` → year identifier

Notes:
- The major and minor version numbers may grow beyond 9.
- The patch version number is limited to single digits (0–9).
  - Valid example: `18.15.7.2028`
  - Invalid example: `18.15.17.2028`

## Alpha versions
If both the major and minor version numbers are **0**, the release is considered an **ALPHA version**.
In alpha versions:
- The **minor version identifier** acts as the major progression indicator.
- The **patch version identifier** acts as the minor progression indicator.

This phase allows rapid iteration without long-term stability guarantees.

## Beta versions
If the major version number is **0** and the minor version number is **greater than or equal to 5**, the release is considered a **BETA version**.
In beta versions:
- The **minor version identifier** represents major feature milestones.
- The **patch version identifier** represents smaller improvements and fixes.

## LTS version
If the major version number is **greater than or equal to 1**, the release is considered **LTS**.
In LTS versions:
- LTS versions follow the standard version structure and aim to maintain backwards compatibility whenever possible.

# Installation

Requirements:
- Python 3.x

## For alpha versions
1. Download the ZIP from github.com/Checkterm/Releases
2. Extract it in any folder
3. Open the root folder of the project in the terminal/command prompt (you can see the folders checkterm and data inside of them)
4. Type "python3 -m checkterm"

Done! You've initiated Checkterm.

# Usage

Once running, type `help` to see all available commands, their usage and outputs.

Main commands:
- `add-entry` (Add an entry)
- `complete-entry` (Complete an entry)
- `remove-entry` (Remove an entry)
- `list-active` (See list of active entries)
- `list-state-0` (See list of incomplete entries)
- `list-state-1` (See list of complete entries)
- `save` (Save checklist to data folder)
- `load` (Load checklist from data folder)
- `quit` (Quit program)

Outputs:
- `0` (Success)
- `1` (Error [Invalid])

# Project Structure

```text
checkterm/
├── checkterm/
│   ├── cli.py
│   ├── commands.py
│   ├── state.py
│   └── storage.py
├── data/
└── README.md
```
# Contributing

Contributions are welcome.

Please open an issue to discuss changes before submitting a pull request.
Follow the existing code/version structure (unless refactor is needed) and naming conventions.

# Author

Created and maintained by cauanamikz in 14/01/2026.

# License

Checkterm is licensed under the Apache License 2.0.

Any use, modification, or distribution must retain credit
to the original project and author, and specify changes.

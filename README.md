# Checkterm
Checkterm is a powerful, lightweight and simple-to-use checklist CLI using Python that can evolve into a GUI eventually.

# Current Version
`0.0.2.2026`

# Functions
- Adding, removing and completing entries
- Basic saving/loading system

## Roadmap
- First internal refactor **(DONE)**
- More languages
- Entry descriptions and better entry management **(DONE)**
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

Note: even if Checkterm receives an official GUI version, the CLI will continue to be maintained as a stable base for other checklist-related projects for anyone, and will become a template project.

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
1. Download the .tar.gz file from github.com/Checkterm/Releases or the .zip file in the button "Code" from github.com/CauaNamikz/Checkterm 
2. Extract it in any folder
3. Open the root folder of the project in the terminal/command prompt (you can see the folders checkterm and data inside of them)
4. Type "python3 -m checkterm"

Done! You've initiated Checkterm.

# Usage

Once running, type `help` to see all available commands, their usage and outputs.

Main commands:
- `add-entry` (Add one entry and its optional description)
- `add-description` (Add/edit description of one existing entry)
- `check-entry`(See info of one entry)
- `edit-entry-name` (Edit one entry's name)
- `complete-entry` (Complete one entry)
- `uncomplete-entry` (Uncomplete one entry)
- `remove-entry` (Remove one entry)
- `list` (List all entries)
- `list-incomplete` (List incomplete entries)
- `list-complete` (List complete entries)
- `save` (Save checklist)
- `load` (Load checklist)
- `quit` (Quit the program)

Outputs:
- `0` (Success)
- `1` (Error [invalid])

# Project Structure

```text
checkterm/
├── checkterm/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── commands.py
│   ├── help.py
│   ├── output.py
│   ├── state.py
│   └── storage.py
├── data/
│   ├── entries.json
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

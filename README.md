# pythonPCEPtrainer

PCEP Python Exam Tutor — an interactive study tool for PCEP (Python Certified Entry-Level Programmer) with both terminal and GUI versions.

## Features

- 15 comprehensive lessons covering all PCEP exam topics
- Interactive quizzes with instant feedback
- Hands-on coding exercises
- 20-question practice exams
- Progress tracking and statistics
- Both terminal (CLI) and graphical (GUI) interfaces

## Quick Start

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Run the tutor:

**Terminal Version:**
```bash
python3 python_tutor.py
```

**GUI Version:**
```bash
python3 python_tutor_gui.py
```

## Usage

### Terminal Version
- Navigate with keyboard commands
- Complete lessons, exercises, and quizzes
- Take practice exams
- View study tips

### GUI Version
- Double-click lessons to open them
- Use tabs to navigate content, examples, exercises, and quizzes
- Click buttons to run code and check answers
- Access practice exams and study tips from the menu

## Development

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest
```

Run linters:

```bash
ruff check .
black --check .
```

## Notes

- Progress is saved to `pcep_tutor_progress.json`
- Both versions share the same progress file
- GitHub Actions CI runs linters and tests on every push

## License

MIT — see [LICENSE](LICENSE)
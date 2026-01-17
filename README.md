# pythonPCEPtrainer

🎓 PCEP Python Exam Tutor — a comprehensive interactive study tool for the Python Certified Entry-Level Programmer (PCEP) certification exam.

## Features

### 📚 Comprehensive Learning Content
- **15 detailed lessons** covering all PCEP exam topics:
  - Python fundamentals and compilation
  - Data types, variables, and operators
  - Strings and I/O operations
  - Boolean logic and conditionals
  - Loops (for, while) and control flow
  - Lists and list operations
  - Functions and scope
  - Tuples and dictionaries
  - Modules and packages
  - Exception handling
  - Bitwise and logical operations

### 🎯 Interactive Learning Tools
- **Quizzes**: Multiple-choice quizzes with instant feedback and explanations
- **Exercises**: Hands-on coding exercises with validation
- **Practice Exams**: Full 20-question practice exams simulating the real PCEP test
- **Code Examples**: Runnable code examples for every lesson
- **Study Tips**: Comprehensive exam preparation guidance

### 💾 Progress Tracking
- Automatic progress saving
- Quiz score tracking and averages
- Lesson completion status
- Shared progress between terminal and GUI versions

### 🖥️ Dual Interface Options
- **Terminal Version**: Classic command-line interface for focused learning
- **GUI Version**: Modern graphical interface with:
  - Tabbed lesson viewer
  - Syntax-highlighted code display
  - Interactive quiz interface
  - One-click code execution
  - Menu-driven navigation
  - Clean, organized layout

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone git@github.com:jeuanimo/pythonPCEPtrainer.git
cd pythonPCEPtrainer
```

2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. (Optional) Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

### Running the Application

**GUI Version (Recommended):**
```bash
python3 python_tutor_gui.py
```

**Terminal Version:**
```bash
python3 python_tutor.py
```

## Usage Guide

### GUI Version Features

#### Main Menu
- Browse all 15 lessons organized by PCEP sections
- View progress indicators (✓ for completed lessons)
- See quiz scores at a glance
- Double-click any lesson to open it

#### Lesson Viewer
- **Content Tab**: Read lesson material covering key concepts
- **Example Tab**: View and run code examples with output display
- **Exercise Tab**: Write and test your own code with validation
- **Quiz Tab**: Take interactive quizzes with immediate feedback

#### Menus
- **File Menu**: 
  - Reset Progress: Clear all saved progress
  - Exit: Close the application
- **Exam Menu**:
  - Practice Exam: Take a full 20-question PCEP practice test
  - Study Tips: View exam strategies and key topics to memorize

#### Navigation
- Previous/Next buttons to move between lessons
- Back to Menu button to return to lesson list
- Keyboard-friendly interface

### Terminal Version Features
- Command-line navigation (type lesson numbers, 'n' for next, 'p' for previous)
- Interactive mode for each lesson
- Full quiz and practice exam support
- Progress tracking shared with GUI version

## PCEP Exam Information

The PCEP (Python Certified Entry-Level Programmer) certification is the entry-level credential for Python programming:

- **Questions**: 30 multiple-choice
- **Duration**: 40 minutes
- **Passing Score**: 70%
- **Format**: Online proctored exam
- **Topics**: 
  - Basic Concepts (18%)
  - Data Types & Operators (29%)
  - Control Flow & Collections (25%)
  - Functions & Modules (28%)

## Development

### Running Tests

Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

Run the test suite:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=. --cov-report=html
```

### Code Quality

Run linters:
```bash
ruff check .
black --check .
```

Auto-format code:
```bash
black .
ruff format .
isort .
```

### Project Structure

```
pythonPCEPtrainer/
├── python_tutor.py          # Terminal version
├── python_tutor_gui.py      # GUI version (tkinter)
├── tests/
│   ├── test_basic.py        # Basic compilation tests
│   └── test_tutor.py        # Comprehensive unit tests
├── .github/
│   ├── workflows/
│   │   └── python-app.yml   # CI/CD pipeline
│   └── dependabot.yml       # Dependency updates
├── requirements.txt         # Runtime dependencies (none)
├── requirements-dev.txt     # Dev dependencies (pytest, ruff, black)
├── pyproject.toml          # Project configuration
├── pytest.ini              # Pytest configuration
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
└── README.md              # This file
```

### Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Run linters and tests
5. Submit a pull request

## Technical Details

- **Python Version**: 3.6+
- **GUI Framework**: tkinter (included with Python)
- **Testing**: pytest
- **Linting**: ruff, black
- **CI/CD**: GitHub Actions
- **Dependencies**: Standard library only (no runtime dependencies)

## Notes

- Progress is automatically saved to `pcep_tutor_progress.json`
- Both GUI and terminal versions share the same progress file
- All lessons, quizzes, and exams are included in the application
- No internet connection required after download
- GitHub Actions CI runs on every push and PR

## License

MIT — see [LICENSE](LICENSE)
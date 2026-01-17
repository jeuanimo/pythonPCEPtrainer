# pythonPCEPtrainer

PCEP Python Exam Tutor — an interactive terminal-based study tool for PCEP (Python Certified Entry-Level Programmer).

Quick start

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Run the tutor:

```bash
python3 python_tutor.py
```

Notes

- Progress is saved to `pcep_tutor_progress.json`. Add this file to `.gitignore` if you don't want to track it.
- This repository contains a basic GitHub Actions workflow that performs a syntax check with `python -m py_compile`.

License

MIT — see LICENSE (not included).
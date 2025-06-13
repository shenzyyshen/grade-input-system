# Grade Input System

A CLI tool for teachers to input and analyze student grades across multiple subjects.

## Features

- Input grades for multiple students in sequence
- Calculates per-subject and overall class averages
- Converts averages to GPA (4.0 scale)
- Identifies and lists failing students per subject

## Usage

```bash
python main.py
```

## Key Learnings

- Reusable input validation with `while True` + `try/except ValueError`
- Separating data collection from analysis functions
- GPA conversion with conditional ranges
- Iterating a list of dicts to compute running totals

## Project Structure

```
grade-input-system/
├── main.py            # All functions and entry point
└── sample_output.txt  # Example run with two students
```
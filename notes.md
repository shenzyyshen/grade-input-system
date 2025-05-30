# Dev Notes

## Design
- `get_grade(subject)` is reusable — called once per subject with the subject name
- `get_student_info()` returns a dict with Name, English, Math keys
- `calculate_average_grades()` and `calculate_failing_grades()` are separate for single responsibility

# Dev Notes

## Design
- `get_grade(subject)` is reusable — called once per subject with the subject name
- `get_student_info()` returns a dict with Name, English, Math keys
- `calculate_average_grades()` and `calculate_failing_grades()` are separate for single responsibility

## GPA Scale
- 90–100 → 4.0
- 80–89  → 3.0
- 70–79  → 2.0
- 60–69  → 1.0
- Below 60 → 0.0 (failing)

## display_all_students()
- Loops through the students list and prints each entry
- Uses `_` * 30 as a visual separator between students
- Could be extended to support more subjects by iterating dict keys

## Failing Grade Logic
- Grade < 60 is considered failing
- `failing_records` accumulates strings like "Name is failing in Subject with grade X"
- Both the count and the full list are returned for flexible use in `main()`

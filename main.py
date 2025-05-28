def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the student's {subject} grade: ")
            return grade
        except ValueError:
            print("please enter a valid number for the grade.")


def get_student_info()

    name = input("Enter the student#s name: ")
    english_grade = get_grade("English")
    math_grade = get_grade("Math")

    return {
        'name': name,
        'English': english_grade,
        'Math' = math_grade
    }

    student = get_student_info()
    print(student
    Information: "")
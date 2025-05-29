def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter the student's {subject} grade: "))
            return grade
        except ValueError:
            print("please enter a valid number for the grade.")


def get_student_info():
    name = input("Enter the student's name: ")
    english_grade = get_grade("English")
    math_grade = get_grade("Math")

    return {
        'Name': name,
        'English': english_grade,
        'Math' : math_grade
    }

def display_all_students(student_list):

    print("\n=== All Student's Info ===")

    for student in student_list:
        print(f"Name: {student['Name']}")
        print(f" English Grade: {student['English']}")
        print(f" Math Grade: {student['Math']}")
        print("_" * 30)



def calculate_average_grades(students):
    total_english = 0
    total_math = 0
    total_grades = 0

    num_student = len(students)
    num_subjects = 2

    for student in students:
        total_english += student['English']
        total_math += student['Math']
        total_grades += student['English'] + student['Math']

    average_english = total_english / num_student
    average_math = total_math / num_student
    overall_average = (average_english + average_math)/2

    return average_english, average_math, overall_average

def convert_to_gpa(percentage):
    if percentage >= 90:
        return 4.0
    elif percentage >= 80:
        return 3.0
    elif percentage >= 70:
        return 2.0
    elif percentage >= 60:
        return 1.0
    else:
        return 0.0



def main():
    students = []

    while True:
        student = get_student_info()
        students.append(student)

        more = input("do you want to enter another student? (y/n) : ").lower()
        if more != 'y':
            break

    display_all_students(students)

    average_english, average_math, overall_average = calculate_average_grades(students)


    print("\n=== Average Grades per Subject===")
    print(f"Average English Grade: {average_english:.2f} ({convert_to_gpa(average_english): .2f} GPA)")
    print(f"Average Math Grade: {average_math:.2f} ({convert_to_gpa(average_math):.2f} GPA)")
    print(f"Overall Average Grade across all subjects: {overall_average:.2f}({convert_to_gpa(overall_average):.2f} GPA)")



if __name__=="__main__":
    main()



   # average_grades_per_subject, overall_average_grade = calculate_average_grades(students)
    #print("\nAverage grades per subject:")
    #for subject, average_grade in average_grades_per_subject.items():
     #   print(f"{subject}: {average_grade:.2f}")

    #print(f"\nOverall average grade across all subjects: {overall_average_grade:.2f}")



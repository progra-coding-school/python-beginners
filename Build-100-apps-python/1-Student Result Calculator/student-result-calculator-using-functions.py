
# Student Result Calculator using Functions

def get_student_details():
    name = input("Enter student name: ")
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    english = int(input("Enter English marks: "))

    return name, maths, science, english


def calculate_total(maths, science, english):
    total = maths + science + english
    return total


def calculate_percentage(total):
    percentage = (total / 300) * 100
    return percentage


def calculate_grade(maths, science, english, percentage):

    if maths < 35 or science < 35 or english < 35:
        return "F", "Fail"

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    return grade, "Pass"


def display_report(name, total, percentage, grade, result):
    print("\n--- STUDENT RESULT REPORT ---")
    print("Student:", name)
    print("Total:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)


def main():
    name, maths, science, english = get_student_details()

    total = calculate_total(maths, science, english)

    percentage = calculate_percentage(total)

    grade, result = calculate_grade(
        maths, science, english, percentage
    )

    display_report(name, total, percentage, grade, result)


# Start the application
main()

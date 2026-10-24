
# Student Result Calculator

student_name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Calculate total and percentage
total = maths + science + english
percentage = (total / 300) * 100

# Check pass/fail and grade
if maths < 35 or science < 35 or english < 35:
    grade = "F"
    result = "Fail"

else:
    result = "Pass"

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

# Display the report
print("\n--- STUDENT RESULT REPORT ---")
print("Student:", student_name)
print("Total:", total, "/ 300")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)

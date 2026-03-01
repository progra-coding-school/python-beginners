# Student Report Card Builder
# A real-world use of dictionaries: one dict stores all subject marks.
# KEY IDEA: subject name is the KEY, mark is the VALUE.
# This lets you look up any subject's mark by name, loop through all at once,
# and use built-in functions (sum, max, min) directly on the values.

# Step 1: Store the report card — subject → mark
report = {
    "Maths":   88,
    "Science": 92,
    "English": 74,
    "History": 80,
    "Tamil":   95,
}

student_name = "Aarav"

print(student_name + "'s Report Card")
print()

# Step 2: Display all subjects using .items() — key and value together
print("Subject-wise Marks:")
for subject, marks in report.items():
    print("  " + subject.ljust(10) + " : " + str(marks))

print()

# Step 3: Total and average
# sum(dict.values()) adds all marks in one line
# len(dict) counts how many subjects — no need to hardcode 5
total   = sum(report.values())
average = total / len(report)
print("Total   :", total)
print("Average :", str(round(average, 1)))

print()

# Step 4: Best and worst subject
# max(dict, key=dict.get) → finds the KEY whose VALUE is the highest
# This is the standard pattern for finding the key of the max/min value in a dict
best_subject  = max(report, key=report.get)
worst_subject = min(report, key=report.get)

print("Best subject  :", best_subject, "(" + str(report[best_subject]) + ")")
print("Needs work on :", worst_subject, "(" + str(report[worst_subject]) + ")")

print()

# Step 5: Grade for each subject using a helper function
# The function converts a number to a grade letter — called once per subject
def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

print("Grades:")
for subject, marks in report.items():
    grade = get_grade(marks)
    print("  " + subject.ljust(10) + " : " + grade)

# Program Code: CF-PS-03
# Title: Multi-Subject Grade Report
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Control Flow in Python

# Big question: Generate a grade report for 5 subjects.
# Break it into: collect marks → grade each → find overall → display.

print("=== Grade Report Generator ===\n")

# Step 1: Collect marks
subjects = ["Tamil", "English", "Maths", "Science", "Social"]
marks = []
for subject in subjects:
    mark = int(input(f"Enter marks for {subject} (out of 100): "))
    marks.append(mark)

# Step 2: Grade each subject
print("\n--- Subject-wise Results ---")
failed_subjects = []
for i in range(len(subjects)):
    m = marks[i]
    if m >= 90:
        grade = "A+"
    elif m >= 80:
        grade = "A"
    elif m >= 70:
        grade = "B"
    elif m >= 60:
        grade = "C"
    elif m >= 35:
        grade = "D"
    else:
        grade = "F"
        failed_subjects.append(subjects[i])
    print(f"  {subjects[i]}: {m} — Grade {grade}")

# Step 3: Overall result
total = sum(marks)
average = total / len(subjects)
is_passed = len(failed_subjects) == 0

# Step 4: Display summary
print("\n--- Summary ---")
print(f"Total: {total}/500  |  Average: {average:.1f}")
if is_passed:
    print("Overall Result: PASS")
else:
    print("Overall Result: FAIL")
    print("Failed in:", ", ".join(failed_subjects))

# Think:
# 1. What happens if you change 'for i in range(len(subjects))' to 'for subject in subjects'?
# 2. How would you find the highest and lowest marks using a loop?

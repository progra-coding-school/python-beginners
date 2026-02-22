# Program Code: OP-PS-03
# Title: Exam Eligibility Checker
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Operators in Python

# Big question: Is a student eligible to sit for the final exam?
# Break it into conditions — check one at a time.

print("=== Exam Eligibility Checker ===")
print()

# Step 1: Get student details
student_name = input("Student name: ")
maths = int(input("Maths marks (out of 100): "))
science = int(input("Science marks (out of 100): "))
english = int(input("English marks (out of 100): "))
attendance = int(input("Attendance percentage: "))
fee_paid = input("Has fee been paid? (yes/no): ").lower()

# Step 2: Calculate total and average (arithmetic)
total = maths + science + english
average = total / 3

# Step 3: Individual subject pass check (comparison + logical)
maths_passed = maths >= 35
science_passed = science >= 35
english_passed = english >= 35
all_subjects_passed = maths_passed and science_passed and english_passed

# Step 4: Attendance check (comparison)
attendance_ok = attendance >= 75

# Step 5: Fee check (comparison)
fee_cleared = fee_paid == "yes"

# Step 6: Final eligibility (logical — all conditions must be true)
is_eligible = all_subjects_passed and attendance_ok and fee_cleared

# Step 7: Calculate how many marks needed to reach distinction (arithmetic)
distinction_total = 240  # 80% of 300
marks_needed = distinction_total - total
if marks_needed < 0:
    marks_needed = 0

# Step 8: Display result
print(f"\n--- Eligibility Report: {student_name} ---")
print(f"Maths: {maths}  Science: {science}  English: {english}")
print(f"Total: {total}/300  Average: {round(average, 1)}")
print(f"All subjects passed (>=35): {all_subjects_passed}")
print(f"Attendance (>=75%): {attendance_ok}")
print(f"Fee paid: {fee_cleared}")
print()

if is_eligible:
    print("STATUS: ELIGIBLE to write the exam")
    if total >= 240:
        print("On track for DISTINCTION!")
    else:
        print(f"Need {marks_needed} more marks for distinction.")
else:
    print("STATUS: NOT ELIGIBLE")
    if not all_subjects_passed:
        print("Reason: Did not pass all subjects.")
    if not attendance_ok:
        print("Reason: Attendance below 75%.")
    if not fee_cleared:
        print("Reason: Fee not paid.")

# Think:
# 1. What extra condition would you add for a 'sports quota' exemption?
# 2. How would you check if a student improved compared to last semester?

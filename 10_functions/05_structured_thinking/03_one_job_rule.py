# Program Code: FN-ST-03
# Title: The One Job Rule
# Cognitive Skill: Structured Thinking (Data Organisation)
# Topic: Functions in Python

# The GOLDEN RULE of functions:
# Each function should do ONE job and do it well.
# A function that does 3 things is really 3 functions.

# --- BAD: One function doing everything ---
def process_student_BAD(name, m, s, e):
    # calculates total
    total = m + s + e
    # calculates average
    avg = total / 3
    # determines grade
    if avg >= 80: grade = "A"
    elif avg >= 60: grade = "B"
    else: grade = "C"
    # checks pass/fail
    if m >= 35 and s >= 35 and e >= 35:
        result = "PASS"
    else:
        result = "FAIL"
    # prints the report
    print(f"Student: {name}")
    print(f"Total: {total}, Average: {avg:.1f}")
    print(f"Grade: {grade}, Result: {result}")

print("=== BAD approach (one giant function) ===")
process_student_BAD("Aarav", 85, 72, 90)
print("Problem: Can't reuse just the grade logic, can't test pieces separately.")
print()

# --- GOOD: One job per function ---
def calc_total(m, s, e):
    return m + s + e

def calc_average(total, subjects=3):
    return total / subjects

def get_grade(average):
    if average >= 80: return "A"
    elif average >= 60: return "B"
    else: return "C"

def has_passed(m, s, e):
    return m >= 35 and s >= 35 and e >= 35

def show_report(name, m, s, e):
    total   = calc_total(m, s, e)
    average = calc_average(total)
    grade   = get_grade(average)
    result  = "PASS" if has_passed(m, s, e) else "FAIL"

    print(f"Student: {name}")
    print(f"Total: {total}, Average: {average:.1f}")
    print(f"Grade: {grade}, Result: {result}")

print("=== GOOD approach (one job per function) ===")
show_report("Aarav", 85, 72, 90)
print()

# Benefits of the One Job Rule:
print("=== Why One Job? ===")
print("1. REUSE: Use get_grade() for ANY student without the whole report")
print("2. TEST: Test each function separately to find bugs easily")
print("3. READ: Code reads like English — each function name tells a story")
print("4. FIX: Change grade boundary? Update only get_grade()")
print()

# --- Demonstrate reuse of single-job functions ---
marks_list = [92, 45, 73, 28, 88]
print("Grades for different mark values:")
for m in marks_list:
    avg = calc_average(m, 1)   # treat single mark as average
    print(f"  {m} → {get_grade(avg)}")

# Think:
# 1. Look at process_student_BAD — how many 'jobs' does it do?
# 2. Can you break down a "make_sandwich" task into 5 single-job functions?

# Program Code: FN-LR-03
# Title: Function Call Chain
# Cognitive Skill: Logical Reasoning (Sequential Reasoning)
# Topic: Functions in Python

# Functions call other functions — creating a CHAIN.
# Trace the chain step by step to understand the flow.

def get_total(a, b, c):
    return a + b + c

def get_average(total):
    return total / 3

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"

def get_status(grade):
    if grade == "F":
        return "FAIL"
    return "PASS"

def generate_result(m, s, e):
    total   = get_total(m, s, e)
    average = get_average(total)
    grade   = get_grade(average)
    status  = get_status(grade)
    return total, average, grade, status

# --- Trace the chain ---
print("--- Tracing Function Call Chain ---")
print()
print("Call: generate_result(72, 85, 63)")
print()
print("Step 1: get_total(72, 85, 63)")
t = get_total(72, 85, 63)
print("         returns:", t)
print()
print("Step 2: get_average(" + str(t) + ")")
a = get_average(t)
print("         returns:", round(a, 2))
print()
print("Step 3: get_grade(" + str(round(a, 2)) + ")")
g = get_grade(a)
print("         returns: '" + g + "'")
print()
print("Step 4: get_status('" + g + "')")
s = get_status(g)
print("         returns: '" + s + "'")
print()

# Quiz: Predict before Python confirms
print("--- Now YOU trace it ---")
print()

score = 0

print("Trace: generate_result(30, 25, 40)")
answer1 = input("Step 1 — get_total(30, 25, 40) = ? ")
answer2 = input("Step 2 — get_average(total) ≈ ? (round to 1 decimal) ")
answer3 = input("Step 3 — get_grade(average) = ? (A/B/C/F) ")
answer4 = input("Step 4 — get_status(grade) = ? (PASS/FAIL) ")

total, average, grade, status = generate_result(30, 25, 40)
print("\nAnswers: total=" + str(total) + ", average=" + str(round(average, 1)) + ", grade=" + grade + ", status=" + status)

if answer1.strip() == str(total): score += 1
if answer2.strip() == str(round(average, 1)): score += 1
if answer3.strip().upper() == grade: score += 1
if answer4.strip().upper() == status: score += 1

print("Score:", score, "/ 4")

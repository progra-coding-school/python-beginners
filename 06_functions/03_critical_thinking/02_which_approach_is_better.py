# Program Code: FN-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking (Approach Evaluation)
# Topic: Functions in Python

# Same problem — two approaches. Analyze which is better and WHY.

# --- Scenario 1: Calculate area for 3 shapes ---
print("=== Scenario 1: Calculate area for 3 shapes ===")

# Approach A: No functions — repeated code
length1, width1 = 10, 5
area1 = length1 * width1

length2, width2 = 8, 3
area2 = length2 * width2

length3, width3 = 6, 6
area3 = length3 * width3

print(f"Approach A: {area1}, {area2}, {area3}")

# Approach B: With a function — reusable
def calculate_area(length, width):
    return length * width

print(f"Approach B: {calculate_area(10,5)}, {calculate_area(8,3)}, {calculate_area(6,6)}")

print("Better: B — if formula changes, fix only the function, not 3 places!")
print()

# --- Scenario 2: Print a student result ---
print("=== Scenario 2: Print student result ===")

# Approach A: One giant function doing everything
def process_student_v1(name, m, s, e):
    total = m + s + e
    average = total / 3
    if average >= 80:
        grade = "A"
    elif average >= 60:
        grade = "B"
    else:
        grade = "C"
    print(f"{name}: Total={total}, Avg={average:.1f}, Grade={grade}")

# Approach B: Small, single-purpose functions
def get_total(m, s, e):
    return m + s + e

def get_average_v2(total):
    return total / 3

def get_grade_v2(average):
    if average >= 80: return "A"
    elif average >= 60: return "B"
    else: return "C"

def process_student_v2(name, m, s, e):
    total   = get_total(m, s, e)
    average = get_average_v2(total)
    grade   = get_grade_v2(average)
    print(f"{name}: Total={total}, Avg={average:.1f}, Grade={grade}")

process_student_v1("Aarav", 85, 72, 90)
process_student_v2("Aarav", 85, 72, 90)

print("Better: B — each function does ONE job. Easy to test and fix individually.")
print()

# --- Scenario 3: Using return vs storing in global variable ---
print("=== Scenario 3: Return vs global variable ===")

# Approach A: Storing in a shared variable (bad practice)
shared_result = 0
def add_global(a, b):
    global shared_result
    shared_result = a + b

add_global(5, 3)
print("Approach A result:", shared_result)

# Approach B: Return the value
def add_clean(a, b):
    return a + b

result = add_clean(5, 3)
print("Approach B result:", result)

print("Better: B — return keeps functions independent and safe to reuse.")

# Think:
# 1. What problems can arise if two functions share a global variable?
# 2. How small is 'too small' for a function? Is return x + y worth a function?

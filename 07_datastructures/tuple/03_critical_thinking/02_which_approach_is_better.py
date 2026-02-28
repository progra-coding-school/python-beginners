# Program Code: TU-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking
# Topic: Tuples in Python

# Two approaches solve the same problem.
# Read both, decide which is better and WHY.

# =========================================================
# Problem 1: Store a student's fixed profile
# =========================================================

print("=== Problem 1: Student Profile ===")

# Approach A: list
student_a = ["Aarav", 13, 7, "Chennai"]
print("List approach:", student_a)
student_a[1] = 999      # accidental modification possible!
print("After accident:", student_a)

# Approach B: tuple
student_b = ("Aarav", 13, 7, "Chennai")
print("Tuple approach:", student_b)
try:
    student_b[1] = 999  # impossible
except TypeError:
    print("Tuple protected the data — no accidental change!")

print()
print("Verdict: Tuple is better for a FIXED profile.")
print("  List allows accidental modification.")
print("  Tuple signals: 'this data is read-only'.\n")

# =========================================================
# Problem 2: Return multiple values from a function
# =========================================================

print("=== Problem 2: Return multiple values ===")

# Approach A: use a list
def stats_list(numbers):
    return [min(numbers), max(numbers), sum(numbers)/len(numbers)]

result_a = stats_list([45, 12, 89, 34, 67])
print("List return:", result_a)
result_a[0] = -1    # caller can mutate it — risky
print("After mutation:", result_a)

# Approach B: use a tuple
def stats_tuple(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

low, high, avg = stats_tuple([45, 12, 89, 34, 67])
print(f"Tuple return: low={low}, high={high}, avg={avg:.1f}")

print()
print("Verdict: Tuple is better for returning multiple values.")
print("  Tuple unpacking is clean and readable.")
print("  Caller cannot accidentally mutate the return value.\n")

# =========================================================
# Problem 3: GPS coordinate as a dictionary key
# =========================================================

print("=== Problem 3: GPS coordinate as dict key ===")

# Approach A: list (WILL FAIL)
try:
    bad = {[13.08, 80.27]: "Chennai"}
except TypeError as e:
    print("List key → TypeError:", e)

# Approach B: tuple (works perfectly)
locations = {(13.08, 80.27): "Chennai", (12.97, 77.59): "Bengaluru"}
print("Tuple key → OK:", locations[(13.08, 80.27)])

print()
print("Verdict: Only tuples (not lists) can be dict keys.")
print("  Lists are mutable — their hash can't be computed.")
print("  Tuples are immutable — they have a stable hash.")

# Think:
# 1. In Problem 1, what if you NEED to update the student's grade at year-end?
#    How would you handle that with a tuple-based design?
# 2. Can you think of a case where returning a LIST is better than returning a TUPLE?

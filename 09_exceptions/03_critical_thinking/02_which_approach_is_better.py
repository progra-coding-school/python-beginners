# Program Code: EX-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking
# Topic: Exceptions in Python

# Two approaches solve the same problem.
# Read both, decide which is better and WHY.

# =========================================================
# Problem 1: Parse an integer safely
# =========================================================

print("=== Problem 1: Parse integer safely ===")

# Approach A: check first (LBYL — Look Before You Leap)
def parse_lbyl(text):
    if text.lstrip("-").isdigit():
        return int(text)
    return None

# Approach B: try/except (EAFP — Easier to Ask Forgiveness than Permission)
def parse_eafp(text):
    try:
        return int(text)
    except ValueError:
        return None

tests = ["42", "-5", "3.14", "hello", "0", "99abc"]
print(f"  {'Input':<10} {'LBYL':>8} {'EAFP':>8}")
for t in tests:
    print(f"  {t:<10} {str(parse_lbyl(t)):>8} {str(parse_eafp(t)):>8}")

print()
print("Verdict: Approach B (EAFP) is more Pythonic.")
print("  LBYL misses edge cases like '3.14' or '99abc'.")
print("  EAFP lets Python define what 'valid' means.")

print()

# =========================================================
# Problem 2: Access a dictionary key safely
# =========================================================

print("=== Problem 2: Safe dict access ===")
student = {"name": "Aarav", "grade": 7}

# Approach A: if check
if "age" in student:
    print("Age (A):", student["age"])
else:
    print("Age (A): Not available")

# Approach B: try/except
try:
    print("Age (B):", student["age"])
except KeyError:
    print("Age (B): Not available")

# Approach C: .get() (best for this specific case)
print("Age (C):", student.get("age", "Not available"))

print()
print("Verdict: C (.get()) wins for simple dict access.")
print("  A and B are fine but more verbose for a simple lookup.")
print("  Use try/except when multiple things inside could fail.")

print()

# =========================================================
# Problem 3: Validate user score (0–100)
# =========================================================

print("=== Problem 3: Validate score ===")

# Approach A: if/else only
def validate_if(score):
    if not isinstance(score, int):
        return "Not an integer"
    if score < 0 or score > 100:
        return "Out of range"
    return score

# Approach B: raise exceptions
def validate_raise(score):
    if not isinstance(score, int):
        raise TypeError("Score must be an integer")
    if score < 0 or score > 100:
        raise ValueError("Score must be 0–100")
    return score

for val in [85, -5, 110, "A+"]:
    print(f"  if/else: {validate_if(val)}")
    try:
        print(f"  raise  : {validate_raise(val)}")
    except (ValueError, TypeError) as e:
        print(f"  raise  : {type(e).__name__}: {e}")
    print()

print("Verdict: raising exceptions is better for library/function code.")
print("  The caller decides how to handle the error.")
print("  if/else returning strings mixes error and success return values.")

# Think:
# 1. What does LBYL stand for? What does EAFP stand for?
# 2. When would you choose if/else over try/except?

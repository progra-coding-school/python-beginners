# Program Code: EX-ST-03
# Title: When to Use Exceptions vs Conditions
# Cognitive Skill: Structured Thinking
# Topic: Exceptions in Python

# Rule of thumb:
#   if/else  → for EXPECTED conditions in normal program flow
#   try/except → for UNEXPECTED situations or external failures

print("=== Decision Guide: if/else vs try/except ===\n")

# --- Scenario 1: Check if a list is empty ---
print("Scenario 1: Is the list empty?")
print("→ EXPECTED condition — use if/else")
scores = []
if scores:
    print(f"  Average: {sum(scores)/len(scores):.1f}")
else:
    print("  No scores yet.")
print()

# --- Scenario 2: Parse user-typed age ---
print("Scenario 2: Parse age from user input")
print("→ UNEXPECTED failure — user might type anything, use try/except")
for raw in ["13", "thirteen", "13.5"]:
    try:
        age = int(raw)
        print(f"  '{raw}' → age = {age}")
    except ValueError:
        print(f"  '{raw}' → not a valid age")
print()

# --- Scenario 3: Check if student passed ---
print("Scenario 3: Did the student pass (score >= 50)?")
print("→ EXPECTED condition — use if/else")
mark = 47
if mark >= 50:
    print("  Pass")
else:
    print("  Fail — needs to reappear")
print()

# --- Scenario 4: Read from a file ---
print("Scenario 4: Read marks from a file")
print("→ UNEXPECTED failure — file may not exist, use try/except")
try:
    with open("marks.csv", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("  File 'marks.csv' not found. Please create it first.")
except PermissionError:
    print("  Cannot read 'marks.csv' — permission denied.")
print()

# --- Scenario 5: Find a student in a list ---
print("Scenario 5: Is 'Aarav' enrolled?")
print("→ EXPECTED condition — use 'in' operator (not try/except)")
enrolled = ["Aarav", "Diya", "Karthik"]
name = "Riya"
if name in enrolled:
    print(f"  {name} is enrolled.")
else:
    print(f"  {name} is not enrolled.")
print()

# --- Quick Reference ---
print("=== Quick Reference ===")
cases = [
    ("List/dict membership check",      "if 'key' in d"),
    ("Empty collection",                "if not lst"),
    ("Comparing values",                "if a > b"),
    ("Parsing unknown external input",  "try/except ValueError"),
    ("File/network operations",         "try/except IOError"),
    ("Type mismatch in operation",      "try/except TypeError"),
    ("Division where 0 is possible",    "try/except ZeroDivisionError"),
]
for situation, approach in cases:
    print(f"  {situation:<40} → {approach}")

# Think:
# 1. What is the key difference between "expected" and "unexpected" errors?
# 2. Can you think of a case where you would use BOTH if/else AND try/except together?

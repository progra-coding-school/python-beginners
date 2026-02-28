# Program Code: EX-ST-02
# Title: Naming Matters — Meaningful Exception Messages
# Cognitive Skill: Structured Thinking
# Topic: Exceptions in Python

# A good exception message tells WHAT went wrong, WHY, and HOW to fix it.
# A bad message just says "error" and leaves the user confused.

# ─── VERSION A: Poor exception messages ─────────────────────────
print("=== Version A: Poor messages (confusing) ===")

def register_a(name, age):
    try:
        age = int(age)
        if age < 5 or age > 18:
            raise ValueError("Invalid")     # Too vague!
    except ValueError:
        print("Error!")                     # Which error? What to do?

register_a("Aarav", 25)
register_a("Diya", "abc")

print()

# ─── VERSION B: Good exception messages ─────────────────────────
print("=== Version B: Good messages (clear and helpful) ===")

def register_b(name, age_str):
    try:
        age = int(age_str)
    except ValueError:
        print(f"Registration failed: age '{age_str}' is not a valid number.")
        return
    if age < 5 or age > 18:
        print(f"Registration failed: age {age} is out of range. "
              f"Students must be between 5 and 18 years old.")
        return
    print(f"Registered: {name}, Age {age}")

register_b("Aarav", "25")
register_b("Diya",  "abc")
register_b("Riya",  "12")

print()

# ─── Message quality guidelines ─────────────────────────────────
print("=== Exception Message Guidelines ===")
examples = [
    ("Poor",  "Error"),
    ("Poor",  "Invalid input"),
    ("Poor",  "Failed"),
    ("Good",  "Score 150 is out of range. Must be 0–100."),
    ("Good",  "Student ID 999 not found. Check the ID and try again."),
    ("Good",  "Cannot divide Rs.0 among 3 students: total must be > 0."),
]
for quality, msg in examples:
    marker = "✓" if quality == "Good" else "✗"
    print(f"  {marker} [{quality:4}] {msg}")

print()

# ─── Practice: improve these messages ───────────────────────────
print("=== Practice: Write better messages ===")

# Poor: raise ValueError("Bad")
# Better:
try:
    score = -5
    if score < 0:
        raise ValueError(f"Score {score} is invalid — scores cannot be negative.")
except ValueError as e:
    print(f"  Improved: {e}")

# Poor: raise KeyError("not found")
# Better:
try:
    subject = "Drawing"
    valid   = {"Maths", "Science", "English"}
    if subject not in valid:
        raise KeyError(f"Subject '{subject}' not found. Valid subjects: {sorted(valid)}")
except KeyError as e:
    print(f"  Improved: {e}")

# Think:
# 1. What three things should a good exception message always include?
# 2. How would you make the message different for developers vs students reading it?

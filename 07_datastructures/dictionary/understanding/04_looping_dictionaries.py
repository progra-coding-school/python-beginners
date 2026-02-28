# Program Code: DC-UN-04
# Title: Looping Through Dictionaries
# Cognitive Skill: Understanding
# Topic: Dictionaries in Python

marks = {
    "Maths":   85,
    "Science": 90,
    "English": 78,
    "History": 88,
}

# --- Loop 1: over KEYS (default behaviour) ---
print("=== Looping over keys ===")
for subject in marks:           # same as: for subject in marks.keys()
    print(f"  Subject: {subject}")

print()

# --- Loop 2: over VALUES ---
print("=== Looping over values ===")
for score in marks.values():
    print(f"  Score: {score}")

print()

# --- Loop 3: over KEY-VALUE PAIRS (most useful!) ---
print("=== Looping over key-value pairs ===")
for subject, score in marks.items():
    print(f"  {subject}: {score}")

print()

# --- Practical: find the topper ---
print("=== Finding highest scorer ===")
students = {"Aarav": 85, "Diya": 92, "Karthik": 78, "Riya": 88}

best_name  = None
best_score = 0

for name, score in students.items():
    if score > best_score:
        best_score = score
        best_name  = name

print(f"Topper: {best_name} with {best_score} marks")

print()

# --- Practical: build a new dict while looping ---
print("=== Grade labels from marks ===")

def grade_label(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

grades = {}
for subject, score in marks.items():
    grades[subject] = grade_label(score)

for subject, grade in grades.items():
    print(f"  {subject}: {grade}")

print()

# --- Practical: filter a dictionary ---
print("=== Subjects with score above 85 ===")
high_scores = {}
for subject, score in marks.items():
    if score > 85:
        high_scores[subject] = score

print("High scorers:", high_scores)

# Think:
# 1. What is the difference between looping with .keys() vs .items()?
# 2. How would you count how many subjects have a score above 80?

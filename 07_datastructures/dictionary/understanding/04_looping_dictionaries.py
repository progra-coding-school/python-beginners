# Looping Through Dictionaries
# Three ways to loop — each gives you different data:
#   for key in dict:                → gives only the keys (default loop)
#   for value in dict.values():     → gives only the values
#   for key, value in dict.items(): → gives BOTH key and value (most useful!)
# Always use .items() when you need to print or process both the key and value.

marks = {
    "Maths":   85,
    "Science": 90,
    "English": 78,
    "History": 88,
}

# Loop Style 1: over keys only — looping a dict directly gives you the keys
# Same as: for subject in marks.keys()
# Use when you only need to know the keys, not the values
print("Looping over keys:")
for subject in marks:
    print("  Subject:", subject)

print()

# Loop Style 2: over values only
# Use when you only need the numbers/data, not the labels
print("Looping over values:")
for score in marks.values():
    print("  Score:", score)

print()

# Loop Style 3: over key-value pairs with .items() — the most useful loop
# Use when you need BOTH the key and value at the same time
print("Looping over key-value pairs:")
for subject, score in marks.items():
    print("  " + subject + ":", score)

print()

# Practical: find the highest scorer
# Start with "no winner" and update whenever we find a higher score
print("Finding highest scorer:")
students = {"Aarav": 85, "Diya": 92, "Karthik": 78, "Riya": 88}

best_name  = None
best_score = 0

for name, score in students.items():
    if score > best_score:
        best_score = score
        best_name  = name

print("Topper:", best_name, "with", best_score, "marks")

print()

# Practical: build a new dict while looping through an existing one
# Loop through marks → convert each score to a grade letter → store in new dict
print("Grade labels from marks:")

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
    grades[subject] = grade_label(score)   # build a new dict: subject → grade letter

for subject, grade in grades.items():
    print("  " + subject + ":", grade)

print()

# Practical: filter a dictionary — keep only entries that match a condition
print("Subjects with score above 85:")
high_scores = {}
for subject, score in marks.items():
    if score > 85:
        high_scores[subject] = score   # only add to new dict if condition is met

print("High scorers:", high_scores)

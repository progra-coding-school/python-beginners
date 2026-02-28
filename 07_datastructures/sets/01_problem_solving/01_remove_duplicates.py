# Program Code: SE-PS-01
# Title: Remove Duplicates from a List
# Cognitive Skill: Problem Solving
# Topic: Sets in Python

# Problem:
# The school collected student names from a sign-up form.
# Many students submitted the form more than once.
# Find the unique names and count how many actually signed up.

# --- Step 1: Raw sign-up data (with duplicates) ---
signups = [
    "Aarav", "Diya", "Karthik", "Aarav",
    "Riya",  "Diya", "Ananya",  "Karthik",
    "Vivek", "Aarav", "Riya",   "Ananya",
]

print("=== Sign-up Form Entries ===")
print("Raw entries    :", signups)
print("Total entries  :", len(signups))

print()

# --- Step 2: Remove duplicates using a set ---
unique_students = set(signups)
print("Unique students:", unique_students)
print("Actual count   :", len(unique_students))
print(f"Duplicate entries removed: {len(signups) - len(unique_students)}")

print()

# --- Step 3: Restore order if needed (sorted) ---
print("=== Sorted unique list ===")
sorted_students = sorted(unique_students)   # convert back to list, alphabetically sorted
for i, name in enumerate(sorted_students, 1):
    print(f"  {i}. {name}")

print()

# --- Step 4: Real-world extension — find who submitted multiple times ---
print("=== Who submitted more than once? ===")
seen = set()
duplicates = set()

for name in signups:
    if name in seen:
        duplicates.add(name)
    else:
        seen.add(name)

print("Submitted more than once:", duplicates)

print()

# --- Step 5: Deduplication in one line ---
print("=== One-line deduplication ===")
unique_one_line = list(set(signups))
print("Result:", unique_one_line)

# Think:
# 1. Why did we use sorted() when printing — what does a raw set look like?
# 2. How would you deduplicate a list of email addresses for a newsletter?

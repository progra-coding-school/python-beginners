# Remove Duplicates from a List
# Problem: a sign-up form collected names but many students submitted more than once.
# Find the unique names, count actual sign-ups, and identify who submitted multiple times.

# --- Step 1: Raw sign-up data (with duplicates) ---
signups = [
    "Aarav", "Diya", "Karthik", "Aarav",
    "Riya",  "Diya", "Ananya",  "Karthik",
    "Vivek", "Aarav", "Riya",   "Ananya",
]

print("Sign-up Form Entries:")
print("Raw entries    :", signups)
print("Total entries  :", len(signups))

print()

# --- Step 2: Remove duplicates using a set ---
# set() instantly discards all duplicates — no loop needed
unique_students = set(signups)
print("Unique students:", unique_students)
print("Actual count   :", len(unique_students))
print("Duplicate entries removed:", len(signups) - len(unique_students))

print()

# --- Step 3: Restore order if needed (sorted) ---
# Sets are unordered; sorted() converts to a list in alphabetical order
print("Sorted unique list:")
sorted_students = sorted(unique_students)   # convert back to list, alphabetically sorted
for i, name in enumerate(sorted_students, 1):
    print("  " + str(i) + ". " + name)

print()

# --- Step 4: Real-world extension — find who submitted multiple times ---
# Two sets: 'seen' tracks first occurrence; 'duplicates' catches second occurrence
print("Who submitted more than once?")
seen = set()
duplicates = set()

for name in signups:
    if name in seen:
        duplicates.add(name)    # second time we saw this name
    else:
        seen.add(name)          # first time — note it

print("Submitted more than once:", duplicates)

print()

# --- Step 5: Deduplication in one line ---
# list(set(...)) is the standard one-liner pattern for removing duplicates
print("One-line deduplication:")
unique_one_line = list(set(signups))
print("Result:", unique_one_line)

# Think:
# 1. Why did we use sorted() when printing — what does a raw set look like?
# 2. How would you deduplicate a list of email addresses for a newsletter?

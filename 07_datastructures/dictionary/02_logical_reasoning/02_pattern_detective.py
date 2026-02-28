# Program Code: DC-LR-02
# Title: Pattern Detective
# Cognitive Skill: Logical Reasoning
# Topic: Dictionaries in Python

# Spot the pattern in each code block.
# Name it, then complete the missing piece.

# --- Pattern 1: Counting with a dictionary ---
print("=== Pattern 1: Counting ===")
votes = ["cricket", "football", "cricket", "hockey", "cricket", "football"]

tally = {}
for sport in votes:
    tally[sport] = tally.get(sport, 0) + 1   # <- what does this line do?

print("Votes tally:", tally)
# Pattern: builds a frequency/count dictionary

print()

# --- Pattern 2: Grouping with a dictionary ---
print("=== Pattern 2: Grouping ===")
students = [
    ("Aarav",   "A"),
    ("Diya",    "B"),
    ("Karthik", "A"),
    ("Riya",    "B"),
    ("Ananya",  "A"),
]

classes = {}
for name, section in students:
    if section not in classes:
        classes[section] = []       # start a new list for that section
    classes[section].append(name)  # add student to their section

for section, names in classes.items():
    print(f"  Section {section}: {names}")
# Pattern: groups items into lists inside a dictionary

print()

# --- Pattern 3: Inverting a dictionary ---
print("=== Pattern 3: Inverting keys and values ===")
colour_codes = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

inverted = {}
for name, code in colour_codes.items():
    inverted[code] = name           # swap key and value

print("Original:", colour_codes)
print("Inverted:", inverted)
# Pattern: look up by code instead of by name

print()

# --- Pattern 4: Merging two dictionaries ---
print("=== Pattern 4: Merging ===")
term1 = {"Maths": 85, "Science": 90}
term2 = {"English": 78, "Maths": 88}   # Maths appears in both!

merged = {}
merged.update(term1)
merged.update(term2)    # Maths will be overwritten by term2 value

print("Merged:", merged)
# Pattern: later .update() wins for duplicate keys

# Think:
# 1. In Pattern 2, what would happen if you used a dictionary of sets instead of lists?
# 2. In Pattern 4, how would you keep the HIGHER Maths score instead of the later one?

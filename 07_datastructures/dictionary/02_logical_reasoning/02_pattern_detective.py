# Pattern Detective
# Every dictionary program uses one of a small set of patterns.
# Learn to recognise these patterns — then you can build any program.
# Four patterns: COUNTING, GROUPING, INVERTING, MERGING.

# Pattern 1: Counting — build a frequency dict
# For each item, either start a count at 1 or add 1 to an existing count.
# .get(sport, 0) safely returns 0 for new sports (instead of crashing on missing key)
print("Pattern 1: Counting")
votes = ["cricket", "football", "cricket", "hockey", "cricket", "football"]

tally = {}
for sport in votes:
    tally[sport] = tally.get(sport, 0) + 1   # get current count (0 if new) + 1

print("Votes tally:", tally)
# Result: {'cricket': 3, 'football': 2, 'hockey': 1}

print()

# Pattern 2: Grouping — collect items that share a common property into lists
# For each (name, section) pair, add the name to the correct section's list.
# "if section not in classes" creates a new empty list for each new section seen first.
print("Pattern 2: Grouping")
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
        classes[section] = []           # first student in this section → create empty list
    classes[section].append(name)       # add student to their section's list

for section, names in classes.items():
    print("  Section " + section + ":", names)

print()

# Pattern 3: Inverting — swap keys and values
# Useful when you need to look up by value instead of by key.
# Original: name → hex code.  Inverted: hex code → name.
print("Pattern 3: Inverting keys and values")
colour_codes = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}

inverted = {}
for name, code in colour_codes.items():
    inverted[code] = name           # the old VALUE becomes the new KEY

print("Original:", colour_codes)
print("Inverted:", inverted)

print()

# Pattern 4: Merging — combine two dictionaries into one
# .update() adds all pairs from one dict into another.
# If the same key exists in both dicts, the LAST .update() wins.
print("Pattern 4: Merging")
term1 = {"Maths": 85, "Science": 90}
term2 = {"English": 78, "Maths": 88}   # Maths appears in BOTH!

merged = {}
merged.update(term1)    # Maths = 85
merged.update(term2)    # Maths = 88 (overwrites 85 — later update wins)

print("Merged:", merged)
# Result: {'Maths': 88, 'Science': 90, 'English': 78}

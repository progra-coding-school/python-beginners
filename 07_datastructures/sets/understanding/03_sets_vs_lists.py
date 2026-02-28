# Program Code: SE-UN-03
# Title: Sets vs Lists — When to Use Which
# Cognitive Skill: Understanding
# Topic: Sets in Python

# The right tool for the right job.
# Choosing between a list and a set changes how your program behaves.

print("=== Feature Comparison ===")
features = {
    "Ordered (keeps position)": ("YES", "NO"),
    "Allows duplicates"       : ("YES", "NO"),
    "Index access (items[0])" : ("YES", "NO"),
    "Fast membership check"   : ("slow", "fast"),
    "Set math (union etc.)"   : ("NO",  "YES"),
    "Mutable"                 : ("YES", "YES"),
}

print(f"  {'Feature':<35} {'LIST':>6}  {'SET':>6}")
print(f"  {'─'*35} {'─'*6}  {'─'*6}")
for feature, (lst, st) in features.items():
    print(f"  {feature:<35} {lst:>6}  {st:>6}")

print()

# --- Use a LIST when... ---
print("=== Use a LIST when ===")
# 1. Order matters (first item is different from last)
queue = ["Aarav", "Diya", "Karthik"]    # Aarav is first in line
print("Queue (order matters):", queue)

# 2. Duplicates are meaningful
scores = [10, 10, 8, 7, 10]             # three 10s are valid scores
print("Scores (duplicates ok):", scores)

# 3. You need index access
print("Third score:", scores[2])        # positional access needed

print()

# --- Use a SET when... ---
print("=== Use a SET when ===")
# 1. You want unique items only
attendance = set()
swipes = ["Aarav", "Diya", "Aarav", "Karthik", "Diya"]  # badge swipes
for name in swipes:
    attendance.add(name)
print("Unique attendees:", attendance)

# 2. You need fast membership checks
allowed_users = {"admin", "teacher", "principal"}
login = "teacher"
if login in allowed_users:              # near-instant, even with millions of users
    print(f"'{login}' is allowed.")

# 3. You need set math
class_a = {"Aarav", "Diya", "Riya"}
class_b = {"Diya", "Karthik", "Riya"}
common  = class_a & class_b
print("Students in both classes:", common)

print()
print("=== Quick Decision Guide ===")
print("  Need order or index?        → LIST")
print("  Need duplicates?            → LIST")
print("  Need unique items only?     → SET")
print("  Need fast 'in' check?       → SET")
print("  Need union/intersection?    → SET")

# Think:
# 1. Which would you use to store the top 10 scorers in ORDER? Why?
# 2. Which would you use to store which students have submitted homework? Why?

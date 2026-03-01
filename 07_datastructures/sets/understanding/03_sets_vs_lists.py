# Sets vs Lists — When to Use Which
# Lists: ordered, allow duplicates, index access. Sets: unique, fast lookup, set math.
# Choosing the right one prevents bugs and makes code faster.

# --- Feature comparison table ---
print("Feature Comparison:")
features = {
    "Ordered (keeps position)": ("YES", "NO"),
    "Allows duplicates"       : ("YES", "NO"),
    "Index access (items[0])" : ("YES", "NO"),
    "Fast membership check"   : ("slow", "fast"),
    "Set math (union etc.)"   : ("NO",  "YES"),
    "Mutable"                 : ("YES", "YES"),
}

# ljust pads text to a fixed width (left-aligned); rjust pads right-aligned
print("  " + "Feature".ljust(35) + "LIST".rjust(6) + "  " + "SET".rjust(6))
print("  " + "-" * 35 + " " + "-" * 6 + "  " + "-" * 6)
for feature, (lst, st) in features.items():
    print("  " + feature.ljust(35) + lst.rjust(6) + "  " + st.rjust(6))

print()

# --- Use a LIST when... ---
print("Use a LIST when:")
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
print("Use a SET when:")
# 1. You want unique items only — set rejects duplicates automatically
attendance = set()
swipes = ["Aarav", "Diya", "Aarav", "Karthik", "Diya"]  # badge swipes (duplicates ok to receive)
for name in swipes:
    attendance.add(name)
print("Unique attendees:", attendance)

# 2. You need fast membership checks — 'in' is instant on a set
allowed_users = {"admin", "teacher", "principal"}
login = "teacher"
if login in allowed_users:              # near-instant, even with millions of users
    print("'" + login + "' is allowed.")

# 3. You need set math — union, intersection, difference work directly
class_a = {"Aarav", "Diya", "Riya"}
class_b = {"Diya", "Karthik", "Riya"}
common  = class_a & class_b
print("Students in both classes:", common)

print()

# --- Quick Decision Guide ---
print("Quick Decision Guide:")
print("  Need order or index?        → LIST")
print("  Need duplicates?            → LIST")
print("  Need unique items only?     → SET")
print("  Need fast 'in' check?       → SET")
print("  Need union/intersection?    → SET")

# Think:
# 1. Which would you use to store the top 10 scorers in ORDER? Why?
# 2. Which would you use to store which students have submitted homework? Why?

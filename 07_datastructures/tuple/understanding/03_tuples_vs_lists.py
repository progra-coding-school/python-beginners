# Program Code: TU-UN-03
# Title: Tuples vs Lists — When to Use Which
# Cognitive Skill: Understanding
# Topic: Tuples in Python

print("=== Feature Comparison ===")
features = {
    "Ordered (keeps position)": ("YES",     "YES"),
    "Allows duplicates"       : ("YES",     "YES"),
    "Index access (items[0])" : ("YES",     "YES"),
    "Mutable (can change)"    : ("YES",     "NO"),
    "Used as dict key"        : ("NO",      "YES"),
    "Memory efficient"        : ("less",    "more"),
    "Number of methods"       : ("many",    "2 only"),
    "Signals fixed data"      : ("NO",      "YES"),
}
print(f"  {'Feature':<35} {'LIST':>8}  {'TUPLE':>6}")
print(f"  {'─'*35} {'─'*8}  {'─'*6}")
for feature, (lst, tup) in features.items():
    print(f"  {feature:<35} {lst:>8}  {tup:>6}")

print()

# --- Use a LIST when data CHANGES ---
print("=== Use a LIST when ===")
# Shopping cart — items are added and removed
cart = ["mango", "banana"]
cart.append("apple")
cart.remove("banana")
print("Cart (changes):", cart)

# Student scores over a semester — updated each term
scores = [85, 90]
scores.append(78)
print("Scores (grows):", scores)

print()

# --- Use a TUPLE when data is FIXED ---
print("=== Use a TUPLE when ===")
# GPS coordinates — never change
location   = (13.0827, 80.2707)
print("Chennai coordinates:", location)

# RGB colour — fixed definition
crimson    = (220, 20, 60)
print("Crimson RGB:", crimson)

# Database record returned from a query (read-only)
student_record = ("Aarav", "Class 7", "Progra School")
print("Student record:", student_record)

# Returning multiple values from a function
def get_range(data):
    return min(data), max(data)     # tuple

low, high = get_range([45, 12, 89, 34])
print(f"Range: {low} to {high}")

print()
print("=== Quick Decision Guide ===")
print("  Data changes over time?          → LIST")
print("  Data is a fixed snapshot?        → TUPLE")
print("  Need as a dictionary key?        → TUPLE")
print("  Returning multiple values?       → TUPLE")
print("  Collecting items in a loop?      → LIST")

# Think:
# 1. Would you store a cricket team's playing XI as a list or a tuple? (Hint: can the team change?)
# 2. Would you store all matches in a season as a list or a tuple? Why?

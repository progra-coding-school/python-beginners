# Pattern Detective
# Spot the pattern in each block. Name it, then complete the missing piece.
# Recognising patterns lets you reuse proven solutions instead of reinventing them.

# --- Pattern 1: Deduplication ---
# list → set → list is the standard way to remove all duplicates from a list
print("Pattern 1: Deduplication:")
raw = ["cricket", "football", "cricket", "hockey", "football", "cricket"]
unique = list(set(raw))
print("Pattern: list → set → list removes all duplicates")
print("Result:", sorted(unique))

print()

# --- Pattern 2: Membership gate ---
# Store allowed values in a set; 'in' check is near-instant for any collection size
print("Pattern 2: Membership gate:")
allowed = {"admin", "teacher", "librarian"}
users   = ["student", "teacher", "admin", "guest", "librarian"]

for user in users:
    if user in allowed:
        print("  " + user.ljust(12) + " → Access GRANTED")
    else:
        print("  " + user.ljust(12) + " → Access DENIED")

print("Pattern: set is used as a fast lookup table for allowed values")

print()

# --- Pattern 3: Growing a set across loops ---
# Start with an empty set; .add() inside a loop accumulates unique values
print("Pattern 3: Accumulating unique values:")
seen_cities = set()
bookings    = [
    ("Aarav",   "Chennai"),
    ("Diya",    "Madurai"),
    ("Karthik", "Chennai"),
    ("Riya",    "Coimbatore"),
    ("Ananya",  "Madurai"),
]

for name, city in bookings:
    seen_cities.add(city)    # duplicates are silently ignored

print("Cities covered:", sorted(seen_cities))
print("Total bookings:", len(bookings), "| Unique cities:", len(seen_cities))
print("Pattern: .add() to a set collects unique values across loops")

print()

# --- Pattern 4: Comparing two groups ---
# Snapshot comparison — set difference tracks what changed between two states
print("Pattern 4: Who is new / who left:")
last_week = {"Aarav", "Diya", "Karthik", "Riya"}
this_week = {"Diya", "Karthik", "Ananya", "Vivek"}

new_members  = this_week - last_week   # in this week but NOT last week
left_members = last_week - this_week   # in last week but NOT this week
still_here   = last_week & this_week   # in both

print("New members   :", sorted(new_members))
print("Left members  :", sorted(left_members))
print("Still here    :", sorted(still_here))
print("Pattern: set difference tracks changes between two snapshots")

# Think:
# 1. Where have you seen Pattern 2 (membership gate) in real life? (e.g., school ID check)
# 2. In Pattern 4, how would you find members who were in NEITHER week?

# Program Code: TU-ST-03
# Title: When to Use Tuples — Choosing the Right Structure
# Cognitive Skill: Structured Thinking
# Topic: Tuples in Python

# For each scenario, choose: list, tuple, set, or dict?
# Then see the correct choice and reason.

print("=== Scenario Decision Guide ===\n")

# --- Scenario 1: RGB colour ---
print("Scenario 1: Store Red=255, Green=128, Blue=0 for 'orange'")
print("Need: fixed 3-value record, used as dict key possible")
orange = (255, 128, 0)
print(f"Best choice: TUPLE → {orange}\n")

# --- Scenario 2: Shopping cart ---
print("Scenario 2: Items added by the user while shopping")
print("Need: grows as user adds items, can be removed, order matters")
cart = ["idli", "dosa", "chai"]
cart.append("vada")
print(f"Best choice: LIST → {cart}\n")

# --- Scenario 3: Coordinates as map keys ---
print("Scenario 3: Store city names keyed by GPS (lat, lon)")
print("Need: fixed pair as key, city name as value")
city_map = {(13.08, 80.27): "Chennai", (12.97, 77.59): "Bengaluru"}
print(f"Best choice: TUPLE keys in DICT → {city_map}\n")

# --- Scenario 4: Student IDs in a batch ---
print("Scenario 4: 200 student IDs — check if one is enrolled")
print("Need: fast lookup, no duplicates")
enrolled = {1001, 1002, 1003, 1004}   # set for fast lookup
print(f"Best choice: SET → {enrolled}\n")

# --- Scenario 5: Class timetable ---
print("Scenario 5: For each day, know which subject is taught")
print("Need: key (day) → value (subject)")
timetable = {"Mon": "Maths", "Tue": "Science", "Wed": "English"}
print(f"Best choice: DICT → {timetable}\n")

# --- Scenario 6: Match results (read-only history) ---
print("Scenario 6: Store past cricket match results — never to be edited")
print("Need: ordered, fixed records, read-only")
results = (
    ("India vs Aus",   287, "Win"),
    ("India vs Eng",   210, "Loss"),
    ("India vs WI",    312, "Win"),
)
print("Best choice: TUPLE of tuples →")
for match, runs, result in results:
    print(f"  {match}: {runs} runs → {result}")

print()
print("=== Quick Guide ===")
print("  Fixed record, read-only, dict key → TUPLE")
print("  Changes over time, ordered        → LIST")
print("  Unique items, fast lookup         → SET")
print("  Key-value pairs                   → DICT")

# Think:
# 1. Would you store a student's exam history (grows each term) as a tuple or list?
# 2. Would you store the final year-end grades as a tuple or list? Why the difference?

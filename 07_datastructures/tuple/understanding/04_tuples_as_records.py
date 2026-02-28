# Program Code: TU-UN-04
# Title: Tuples as Records
# Cognitive Skill: Understanding
# Topic: Tuples in Python

# Tuples shine when representing a FIXED RECORD —
# a row of data where each position has a defined meaning.

# --- A student record: (name, age, grade, city) ---
print("=== Student Records ===")
students = [
    ("Aarav",   13, 7, "Chennai"),
    ("Diya",    12, 6, "Madurai"),
    ("Karthik", 14, 8, "Coimbatore"),
    ("Riya",    11, 5, "Trichy"),
]

print(f"  {'Name':<12} {'Age':>4} {'Grade':>6} {'City'}")
print(f"  {'─'*12} {'─'*4} {'─'*6} {'─'*12}")
for name, age, grade, city in students:     # unpacking each record
    print(f"  {name:<12} {age:>4} {grade:>6} {city}")

print()

# --- Each position has a fixed meaning ---
print("=== Accessing by position ===")
s = ("Karthik", 14, 8, "Coimbatore")
print("Name  [0]:", s[0])
print("Age   [1]:", s[1])
print("Grade [2]:", s[2])
print("City  [3]:", s[3])

print()

# --- RGB colour palette — each tuple is one colour ---
print("=== Colour Palette (RGB Records) ===")
palette = {
    "red"    : (255,   0,   0),
    "green"  : (  0, 255,   0),
    "blue"   : (  0,   0, 255),
    "yellow" : (255, 255,   0),
    "crimson": (220,  20,  60),
}
for name, (r, g, b) in palette.items():    # unpacking the RGB tuple
    print(f"  {name:<10} R={r:>3} G={g:>3} B={b:>3}")

print()

# --- Real-world: list of cricket match results ---
print("=== Cricket Match Results ===")
# Each record: (match_number, team, runs, wickets)
results = [
    (1, "India",     287, 5),
    (2, "Australia", 243, 8),
    (3, "India",     312, 4),
]
for match, team, runs, wickets in results:
    print(f"  Match {match}: {team:<12} {runs} runs for {wickets} wickets")

winner = max(results, key=lambda r: r[2])   # highest runs
print(f"\nHighest score: {winner[1]} with {winner[2]} runs")

# Think:
# 1. What would you use if you needed to ADD a new field to each student record later?
# 2. How is a tuple-as-record similar to a row in a spreadsheet?

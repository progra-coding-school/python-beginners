# Reverse Engineer the Dictionary
# You see the TARGET OUTPUT — your job is to write the code that produces it.
# This is harder than reading examples because you must think backwards:
#   What structure do I need? → What operation creates that? → What input data?

# Challenge 1: Values are squares of 1, 2, 3
# Target: {'a': 1, 'b': 4, 'c': 9}
# Observation: 'a'→1 (1²), 'b'→4 (2²), 'c'→9 (3²) — square each position value
print("Challenge 1 — Write code to get this output:")
print("{'a': 1, 'b': 4, 'c': 9}")
print()

keys   = ['a', 'b', 'c']
values = [1, 2, 3]
result = {}
for i in range(len(keys)):
    result[keys[i]] = values[i] ** 2   # key → value squared
print("Result:", result)

print()

# Challenge 2: Number → "odd" or "even" label
# Target: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
# Observation: n % 2 == 0 → even, otherwise → odd
print("Challenge 2 — Odd/even labels:")
print("{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}")
print()

labels = {}
for n in range(1, 6):
    labels[n] = "even" if n % 2 == 0 else "odd"   # ternary picks the right label
print("Result:", labels)

print()

# Challenge 3: Group players by sport — the GROUPING pattern
# Target: Cricket: ['Aarav', 'Karthik'], Football: ['Diya', 'Riya']
# Observation: sport is the key, list of players is the value
print("Challenge 3 — Group by sport:")
print("Cricket team  : ['Aarav', 'Karthik']")
print("Football team : ['Diya', 'Riya']")
print()

players = [
    ("Aarav",   "Cricket"),
    ("Diya",    "Football"),
    ("Karthik", "Cricket"),
    ("Riya",    "Football"),
]

teams = {}
for name, sport in players:
    if sport not in teams:
        teams[sport] = []           # create list for this sport on first occurrence
    teams[sport].append(name)

for sport, names in teams.items():
    print("  " + sport.ljust(15) + ": " + str(names))

print()

# Challenge 4: Reverse keys and values — the INVERSION pattern
# Input: fruit → colour.  Output: colour → fruit
# Observation: old value becomes new key, old key becomes new value
print("Challenge 4 — Reverse keys and values:")
original = {"apple": "red", "banana": "yellow", "grape": "purple"}
flipped  = {}

for fruit, colour in original.items():
    flipped[colour] = fruit   # colour becomes key, fruit becomes value

print("Original:", original)
print("Flipped :", flipped)

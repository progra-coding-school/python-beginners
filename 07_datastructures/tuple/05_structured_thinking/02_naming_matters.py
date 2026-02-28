# Program Code: TU-ST-02
# Title: Naming Matters
# Cognitive Skill: Structured Thinking
# Topic: Tuples in Python

# Good names make tuple code readable without comments.
# Compare the same logic with poor vs good naming.

# ─── VERSION A: Poor naming ─────────────────────────────────────
print("=== Version A: Poor naming ===")

d = (15, 8, 2012)
print(d[0], d[1], d[2])
# What does d represent? What are 15, 8, 2012?

r = (13.0827, 80.2707)
print(r)
# Is this a price? A size? A coordinate?

print()

# ─── VERSION B: Good naming ─────────────────────────────────────
print("=== Version B: Good naming ===")

date_of_birth = (15, 8, 2012)           # day, month, year
day, month, year = date_of_birth        # unpack with meaningful names
print(f"Born on: {day}/{month}/{year}")

chennai_coordinates = (13.0827, 80.2707)    # latitude, longitude
latitude, longitude = chennai_coordinates
print(f"Chennai: lat={latitude}, lon={longitude}")

print()

# ─── Naming conventions for tuples ──────────────────────────────
print("=== Naming Guidelines for Tuples ===")
guidelines = {
    "Describe what the tuple represents" : "student_record, rgb_colour, gps_point",
    "Name unpacked variables clearly"    : "lat, lon = coords  (not a, b = coords)",
    "Use _ for ignored values"           : "name, _, city = record  (_ = ignored age)",
    "Function returns: name the pair"    : "low, high = get_range(data)",
    "Singular for one record"            : "student = ('Aarav', 13)  not students",
}
for rule, example in guidelines.items():
    print(f"  {rule:<40} → {example}")

print()

# ─── Practice: rename these ─────────────────────────────────────
print("=== Practice ===")

# Poor:
t1 = (255, 128, 0)
print("t1[0]:", t1[0])   # What is index 0?

# Better:
orange_rgb    = (255, 128, 0)
red, green, blue = orange_rgb
print(f"Orange → R={red}, G={green}, B={blue}")

# Poor:
x = ("Aarav", 13, "Chennai")
print(x[2])   # What is index 2?

# Better:
aarav_profile   = ("Aarav", 13, "Chennai")
name, age, city = aarav_profile
print(f"{name} lives in {city}")

# Think:
# 1. If a tuple has 5 items, how do you unpack only the 1st and last, ignoring the rest?
# 2. Why does unpacking with meaningful names make code easier to maintain?

# Create and Access a Dictionary
# Three ways to create a dictionary — each suits a different situation.
# Access values with [ ] (direct, risky) or .get() (safe, recommended when key might be missing).
# KEY RULE: use .get() whenever the key might not exist — it never crashes.

# Way 1: create with {} curly braces — the most common and readable way
fruit_prices = {
    "mango":   120,
    "banana":   40,
    "apple":    80,
    "grapes":   90,
}
print("Fruit prices:", fruit_prices)

# Way 2: create with dict() — useful when keys are valid Python identifiers (no spaces)
colours = dict(red="#FF0000", green="#00FF00", blue="#0000FF")
print("Colours:", colours)

# Way 3: start with an empty dict, then add items one by one
# Useful when you build the dictionary from user input or a loop
marks = {}
marks["Maths"]    = 85
marks["Science"]  = 90
marks["English"]  = 78
print("Marks:", marks)

print()

# Accessing values with [ ] — works when the key exists, crashes if it doesn't
# If the key is missing, Python raises a KeyError and the program stops
print(fruit_prices["mango"])     # 120
print(fruit_prices["apple"])     # 80

# Accessing values with .get() — SAFE, never crashes
# Returns None if key is missing, or a custom default you provide
print(fruit_prices.get("banana"))       # 40    (key exists → gives value)
print(fruit_prices.get("papaya"))       # None  (key missing → no crash!)
print(fruit_prices.get("papaya", 0))    # 0     (key missing → returns custom default)

print()

# Checking if a key exists before accessing — use the 'in' keyword
print("mango" in fruit_prices)      # True
print("papaya" in fruit_prices)     # False
print("papaya" not in fruit_prices) # True

print()

# len() gives the number of key-value pairs in the dictionary
print("Total fruits:", len(fruit_prices))

print()

# Nested access: a dictionary inside another dictionary
# student["marks"] gives the inner dict → ["Maths"] gives the mark value
student = {
    "name":  "Aarav",
    "marks": {"Maths": 85, "Science": 90}
}
print("Maths marks:", student["marks"]["Maths"])   # 85

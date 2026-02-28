# Program Code: DC-KN-02
# Title: Create and Access a Dictionary
# Cognitive Skill: Knowledge
# Topic: Dictionaries in Python

# --- Way 1: Create with {} (most common) ---
fruit_prices = {
    "mango":   120,
    "banana":   40,
    "apple":    80,
    "grapes":   90,
}
print("Fruit prices:", fruit_prices)

# --- Way 2: Create with dict() ---
colours = dict(red="#FF0000", green="#00FF00", blue="#0000FF")
print("Colours:", colours)

# --- Way 3: Start empty, add items ---
marks = {}
marks["Maths"]    = 85
marks["Science"]  = 90
marks["English"]  = 78
print("Marks:", marks)

print()

# --- Accessing values: using [ ] ---
print(fruit_prices["mango"])     # 120
print(fruit_prices["apple"])     # 80

# --- Accessing values: using .get() ---
# .get() is SAFER — returns None instead of error if key is missing
print(fruit_prices.get("banana"))       # 40
print(fruit_prices.get("papaya"))       # None (no error!)
print(fruit_prices.get("papaya", 0))    # 0 (custom default)

print()

# --- Checking if a key EXISTS ---
print("mango" in fruit_prices)     # True
print("papaya" in fruit_prices)    # False
print("papaya" not in fruit_prices) # True

print()

# --- Number of items in a dictionary ---
print("Total fruits:", len(fruit_prices))

print()

# --- Nested access: dictionary inside a dictionary ---
student = {
    "name":  "Aarav",
    "marks": {"Maths": 85, "Science": 90}
}
print("Maths marks:", student["marks"]["Maths"])

# Think:
# 1. What is the difference between dict["key"] and dict.get("key")?
# 2. What happens if you do fruit_prices["papaya"] (without .get())?

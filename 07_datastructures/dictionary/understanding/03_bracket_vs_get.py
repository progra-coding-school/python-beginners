# Program Code: DC-UN-03
# Title: Bracket vs .get() — Safe vs Risky Access
# Cognitive Skill: Understanding
# Topic: Dictionaries in Python

# --- The RISKY way: square brackets [ ] ---
print("=== Using [ ] — direct access ===")

menu = {"idli": 15, "dosa": 30, "chai": 10}

print(menu["idli"])     # 15 — works fine
print(menu["dosa"])     # 30 — works fine

# What if the key doesn't exist?
try:
    print(menu["pizza"])    # KeyError — CRASH!
except KeyError as e:
    print(f"KeyError: {e} — item not in menu!")

print()

# --- The SAFE way: .get() ---
print("=== Using .get() — safe access ===")

print(menu.get("chai"))         # 10 — found it
print(menu.get("pizza"))        # None — key missing, no crash
print(menu.get("pizza", 0))     # 0   — custom default, no crash

print()

# --- When to use which ---
print("=== When to use [ ] vs .get() ===")

student = {"name": "Aarav", "grade": 7, "city": "Chennai"}

# Use [ ] when you are CERTAIN the key exists
name = student["name"]
print("Name (certain it exists):", name)

# Use .get() when the key MIGHT be missing
email = student.get("email", "No email on file")
print("Email (may be missing):", email)

print()

# --- Real-world example: shop price lookup ---
print("=== Shop price lookup ===")

prices = {"mango": 120, "banana": 40, "apple": 80}

def get_price(item):
    price = prices.get(item)
    if price is None:
        return f"Sorry, '{item}' is not available."
    return f"{item}: Rs.{price}"

print(get_price("mango"))       # mango: Rs.120
print(get_price("papaya"))      # Sorry, 'papaya' is not available.
print(get_price("banana"))      # banana: Rs.40

print()

# --- Chaining .get() for nested dicts safely ---
print("=== Safe nested access ===")

profile = {
    "name": "Diya",
    "address": {"city": "Chennai", "pin": 600001}
}

# Safe: use .get() at each level
city = profile.get("address", {}).get("city", "Unknown")
print("City:", city)    # Chennai

# Key doesn't exist — returns default at each step
phone = profile.get("contact", {}).get("phone", "Not provided")
print("Phone:", phone)  # Not provided

# Think:
# 1. When would you prefer [ ] over .get()? Give one real example.
# 2. What does .get("key", default) return when the key IS found?

# Bracket vs .get() — Safe vs Risky Access
# dict["key"] — direct access. Crashes with KeyError if the key doesn't exist.
# dict.get("key") — safe access. Returns None (or a custom default) if key is missing.
# RULE: use .get() whenever the key MIGHT not be there — e.g., user input, optional fields.

# The risky way: square brackets []
# Works perfectly when the key exists, but crashes hard when it doesn't
print("Using [ ] — direct access:")
menu = {"idli": 15, "dosa": 30, "chai": 10}
print(menu["idli"])     # 15 — key exists, works fine
print(menu["dosa"])     # 30 — key exists, works fine

# If the key doesn't exist → KeyError crash!
try:
    print(menu["pizza"])    # KeyError — pizza is not in the menu!
except KeyError as e:
    print("KeyError:", e, "— item not in menu!")

print()

# The safe way: .get()
# Returns None when key is missing — no crash, program keeps running
print("Using .get() — safe access:")
print(menu.get("chai"))         # 10   — found it
print(menu.get("pizza"))        # None — key missing, no crash
print(menu.get("pizza", 0))     # 0    — custom default returned instead of None

print()

# When to use which:
print("When to use [ ] vs .get():")
student = {"name": "Aarav", "grade": 7, "city": "Chennai"}

# Use [ ] when you are CERTAIN the key exists (e.g., required fields in your own data)
name = student["name"]
print("Name (certain it exists):", name)

# Use .get() when the key MIGHT be missing (e.g., optional fields, external data)
email = student.get("email", "No email on file")
print("Email (may be missing):", email)

print()

# Real-world example: shop price lookup
# .get() lets us handle "item not found" gracefully without crashing
print("Shop price lookup:")
prices = {"mango": 120, "banana": 40, "apple": 80}

def get_price(item):
    price = prices.get(item)          # returns None if not found
    if price is None:
        return "Sorry, '" + item + "' is not available."
    return item + ": Rs." + str(price)

print(get_price("mango"))       # mango: Rs.120
print(get_price("papaya"))      # Sorry, 'papaya' is not available.
print(get_price("banana"))      # banana: Rs.40

print()

# Chaining .get() for nested dictionaries — safe at every level
# profile.get("address", {}) → if "address" missing, use {} so the next .get() doesn't crash
print("Safe nested access:")
profile = {
    "name":    "Diya",
    "address": {"city": "Chennai", "pin": 600001}
}

city  = profile.get("address", {}).get("city", "Unknown")     # safe two-level access
phone = profile.get("contact", {}).get("phone", "Not provided")  # "contact" doesn't exist

print("City:", city)    # Chennai
print("Phone:", phone)  # Not provided

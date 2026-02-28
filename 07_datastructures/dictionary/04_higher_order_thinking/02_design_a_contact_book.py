# Program Code: DC-HOT-02
# Title: Design a Contact Book App
# Cognitive Skill: Higher Order Thinking
# Topic: Dictionaries in Python

# Design challenge:
# Build a simple contact book with a menu.
# Each contact stores: name, phone, city.
# The user can: Add / View / Search / Delete a contact / Quit.

# --- Data store ---
contacts = {
    "Amma":  {"phone": "9988776655", "city": "Chennai"},
    "Aarav": {"phone": "9876543210", "city": "Madurai"},
}

# --- Helper functions ---

def add_contact(name, phone, city):
    contacts[name] = {"phone": phone, "city": city}
    print(f"  ✓ Contact '{name}' added.")

def view_all():
    if not contacts:
        print("  Contact book is empty.")
        return
    print(f"  {'Name':<12} {'Phone':<15} {'City'}")
    print(f"  {'─'*12} {'─'*15} {'─'*10}")
    for name, info in contacts.items():
        print(f"  {name:<12} {info['phone']:<15} {info['city']}")

def search_contact(name):
    info = contacts.get(name)
    if info:
        print(f"  Found: {name} | {info['phone']} | {info['city']}")
    else:
        print(f"  '{name}' not found in contact book.")

def delete_contact(name):
    removed = contacts.pop(name, None)
    if removed:
        print(f"  ✓ '{name}' deleted.")
    else:
        print(f"  '{name}' not found.")

# --- Demo: simulating menu choices (no input() so it runs without user) ---

print("=== Contact Book Demo ===")
print()

print("--- View all contacts ---")
view_all()
print()

print("--- Add a new contact ---")
add_contact("Diya", "9123456780", "Coimbatore")
view_all()
print()

print("--- Search for Aarav ---")
search_contact("Aarav")
print()

print("--- Search for someone not in the book ---")
search_contact("Riya")
print()

print("--- Delete Aarav ---")
delete_contact("Aarav")
view_all()
print()

print("--- Try deleting Aarav again ---")
delete_contact("Aarav")

# --- Extension idea ---
print()
print("=== Extension: How would you add a 'favourite' flag? ===")
contacts["Amma"]["favourite"] = True
print("Amma's data:", contacts["Amma"])

# Think:
# 1. How would you save these contacts to a file so they survive after the program ends?
# 2. What happens if two people share the same name? How would you fix this design?

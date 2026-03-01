# Design a Contact Book App
# One dictionary (contacts) stores all contact information.
# Each contact is a NESTED DICTIONARY: name → {phone, city}
# KEY DESIGN DECISIONS:
#   Use .get() for search — returns None if not found (no crash)
#   Use .pop() for delete — removes AND returns, so we know what was deleted
#   Use [name] = {...} for add — simple assignment adds or overwrites
# Each function does ONE job — add, view, search, or delete.

# The data store: contact name → their details (nested dict)
contacts = {
    "Amma":  {"phone": "9988776655", "city": "Chennai"},
    "Aarav": {"phone": "9876543210", "city": "Madurai"},
}

def add_contact(name, phone, city):
    contacts[name] = {"phone": phone, "city": city}   # assignment adds new key or overwrites
    print("  Contact '" + name + "' added.")

def view_all():
    if not contacts:       # empty dict is falsy — same as len(contacts) == 0
        print("  Contact book is empty.")
        return
    print("  " + "Name".ljust(12) + "Phone".ljust(15) + "City")
    print("  " + "-" * 37)
    for name, info in contacts.items():
        print("  " + name.ljust(12) + info["phone"].ljust(15) + info["city"])

def search_contact(name):
    # .get() returns None if name not in contacts — no KeyError
    info = contacts.get(name)
    if info:
        print("  Found:", name, "|", info["phone"], "|", info["city"])
    else:
        print("  '" + name + "' not found in contact book.")

def delete_contact(name):
    # .pop(name, None) removes if found, returns None if not found (no crash)
    removed = contacts.pop(name, None)
    if removed:
        print("  '" + name + "' deleted.")
    else:
        print("  '" + name + "' not found.")

# Demo: run through typical contact book operations
print("Contact Book Demo")
print()

print("View all contacts:")
view_all()
print()

print("Add a new contact:")
add_contact("Diya", "9123456780", "Coimbatore")
view_all()
print()

print("Search for Aarav:")
search_contact("Aarav")
print()

print("Search for someone not in the book:")
search_contact("Riya")
print()

print("Delete Aarav:")
delete_contact("Aarav")
view_all()
print()

print("Try deleting Aarav again:")
delete_contact("Aarav")

# Extension: add a new field to an existing contact — dicts are mutable, easy to extend!
print()
print("Extension — adding a favourite flag:")
contacts["Amma"]["favourite"] = True   # add a new key to a nested dict at any time
print("Amma's data:", contacts["Amma"])

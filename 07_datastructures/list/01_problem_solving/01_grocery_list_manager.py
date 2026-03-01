# Program Code: LIST-PS-01
# Title: Grocery List Manager
# Cognitive Skill: Problem Solving (Applying list operations)
# Topic: Lists in Python

# A simple grocery list manager using a Python list
grocery = []

print("=== Grocery List Manager ===")
print()

# Step 1: Add items
print("ADD ITEMS")
print("Type each grocery item and press Enter.")
print("Type 'done' when finished.")
print()
while True:
    item = input("Item: ").strip()
    if item.lower() == "done":
        break
    if item:
        grocery.append(item)
        print("  Added. List:", grocery)
print()

# Step 2: Show the list
print("YOUR GROCERY LIST:")
for i, item in enumerate(grocery, start=1):
    print("  " + str(i) + ". " + item)
print("Total items:", len(grocery))
print()

# Step 3: Remove an item
if grocery:
    remove_item = input("Which item to remove? ").strip()
    if remove_item in grocery:
        grocery.remove(remove_item)
        print("Removed. Updated list:", grocery)
    else:
        print(remove_item + " not found in list.")
    print()

# Step 4: Insert an urgent item at the top
if grocery:
    urgent = input("Any urgent item to add at the top? ").strip()
    if urgent:
        grocery.insert(0, urgent)
        print("Inserted at top:", grocery)
    print()

# Step 5: Sort the list
grocery.sort()
print("Sorted list:")
for i, item in enumerate(grocery, start=1):
    print("  " + str(i) + ". " + item)
print()
print("Done! Final grocery list has", len(grocery), "items.")

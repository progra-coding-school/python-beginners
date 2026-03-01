# Grocery List Manager
# A real-world app powered by a single Python list.
# We use grocery = [] and apply: append, remove, insert, sort.
# Each step shows a different list operation solving a real need.

grocery = []

# Step 1: Add items — keep appending until the user types 'done'
# append() grows the list one item at a time
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

# Step 2: Show the list — enumerate gives us number + item together
# start=1 makes the numbering 1, 2, 3... instead of 0, 1, 2...
print("YOUR GROCERY LIST:")
for i, item in enumerate(grocery, start=1):
    print("  " + str(i) + ". " + item)
print("Total items:", len(grocery))
print()

# Step 3: Remove an item by name
# We check with 'in' first — remove() raises ValueError if item not found
if grocery:
    remove_item = input("Which item to remove? ").strip()
    if remove_item in grocery:
        grocery.remove(remove_item)        # removes first match by value
        print("Removed. Updated list:", grocery)
    else:
        print(remove_item + " not found in list.")
    print()

# Step 4: Insert an urgent item at the top
# insert(0, item) places the item at index 0 — everything else shifts right
if grocery:
    urgent = input("Any urgent item to add at the top? ").strip()
    if urgent:
        grocery.insert(0, urgent)          # index 0 = beginning of list
        print("Inserted at top:", grocery)
    print()

# Step 5: Sort the list alphabetically
# sort() rearranges in place — the list itself is reordered
grocery.sort()
print("Sorted list:")
for i, item in enumerate(grocery, start=1):
    print("  " + str(i) + ". " + item)
print()
print("Done! Final grocery list has", len(grocery), "items.")

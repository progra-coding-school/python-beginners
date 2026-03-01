# Removing and Updating Items
# Four ways to remove or change items in a list.
# Choose based on what you know:
#   remove(value) → you know the VALUE you want to delete
#   pop(index)    → you know the INDEX (also gives back the removed item)
#   list[i] = x  → you want to REPLACE an item at a position
#   clear()       → you want to EMPTY the entire list

# fruits has two "banana" entries — remove() will only delete the FIRST one
fruits = ["apple", "banana", "mango", "orange", "banana"]
print("Start:", fruits)

# remove() — removes the FIRST matching item by value
# If the value is not found, it raises a ValueError!
fruits.remove("banana")
print("After remove('banana'):", fruits)    # removes first 'banana' only

# pop(index) — removes the item at a specific index and RETURNS it
# Useful when you want to know what you removed
removed = fruits.pop(1)                     # remove item at index 1
print("After pop(1):", fruits)
print("Removed item:", removed)             # the item that was at index 1

# pop() with no argument — removes and returns the LAST item
# The default index for pop() is -1 (last item)
last = fruits.pop()
print("After pop():", fruits)
print("Removed last:", last)

# Updating an item — use index assignment, just like a variable
# lists[i] = new_value replaces whatever was at index i
marks = [80, 75, 90]
print("Before update:", marks)
marks[1] = 85                               # replace index 1 (75 → 85)
print("After marks[1] = 85:", marks)

# clear() — removes ALL items and leaves an empty list
# The list itself still exists — it is just empty
shopping = ["milk", "eggs", "bread"]
print("Before clear:", shopping)
shopping.clear()
print("After clear:", shopping)             # []
print("Length after clear:", len(shopping)) # 0

print()
print("remove(value) — by VALUE (removes first match)")
print("pop(index)    — by INDEX (returns removed item)")
print("pop()         — removes the LAST item")
print("list[i] = val — update/replace item at index i")
print("clear()       — empties the entire list")

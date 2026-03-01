# Program Code: LIST-KN-03
# Title: Removing and Updating Items
# Cognitive Skill: Knowledge (Syntax and usage)
# Topic: Lists in Python

fruits = ["apple", "banana", "mango", "orange", "banana"]
print("Start:", fruits)

# remove() — removes the FIRST matching item by value
fruits.remove("banana")
print("After remove('banana'):", fruits)    # removes first 'banana'

# pop() — removes by index and RETURNS the item
removed = fruits.pop(1)                     # remove item at index 1
print("After pop(1):", fruits)
print("Removed item:", removed)

# pop() with no argument — removes the LAST item
last = fruits.pop()
print("After pop():", fruits)
print("Removed last:", last)

# Updating an item — just use assignment
marks = [80, 75, 90]
print("Before update:", marks)
marks[1] = 85                               # update index 1
print("After marks[1] = 85:", marks)

# clear() — removes ALL items
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

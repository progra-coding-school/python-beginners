# Searching, Sorting, and Slicing
# Three powerful operations that make lists very useful:
#   Searching — check if something exists, find its position, or count it
#   Sorting   — rearrange items in ascending or descending order
#   Slicing   — extract a portion of the list using [start:stop:step]

players = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
scores  = [88, 45, 92, 67, 78]

# --- Searching ---
# Use 'in' to check existence — returns True or False
# Use index() to find the position of a value — returns its index number
# Use count() to count how many times a value appears
print("Searching")
print("'Kabir' in players:", "Kabir" in players)          # True
print("'Mani' in players:", "Mani" in players)            # False
print("Index of 'Diya':", players.index("Diya"))          # 1 — Diya is at index 1
print("Count of 45 in scores:", scores.count(45))         # 1 — appears once

print()

# --- Sorting ---
# sort() rearranges the list IN PLACE — the original list changes
# sorted() returns a NEW sorted list — the original stays the same
print("Sorting")
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()                                             # smallest to largest (ascending)
print("Sorted ascending:", numbers)

numbers.sort(reverse=True)                                 # largest to smallest (descending)
print("Sorted descending:", numbers)

# sorted() — does NOT change the original, gives back a new list
fruits = ["mango", "apple", "banana"]
sorted_fruits = sorted(fruits)                             # returns a new sorted list
print("sorted() result:", sorted_fruits)
print("Original unchanged:", fruits)                       # fruits is still in original order

print()

# --- Slicing ---
# Slicing syntax: list[start:stop:step]
#   start → index to begin (included)
#   stop  → index to end   (NOT included)
#   step  → how many to skip (default is 1)
print("Slicing")
nums = [10, 20, 30, 40, 50, 60, 70]

print("nums[1:4]  :", nums[1:4])     # index 1, 2, 3 → [20, 30, 40]  (stops before 4)
print("nums[:3]   :", nums[:3])      # from start up to index 3 → [10, 20, 30]
print("nums[4:]   :", nums[4:])      # from index 4 to end → [50, 60, 70]
print("nums[-3:]  :", nums[-3:])     # last 3 items → [50, 60, 70]
print("nums[::2]  :", nums[::2])     # every 2nd item → [10, 30, 50, 70]
print("nums[::-1] :", nums[::-1])    # step -1 means reverse the whole list

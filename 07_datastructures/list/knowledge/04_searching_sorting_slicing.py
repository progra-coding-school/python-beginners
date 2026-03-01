# Program Code: LIST-KN-04
# Title: Searching, Sorting, and Slicing
# Cognitive Skill: Knowledge (Syntax and usage)
# Topic: Lists in Python

players = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
scores  = [88, 45, 92, 67, 78]

# --- Searching ---
print("Searching")
print("'Kabir' in players:", "Kabir" in players)          # True
print("'Mani' in players:", "Mani" in players)            # False
print("Index of 'Diya':", players.index("Diya"))          # 1
print("Count of 45 in scores:", scores.count(45))         # 1

print()

# --- Sorting ---
print("Sorting")
numbers = [5, 2, 8, 1, 9, 3]
numbers.sort()                                             # ascending (default)
print("Sorted ascending:", numbers)

numbers.sort(reverse=True)                                 # descending
print("Sorted descending:", numbers)

# sorted() — returns a new sorted list, original unchanged
fruits = ["mango", "apple", "banana"]
sorted_fruits = sorted(fruits)
print("sorted() result:", sorted_fruits)
print("Original unchanged:", fruits)

print()

# --- Slicing ---
print("Slicing")
nums = [10, 20, 30, 40, 50, 60, 70]

print("nums[1:4]  :", nums[1:4])     # index 1 to 3 → [20, 30, 40]
print("nums[:3]   :", nums[:3])      # first 3 → [10, 20, 30]
print("nums[4:]   :", nums[4:])      # from index 4 → [50, 60, 70]
print("nums[-3:]  :", nums[-3:])     # last 3 → [50, 60, 70]
print("nums[::2]  :", nums[::2])     # every other → [10, 30, 50, 70]
print("nums[::-1] :", nums[::-1])    # reversed → [70, 60, 50, 40, 30, 20, 10]

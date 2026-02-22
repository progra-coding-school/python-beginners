# Program Code: LIST-KN-01
# Title: What is a List? — Many Things in One Box!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Aarav is captain of his school cricket team. He needs to
# store the names of 5 players. He tried making 5 separate
# variables — player1, player2, player3 ... it got very messy!
# There must be a better way to hold MANY things at once.
# That's where a LIST comes in!
# ============================================================

# ============================================================
# WHAT IS A LIST?
# A list is a single variable that can hold MANY items.
# Think of it like a tiffin box with multiple compartments —
# one box, many items inside!
# In Python, a list is written with square brackets [ ]
# and items are separated by commas.
# ============================================================

print("=" * 55)
print("    WHAT IS A LIST? — MANY THINGS IN ONE BOX!")
print("=" * 55)

# -------------------------------------------------------
# THE OLD WAY — separate variables (messy!) ❌
# -------------------------------------------------------
print("\n--- The OLD Way (messy!) ---")

player1 = "Aarav"
player2 = "Kabir"
player3 = "Rohan"
player4 = "Meera"
player5 = "Diya"

print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
print(f"Player 3: {player3}")
print(f"Player 4: {player4}")
print(f"Player 5: {player5}")
print("(5 variables just for 5 names! Imagine 50 players...)")

# -------------------------------------------------------
# THE NEW WAY — using a LIST ✅
# -------------------------------------------------------
print("\n--- The NEW Way (clean with a List!) ---")

cricket_team = ["Aarav", "Kabir", "Rohan", "Meera", "Diya"]
print(f"Cricket team : {cricket_team}")
print("(All 5 names in ONE variable! Much better!)")

# ============================================================
# CREATING DIFFERENT KINDS OF LISTS
# A list can hold strings, numbers, or even a mix!
# ============================================================

print("\n" + "=" * 55)
print("  CREATING DIFFERENT KINDS OF LISTS")
print("=" * 55)

# -------------------------------------------------------
# List of strings (names)
# -------------------------------------------------------
print("\n--- List of Strings ---")
student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
print(f"Student names : {student_names}")

# -------------------------------------------------------
# List of numbers (marks)
# -------------------------------------------------------
print("\n--- List of Numbers ---")
exam_marks = [88, 95, 72, 100, 65]
print(f"Exam marks    : {exam_marks}")

# -------------------------------------------------------
# List of fruits (strings)
# -------------------------------------------------------
print("\n--- List of Fruits ---")
favourite_fruits = ["Mango", "Banana", "Guava", "Pomegranate"]
print(f"Favourite fruits : {favourite_fruits}")

# -------------------------------------------------------
# An empty list — we can add items later!
# -------------------------------------------------------
print("\n--- Empty List (fill it later!) ---")
shopping_list = []
print(f"Shopping list (empty) : {shopping_list}")

# ============================================================
# ACCESSING ITEMS BY INDEX
# Every item in a list has an ADDRESS called an INDEX.
# Index always starts at 0 (not 1!).
#
# ASCII DIAGRAM of cricket_team:
#
#   cricket_team = ["Aarav", "Kabir", "Rohan", "Meera", "Diya"]
#
#   +----------+----------+----------+----------+----------+
#   |  "Aarav" |  "Kabir" |  "Rohan" |  "Meera" |  "Diya"  |
#   +----------+----------+----------+----------+----------+
#   |  index 0 |  index 1 |  index 2 |  index 3 |  index 4 |
#   +----------+----------+----------+----------+----------+
#   | index -5 | index -4 | index -3 | index -2 | index -1 |
#   +----------+----------+----------+----------+----------+
#
# Positive index → count from the LEFT  (starts at 0)
# Negative index → count from the RIGHT (starts at -1)
# ============================================================

print("\n" + "=" * 55)
print("  ACCESSING ITEMS BY INDEX")
print("=" * 55)

cricket_team = ["Aarav", "Kabir", "Rohan", "Meera", "Diya"]
print(f"\nFull team : {cricket_team}")

# -------------------------------------------------------
# Positive indexing — count from the left
# -------------------------------------------------------
print("\n--- Positive Index (left to right, starts at 0) ---")
print(f"cricket_team[0]  → {cricket_team[0]}   (1st player)")
print(f"cricket_team[1]  → {cricket_team[1]}   (2nd player)")
print(f"cricket_team[2]  → {cricket_team[2]}   (3rd player)")
print(f"cricket_team[3]  → {cricket_team[3]}   (4th player)")
print(f"cricket_team[4]  → {cricket_team[4]}    (5th player)")

# -------------------------------------------------------
# Negative indexing — count from the right
# -------------------------------------------------------
print("\n--- Negative Index (right to left, starts at -1) ---")
print(f"cricket_team[-1] → {cricket_team[-1]}    (LAST player)")
print(f"cricket_team[-2] → {cricket_team[-2]}   (2nd from last)")
print(f"cricket_team[-3] → {cricket_team[-3]}   (3rd from last)")
print(f"cricket_team[-4] → {cricket_team[-4]}   (4th from last)")
print(f"cricket_team[-5] → {cricket_team[-5]}   (5th from last = first!)")

# -------------------------------------------------------
# Real-world use: Getting first and last player
# -------------------------------------------------------
print("\n--- Real Use: First and Last Player ---")
first_player = cricket_team[0]
last_player  = cricket_team[-1]
print(f"Captain (first) : {first_player}")
print(f"Last to bat     : {last_player}")

# ============================================================
# len() — COUNTING ITEMS IN A LIST
# len() tells you how many items are in the list.
# ============================================================

print("\n" + "=" * 55)
print("  len() — HOW MANY ITEMS ARE IN THE LIST?")
print("=" * 55)

print(f"\nCricket team : {cricket_team}")
team_size = len(cricket_team)
print(f"len(cricket_team) = {team_size}")
print(f"There are {team_size} players in the team.")

# More examples with len()
print("\n--- More len() Examples ---")
print(f"len(student_names)   = {len(student_names)}  → {student_names}")
print(f"len(exam_marks)      = {len(exam_marks)}  → {exam_marks}")
print(f"len(shopping_list)   = {len(shopping_list)}  → {shopping_list}  (empty!)")

# -------------------------------------------------------
# KEY INSIGHT: Index of last item = len(list) - 1
# -------------------------------------------------------
print("\n--- Key Insight: Last Index = len() - 1 ---")
last_index = len(cricket_team) - 1
print(f"len(cricket_team) = {len(cricket_team)}")
print(f"Last index        = {len(cricket_team)} - 1 = {last_index}")
print(f"cricket_team[{last_index}]   = {cricket_team[last_index]}")
print("(Same as cricket_team[-1]!)")

# ============================================================
# QUICK REFERENCE SUMMARY
# ============================================================
# list_name = [item1, item2, item3]  → Create a list
# list_name[0]                       → First item (index 0)
# list_name[-1]                      → Last item (negative index)
# len(list_name)                     → Number of items in list
# list_name[len(list_name) - 1]      → Last item (using len)
# []                                 → Empty list
# ============================================================

print("\n" + "=" * 55)
print("  QUICK REFERENCE SUMMARY")
print("=" * 55)
print("  my_list = [a, b, c]  → Create a list")
print("  my_list[0]           → First item  (index starts at 0)")
print("  my_list[-1]          → Last item   (negative index)")
print("  len(my_list)         → Count of items in list")
print("  []                   → Create an empty list")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. If a list has 8 items, what is the index of the LAST item?
#    (Hint: index starts at 0, so count from there!)
# 2. What does cricket_team[-2] give you?
#    Try it mentally before running the code.
# 3. A list called colours = ["Red","Blue","Green","Yellow"]
#    What is colours[2]? What is colours[-1]?
# 4. Why is using a list better than making 10 separate variables?
#    Write your answer as a comment!
# ============================================================

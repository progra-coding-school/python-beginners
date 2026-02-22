# Program Code: LIST-KN-04
# Title: Searching, Sorting & Slicing — Find, Order, and Pick!
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Coach Ramesh is managing the district cricket squad.
# He has a list of 10 players with their scores.
# He needs to:
#   - SEARCH: Is a certain player in the squad? Where in the list?
#   - SORT: Arrange players by score (lowest to highest, and back)
#   - SLICE: Pick only the TOP 3, or LAST 4, or EVERY ALTERNATE player
# Python makes all 3 super simple — let's learn them!
# ============================================================

# ============================================================
# THREE POWERFUL LIST TOOLS:
#
#   PART 1 — SEARCHING  : 'in', index(), count()
#   PART 2 — SORTING    : sort(), sort(reverse=True)
#   PART 3 — SLICING    : list[start:end], list[:n], list[n:]
# ============================================================

print("=" * 55)
print("   SEARCHING, SORTING & SLICING A LIST")
print("=" * 55)

# -------------------------------------------------------
# Coach Ramesh's squad list with trial scores
# -------------------------------------------------------
print("\n--- Coach Ramesh's Cricket Squad ---")

squad_players = ["Aarav", "Kabir", "Rohan", "Diya", "Meera",
                 "Arjun", "Priya", "Ravi", "Anil", "Neha"]

trial_scores  = [78, 92, 55, 88, 72, 95, 61, 84, 70, 90]

print(f"Players  : {squad_players}")
print(f"Scores   : {trial_scores}")
print(f"Total players: {len(squad_players)}")

# ============================================================
# PART 1: SEARCHING — Find items in a list
# ============================================================

print("\n" + "=" * 55)
print("  PART 1: SEARCHING — Find Items in a List")
print("=" * 55)

# -------------------------------------------------------
# SEARCH TOOL 1: 'in' keyword — Is the item present? (True/False)
# Returns True if found, False if not found
# -------------------------------------------------------
print("\n--- TOOL 1: 'in' — Is the item in the list? ---")

print(f"Squad players : {squad_players}")
print()
print(f"Is 'Rohan'  in the squad? → {'Rohan' in squad_players}")
print(f"Is 'Diya'   in the squad? → {'Diya' in squad_players}")
print(f"Is 'Rahul'  in the squad? → {'Rahul' in squad_players}")
print()
print(f"Is 'Rahul' NOT in squad?  → {'Rahul' not in squad_players}")

# Real-world use: Check before adding
print("\n--- Real Use: Check before acting ---")
player_to_check = "Priya"
if player_to_check in squad_players:
    print(f"  '{player_to_check}' is already in the squad. No need to add!")
else:
    print(f"  '{player_to_check}' is NOT in the squad. Adding her now.")

# -------------------------------------------------------
# SEARCH TOOL 2: index() — WHERE is the item? (gives index)
# Returns the INDEX (position) of the first match
# Gives an ERROR if the item is not found
# -------------------------------------------------------
print("\n--- TOOL 2: index() — WHERE is the item? ---")

print(f"Squad players : {squad_players}")
print()

arjun_position  = squad_players.index("Arjun")
meera_position  = squad_players.index("Meera")
aarav_position  = squad_players.index("Aarav")

print(f"squad_players.index('Arjun') → {arjun_position}  (position {arjun_position})")
print(f"squad_players.index('Meera') → {meera_position}  (position {meera_position})")
print(f"squad_players.index('Aarav') → {aarav_position}  (position {aarav_position})")

# Real-world use: Find score of a specific player
print("\n--- Real Use: Find a player's score using index ---")
player_name    = "Rohan"
player_index   = squad_players.index(player_name)
player_score   = trial_scores[player_index]
print(f"  {player_name} is at index {player_index}")
print(f"  {player_name}'s trial score = {player_score}")

# -------------------------------------------------------
# SEARCH TOOL 3: count() — HOW MANY TIMES does it appear?
# Returns the number of times a value appears in the list
# -------------------------------------------------------
print("\n--- TOOL 3: count() — How many times does it appear? ---")

# Example with a list that has repeated items
daily_fruits = ["Mango", "Banana", "Mango", "Apple", "Mango", "Banana"]
print(f"daily_fruits : {daily_fruits}")
print()
print(f"daily_fruits.count('Mango')  → {daily_fruits.count('Mango')}")
print(f"daily_fruits.count('Banana') → {daily_fruits.count('Banana')}")
print(f"daily_fruits.count('Apple')  → {daily_fruits.count('Apple')}")
print(f"daily_fruits.count('Guava')  → {daily_fruits.count('Guava')}   (not in list!)")

# Counting in cricket scores
print()
print(f"trial_scores         : {trial_scores}")
print(f"count(88) in scores  → {trial_scores.count(88)}")
print(f"count(100) in scores → {trial_scores.count(100)}  (no perfect score!)")

# ============================================================
# PART 2: SORTING — Arrange items in order
# ============================================================

print("\n" + "=" * 55)
print("  PART 2: SORTING — Arrange Items in Order")
print("=" * 55)

# -------------------------------------------------------
# SORT TOOL 1: sort() — Ascending order (smallest first)
# Numbers: 1, 2, 3 ...   Strings: A, B, C ...
# sort() modifies the list IN PLACE (changes the original!)
# -------------------------------------------------------
print("\n--- TOOL 1: sort() — Ascending (Lowest to Highest) ---")

scores_to_sort = [78, 92, 55, 88, 72, 95, 61, 84, 70, 90]
print(f"Before sort : {scores_to_sort}")

scores_to_sort.sort()                  # Sorts ascending (in place)

print(f"After  sort : {scores_to_sort}")
print("  sort() → numbers go from LOWEST to HIGHEST")

# -------------------------------------------------------
# SORT TOOL 2: sort(reverse=True) — Descending (highest first)
# -------------------------------------------------------
print("\n--- TOOL 2: sort(reverse=True) — Descending (Highest to Lowest) ---")

scores_to_sort.sort(reverse=True)      # Sorts descending (in place)

print(f"After reverse sort : {scores_to_sort}")
print("  sort(reverse=True) → numbers go from HIGHEST to LOWEST")

# Real-world use: Find top 3 performers
print("\n--- Real Use: Finding Top 3 Scores ---")
all_scores = [78, 92, 55, 88, 72, 95, 61, 84, 70, 90]
all_scores.sort(reverse=True)
print(f"All scores (sorted highest first) : {all_scores}")
print(f"Top 3 scores : {all_scores[0]}, {all_scores[1]}, {all_scores[2]}")

# -------------------------------------------------------
# SORT TOOL 3: Sorting STRINGS — Alphabetical order
# sort() on strings sorts A to Z (alphabetically)
# -------------------------------------------------------
print("\n--- TOOL 3: Sorting Strings — Alphabetical Order ---")

name_list = ["Rohan", "Aarav", "Meera", "Diya", "Kabir"]
print(f"Before sort : {name_list}")

name_list.sort()                       # Alphabetical A → Z

print(f"After  sort : {name_list}")
print("  sort() on strings → alphabetical order A to Z")

name_list.sort(reverse=True)           # Reverse alphabetical Z → A
print(f"Reverse sort: {name_list}")
print("  sort(reverse=True) → alphabetical order Z to A")

# ============================================================
# PART 3: SLICING — Pick a portion of a list
# list[start:end]  → from index 'start' up to (not including) 'end'
# Think of it like cutting a piece of a banana bread loaf!
# ============================================================

print("\n" + "=" * 55)
print("  PART 3: SLICING — Pick a Portion of the List")
print("=" * 55)

# -------------------------------------------------------
# Reset squad_players for slicing demos
# -------------------------------------------------------
squad_players = ["Aarav", "Kabir", "Rohan", "Diya", "Meera",
                 "Arjun", "Priya", "Ravi", "Anil", "Neha"]

print(f"\nFull squad : {squad_players}")
print(f"Indices    :  [0]     [1]     [2]    [3]    [4]")
print(f"             [5]     [6]     [7]    [8]    [9]")

# -------------------------------------------------------
# SLICE 1: list[start:end] — Items from start up to (not including) end
# -------------------------------------------------------
print("\n--- SLICE 1: list[start:end] — Specific range ---")

middle_players = squad_players[2:6]    # index 2, 3, 4, 5 (NOT 6)
print(f"squad_players[2:6] → {middle_players}")
print("  Takes items at index 2, 3, 4, 5 — stops BEFORE index 6")

# -------------------------------------------------------
# SLICE 2: list[:n] — First n items (start from beginning)
# -------------------------------------------------------
print("\n--- SLICE 2: list[:n] — First n items ---")

first_three = squad_players[:3]        # first 3 players (index 0, 1, 2)
print(f"squad_players[:3]  → {first_three}")
print("  Takes the FIRST 3 items (index 0 to 2)")

# Real-world use: Select top 3 for the playing XI
print(f"\n  Coach picks first 3 for the starting XI: {first_three}")

# -------------------------------------------------------
# SLICE 3: list[n:] — From index n to the END
# -------------------------------------------------------
print("\n--- SLICE 3: list[n:] — From index n to the END ---")

from_index_7 = squad_players[7:]       # from index 7 to the end
print(f"squad_players[7:]  → {from_index_7}")
print("  Takes items from index 7 to the END of the list")

# -------------------------------------------------------
# SLICE 4: list[-n:] — Last n items (using negative index)
# -------------------------------------------------------
print("\n--- SLICE 4: list[-n:] — Last n items ---")

last_three = squad_players[-3:]        # last 3 players
print(f"squad_players[-3:] → {last_three}")
print("  Takes the LAST 3 items using negative index")

# Real-world use: Reserve players are last 3
print(f"\n  Reserve players (last 3): {last_three}")

# -------------------------------------------------------
# SLICE 5: list[::2] — Every 2nd item (step slicing)
# list[start:end:step] — step tells how many to skip
# -------------------------------------------------------
print("\n--- SLICE 5: list[::2] — Every 2nd item (step) ---")

every_second = squad_players[::2]      # step=2, picks index 0,2,4,6,8
print(f"squad_players[::2] → {every_second}")
print("  Picks every 2nd item: index 0, 2, 4, 6, 8")

every_third = squad_players[::3]       # step=3, picks index 0,3,6,9
print(f"squad_players[::3] → {every_third}")
print("  Picks every 3rd item: index 0, 3, 6, 9")

# -------------------------------------------------------
# SLICING KEY RULE — Does NOT include the end index!
# -------------------------------------------------------
print("\n" + "-" * 40)
print("  SLICING RULE: list[start:end]")
print("  → Includes 'start', EXCLUDES 'end'")
print(f"  squad_players[1:4] → {squad_players[1:4]}")
print("  Takes index 1, 2, 3 — NOT index 4!")
print("-" * 40)

# ============================================================
# QUICK REFERENCE SUMMARY
# ============================================================
# SEARCHING:
#   'x' in list       → True/False (is x in the list?)
#   'x' not in list   → True/False (is x NOT in the list?)
#   list.index(x)     → index of first x (error if not found)
#   list.count(x)     → how many times x appears
#
# SORTING:
#   list.sort()              → ascending (in place, changes list)
#   list.sort(reverse=True)  → descending (in place)
#   Works for numbers (1,2,3) and strings (A,B,C)
#
# SLICING:
#   list[start:end]  → items from start up to (not including) end
#   list[:n]         → first n items
#   list[n:]         → from index n to end
#   list[-n:]        → last n items
#   list[::step]     → every step-th item
# ============================================================

print("\n" + "=" * 55)
print("  QUICK REFERENCE SUMMARY")
print("=" * 55)
print("  --- SEARCHING ---")
print("  x in list          → True if x is found")
print("  list.index(x)      → Index of first x")
print("  list.count(x)      → How many times x appears")
print("-" * 40)
print("  --- SORTING ---")
print("  list.sort()        → Ascending (A-Z, 1-2-3)")
print("  list.sort(         → Descending (Z-A, 9-8-7)")
print("    reverse=True)")
print("-" * 40)
print("  --- SLICING ---")
print("  list[s:e]          → From index s to e (excl. e)")
print("  list[:n]           → First n items")
print("  list[n:]           → From index n to end")
print("  list[-n:]          → Last n items")
print("  list[::step]       → Every step-th item")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. You have scores = [55, 90, 78, 62, 88, 45, 99].
#    What does scores.sort() give you?
#    What does scores.sort(reverse=True) give you after that?
# 2. Given players = ["Aarav","Diya","Kabir","Meera","Rohan"],
#    what does players[1:4] return?
#    What does players[-2:] return?
# 3. If a name appears 0 times in count(), what does that tell you?
#    Is that the same as getting an error from index()?
# 4. Coach wants EVERY OTHER player starting from the 2nd one.
#    What slice would you write? (Hint: use the step parameter!)
# ============================================================

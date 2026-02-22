# Program Code: LIST-KN-03
# Title: Removing & Updating Items — remove, pop, clear, update
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Meera's class teacher is managing the student attendance list.
# During the year:
#   - Some students transfer out (need to REMOVE them)
#   - Some names were typed wrongly (need to UPDATE them)
#   - At year end, the list is CLEARED for the new batch
# Python gives us easy tools to remove and update list items!
# ============================================================

# ============================================================
# PART 1: REMOVING ITEMS — 4 ways to remove
#   remove(value)  → Remove by VALUE (what it says)
#   pop(index)     → Remove by INDEX (where it is), returns item
#   pop()          → Remove the LAST item (no index needed)
#   clear()        → Remove EVERYTHING from the list
#
# PART 2: UPDATING ITEMS
#   list[index] = new_value → Replace an item at a position
# ============================================================

print("=" * 55)
print("   REMOVING & UPDATING ITEMS IN A LIST")
print("=" * 55)

# -------------------------------------------------------
# Teacher starts with the class list
# -------------------------------------------------------
print("\n--- Teacher's Starting Class List ---")
class_list = ["Aarav", "Diya", "Kabir", "Meera", "Rohan", "Priya", "Ravi"]
print(f"Class list : {class_list}")
print(f"Total students : {len(class_list)}")

# ============================================================
# PART 1: REMOVING ITEMS
# ============================================================

print("\n" + "=" * 55)
print("  PART 1: REMOVING ITEMS")
print("=" * 55)

# -------------------------------------------------------
# REMOVE METHOD 1: remove(value) — Remove by VALUE
# Use when: you know the NAME/VALUE of the item to remove
# Removes the FIRST occurrence if the value appears more than once
# Gives an ERROR if the value is not found
# -------------------------------------------------------
print("\n--- METHOD 1: remove(value) — Remove by Name/Value ---")

print(f"Before remove : {class_list}")
print("  Kabir has transferred to another school.")

class_list.remove("Kabir")             # Remove the item "Kabir"

print(f"After  remove : {class_list}")
print(f"  remove('Kabir') → 'Kabir' is gone! List has {len(class_list)} students now.")

# -------------------------------------------------------
# REMOVE METHOD 2: pop(index) — Remove by INDEX, returns item
# Use when: you know the POSITION of the item to remove
# pop() RETURNS the removed item — you can store it!
# -------------------------------------------------------
print("\n--- METHOD 2: pop(index) — Remove by Position ---")

print(f"Before pop    : {class_list}")
print(f"  Index 1 holds : '{class_list[1]}'")
print("  Diya is moving to Section B — remove her from this list.")

removed_student = class_list.pop(1)    # Remove item at index 1, save it

print(f"After  pop    : {class_list}")
print(f"  pop(1) removed → '{removed_student}'")
print(f"  The removed student was: {removed_student}")
print(f"  List now has {len(class_list)} students.")

# -------------------------------------------------------
# REMOVE METHOD 3: pop() — Remove the LAST item
# Use when: you want to remove from the end (no index needed)
# Very useful! Always removes the very last item.
# -------------------------------------------------------
print("\n--- METHOD 3: pop() — Remove the LAST Item ---")

print(f"Before pop()  : {class_list}")
print("  Ravi has left without telling the teacher. Remove last entry.")

last_removed = class_list.pop()        # No index → removes LAST item

print(f"After  pop()  : {class_list}")
print(f"  pop() removed the last item → '{last_removed}'")
print(f"  List now has {len(class_list)} students.")

# -------------------------------------------------------
# REMOVE METHOD 4: clear() — Remove ALL items
# Use when: you want to empty the entire list at once
# The list still exists — it just becomes empty []
# -------------------------------------------------------
print("\n--- METHOD 4: clear() — Remove EVERYTHING ---")

# First, let's show clear() on a copy so we keep class_list intact
temp_list = ["Batch A", "Batch B", "Batch C"]
print(f"Before clear  : {temp_list}")

temp_list.clear()                      # All items removed

print(f"After  clear  : {temp_list}")
print("  clear() → list is now empty, but the variable still exists!")
print(f"  Type of temp_list after clear : {type(temp_list)}")

# -------------------------------------------------------
# Recap: class_list after all removals
# -------------------------------------------------------
print("\n" + "-" * 40)
print("  Class List — After All Removals:")
print(f"  {class_list}")
print(f"  Students remaining: {len(class_list)}")
print("-" * 40)

# ============================================================
# PART 2: UPDATING ITEMS
# list[index] = new_value → Directly replace the item
# Use when: a value was wrong and needs to be corrected
# ============================================================

print("\n" + "=" * 55)
print("  PART 2: UPDATING ITEMS")
print("=" * 55)

# -------------------------------------------------------
# Reset to a fresh list for updating examples
# -------------------------------------------------------
print("\n--- Teacher's Corrected Class List (fresh start) ---")
class_list = ["aarav", "MEERA", "Rohen", "Priya", "Arjun"]
print(f"Class list (with errors) : {class_list}")
print("  Errors: 'aarav' needs proper case, 'MEERA' → 'Meera', 'Rohen' → 'Rohan'")

# -------------------------------------------------------
# UPDATE 1: Fix the FIRST item (index 0)
# -------------------------------------------------------
print("\n--- Update 1: Fix index 0 — 'aarav' → 'Aarav' ---")
print(f"Before update : {class_list}")

class_list[0] = "Aarav"                # Replace item at index 0

print(f"After  update : {class_list}")
print("  class_list[0] = 'Aarav' → first item is now fixed!")

# -------------------------------------------------------
# UPDATE 2: Fix a MIDDLE item (index 1)
# -------------------------------------------------------
print("\n--- Update 2: Fix index 1 — 'MEERA' → 'Meera' ---")
print(f"Before update : {class_list}")

class_list[1] = "Meera"               # Replace item at index 1

print(f"After  update : {class_list}")
print("  class_list[1] = 'Meera' → second item is now fixed!")

# -------------------------------------------------------
# UPDATE 3: Fix a spelling mistake (index 2)
# -------------------------------------------------------
print("\n--- Update 3: Fix index 2 — 'Rohen' → 'Rohan' ---")
print(f"Before update : {class_list}")

class_list[2] = "Rohan"               # Replace item at index 2

print(f"After  update : {class_list}")
print("  class_list[2] = 'Rohan' → spelling corrected!")

# -------------------------------------------------------
# UPDATE 4: Fix the LAST item using negative index
# -------------------------------------------------------
print("\n--- Update 4: Fix the LAST item using index -1 ---")
print(f"Before update : {class_list}")
print(f"  Last item currently : '{class_list[-1]}' → should be 'Arjun V'")

class_list[-1] = "Arjun V"            # Replace last item using -1

print(f"After  update : {class_list}")
print("  class_list[-1] = 'Arjun V' → last item updated using negative index!")

# -------------------------------------------------------
# Final corrected class list
# -------------------------------------------------------
print("\n" + "-" * 40)
print("  Final Corrected Class List:")
print(f"  {class_list}")
print(f"  Total students: {len(class_list)}")
print("-" * 40)

# -------------------------------------------------------
# Updating numbers in a marks list
# -------------------------------------------------------
print("\n--- Updating Marks — Number List ---")
marks_list = [88, 72, 95, 60, 80]
print(f"Original marks : {marks_list}")
print("  Meera's marks were entered wrong — 72 should be 82")

marks_list[1] = 82                     # Correct Meera's marks at index 1

print(f"Updated  marks : {marks_list}")
print("  marks_list[1] = 82 → Meera's marks corrected!")

# ============================================================
# QUICK REFERENCE SUMMARY
# ============================================================
# REMOVING:
#   remove(value)  → Remove by value (first match), ERROR if not found
#   pop(index)     → Remove by index, RETURNS the removed item
#   pop()          → Remove and RETURN the LAST item
#   clear()        → Remove ALL items, list becomes []
#
# UPDATING:
#   list[index] = new_value → Replace item at that index
#   list[-1] = new_value    → Replace the LAST item
#   list[0] = new_value     → Replace the FIRST item
# ============================================================

print("\n" + "=" * 55)
print("  QUICK REFERENCE SUMMARY")
print("=" * 55)
print("  --- REMOVING ---")
print("  remove(value)      → Remove by value (first match)")
print("  pop(index)         → Remove by index, returns item")
print("  pop()              → Remove & return the LAST item")
print("  clear()            → Remove ALL → list becomes []")
print("-" * 40)
print("  --- UPDATING ---")
print("  list[0]  = val     → Update the FIRST item")
print("  list[-1] = val     → Update the LAST item")
print("  list[i]  = val     → Update item at index i")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. What is the difference between remove() and pop()?
#    When would you use each one?
# 2. You have: colours = ["Red", "Blue", "Green", "Blue"]
#    What happens when you do colours.remove("Blue")?
#    (Hint: only ONE Blue gets removed — which one?)
# 3. pop() returns the removed item. How can you save that item
#    in a variable? Write the code.
# 4. If you do clear() on a list, does the variable disappear?
#    What does the list look like after clear()?
# ============================================================

# Program Code: LIST-KN-02
# Title: Adding Items to a List — append, insert, extend
# Cognitive Skill: Knowledge (Acquiring the concept)
# Topic: Lists in Python

# ============================================================
# PROBLEM STATEMENT:
# Diya is shopping with Amma for Pongal. She starts with a
# small list — then keeps thinking of more things to buy!
# Some items go to the END of the list, some need to go in
# the MIDDLE (like a priority item), and sometimes she wants
# to add a BUNCH of items at once from another list.
# Python has 3 methods to handle exactly this: append,
# insert, and extend!
# ============================================================

# ============================================================
# THREE WAYS TO ADD ITEMS TO A LIST:
#
#   append(item)         → Add ONE item to the END
#   insert(pos, item)    → Add ONE item at a SPECIFIC position
#   extend([item, item]) → Add MANY items from another list
# ============================================================

print("=" * 55)
print("   ADDING ITEMS TO A LIST — append, insert, extend")
print("=" * 55)

# -------------------------------------------------------
# Diya starts with a small shopping list
# -------------------------------------------------------
print("\n--- Diya's Starting Shopping List ---")
shopping_list = ["Rice", "Dal", "Sugar"]
print(f"Shopping list : {shopping_list}")
print(f"Number of items : {len(shopping_list)}")

# ============================================================
# METHOD 1: append() — Add ONE item to the END
# Use when: you want to add something to the tail of the list
# Think of it like adding a new item at the BOTTOM of a paper
# ============================================================

print("\n" + "=" * 55)
print("  METHOD 1: append() — Add to the END")
print("=" * 55)

# -------------------------------------------------------
# Step 1: Diya remembers she needs Oil
# -------------------------------------------------------
print("\n--- Step 1: Diya remembers Oil ---")
print(f"Before append : {shopping_list}")

shopping_list.append("Oil")             # Oil goes to the END

print(f"After  append : {shopping_list}")
print("  append('Oil') → added to the END of the list")

# -------------------------------------------------------
# Step 2: She also wants Salt
# -------------------------------------------------------
print("\n--- Step 2: Diya adds Salt ---")
print(f"Before append : {shopping_list}")

shopping_list.append("Salt")            # Salt goes to the END

print(f"After  append : {shopping_list}")
print("  append('Salt') → goes after Oil, at the END")

# -------------------------------------------------------
# Step 3: One more — she needs Turmeric
# -------------------------------------------------------
print("\n--- Step 3: Diya adds Turmeric ---")
print(f"Before append : {shopping_list}")

shopping_list.append("Turmeric")        # Turmeric goes to the END

print(f"After  append : {shopping_list}")
print("  append('Turmeric') → always adds at the very END")

print(f"\nList after 3 appends : {shopping_list}")
print(f"Total items now      : {len(shopping_list)}")

# ============================================================
# METHOD 2: insert(pos, item) — Add ONE item at a POSITION
# Use when: you need to place something at a specific spot
# Think of it like inserting a page in the MIDDLE of a book
#
# insert(0, item)  → adds at the very BEGINNING
# insert(2, item)  → adds at index 2, others shift right
# ============================================================

print("\n" + "=" * 55)
print("  METHOD 2: insert(pos, item) — Add at a POSITION")
print("=" * 55)

# -------------------------------------------------------
# Amma says Milk is most important — put it FIRST!
# -------------------------------------------------------
print("\n--- Amma says add Milk at the START (index 0) ---")
print(f"Before insert : {shopping_list}")

shopping_list.insert(0, "Milk")         # Milk goes to index 0 (start)

print(f"After  insert : {shopping_list}")
print("  insert(0, 'Milk') → placed at index 0, everything shifted right")

# -------------------------------------------------------
# Diya wants to add Jaggery after Dal (which is at index 2)
# -------------------------------------------------------
print("\n--- Diya adds Jaggery at index 2 (after Dal) ---")
print(f"Before insert : {shopping_list}")
print(f"  Index 2 currently holds : '{shopping_list[2]}'")

shopping_list.insert(2, "Jaggery")      # Jaggery goes at index 2

print(f"After  insert : {shopping_list}")
print("  insert(2, 'Jaggery') → placed at index 2, items after shifted right")

print(f"\nList after inserts : {shopping_list}")
print(f"Total items now    : {len(shopping_list)}")

# ============================================================
# METHOD 3: extend([...]) — Add MANY items from another list
# Use when: you have a whole group of items to add at once
# Think of it like merging two lists together
# extend() adds each item individually (NOT a list inside a list)
# ============================================================

print("\n" + "=" * 55)
print("  METHOD 3: extend([...]) — Add MANY Items at Once")
print("=" * 55)

# -------------------------------------------------------
# Diya's cousin Meera sends her extra items to buy
# -------------------------------------------------------
print("\n--- Meera sends extra items for her ---")
meera_extra_items = ["Coconut", "Cardamom", "Ghee"]
print(f"Meera's extra items   : {meera_extra_items}")
print(f"Before extend         : {shopping_list}")

shopping_list.extend(meera_extra_items) # All 3 items added to END

print(f"After  extend         : {shopping_list}")
print("  extend() adds ALL items from meera_extra_items to the END")

print(f"\nFinal shopping list : {shopping_list}")
print(f"Total items now     : {len(shopping_list)}")

# -------------------------------------------------------
# IMPORTANT: append vs extend — know the difference!
# -------------------------------------------------------
print("\n" + "-" * 40)
print("  append vs extend — What is the difference?")
print("-" * 40)

list_a = ["Pen", "Book"]
list_b = ["Pen", "Book"]

list_a.append(["Ruler", "Eraser"])   # Appends the LIST as ONE item
list_b.extend(["Ruler", "Eraser"])   # Extends with individual items

print(f"\nAfter append(['Ruler','Eraser']) : {list_a}")
print(f"  → The whole list became ONE item inside list_a!")

print(f"\nAfter extend(['Ruler','Eraser']) : {list_b}")
print(f"  → Each item was added separately to list_b!")
print("-" * 40)

# ============================================================
# QUICK REFERENCE SUMMARY
# ============================================================
# append(item)        → Adds 1 item to the END
# insert(pos, item)   → Adds 1 item at a specific INDEX
# extend([i1, i2])    → Adds MANY items from another list to END
#
# insert(0, item)     → Adds to the very BEGINNING
# append ≠ extend     → append([a,b]) nests a list inside,
#                        extend([a,b]) adds a and b separately
# ============================================================

print("\n" + "=" * 55)
print("  QUICK REFERENCE SUMMARY")
print("=" * 55)
print("  append(item)       → Add 1 item to the END")
print("  insert(pos, item)  → Add 1 item at position pos")
print("  extend([i1, i2])   → Add MANY items to the END")
print("-" * 40)
print("  insert(0, x)       → Add to the very BEGINNING")
print("  append([a, b])     → Adds a LIST as 1 item (nested!)")
print("  extend([a, b])     → Adds a and b as separate items")
print("=" * 55)

# ============================================================
# REFLECTION:
# 1. Diya has a list: items = ["Pen", "Pencil", "Eraser"]
#    She wants to add "Ruler" to the END. Which method does she use?
# 2. She now wants to add "Sharpener" at position 1 (between
#    "Pen" and "Pencil"). What code does she write?
# 3. What is the difference between append(["A","B"]) and
#    extend(["A","B"])? Try both and observe the output!
# 4. If you do insert(100, "X") on a list with only 3 items,
#    what do you think happens? Run it and find out!
# ============================================================

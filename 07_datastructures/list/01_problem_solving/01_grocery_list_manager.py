
# Program Code: LIST-PS-01
# Title: Amma's Grocery List — Managing a Shopping List!
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Lists in Python

# ======================================================
# WHAT PROBLEM ARE WE SOLVING?
# ======================================================
# Amma is going to the market.
# She has a grocery list but it keeps changing —
#   - She remembers more items to buy
#   - She finds some items already at home
#   - She wants items in a specific order
# We need to help her MANAGE the list as it changes!
#
# WHY USE A LIST?
# A list lets us store MULTIPLE items together and
# change them easily — add, remove, insert, reorder.
# Without a list, we'd need a new variable for every item!
# ======================================================

# ======================================================
# DECOMPOSE THE PROBLEM
# ======================================================
# Break the big problem into small, clear steps:
#
# Step 1: Create the initial grocery list with known items
# Step 2: Amma remembers 2 more items → add them to the list
# Step 3: She found salt at home → remove it from the list
# Step 4: She wants sugar placed before dal → insert at correct position
# Step 5: Show the final numbered shopping list neatly
# Step 6: Count and display the total number of items to buy
#
# BONUS: Sort the list alphabetically so it is easier
#        to find items aisle by aisle in the store
# ======================================================


print("=" * 55)
print("   Amma's Grocery List — Managing a Shopping List!")
print("=" * 55)


# --------------------------------------------------
# STEP 1: Create the initial grocery list
# --------------------------------------------------
# Amma wrote down these items before leaving home

grocery_list = ["rice", "dal", "oil", "salt", "onion", "tomato"]

print("\nStep 1: Amma's initial grocery list")
print("-" * 40)
print("Items Amma wrote down:", grocery_list)


# --------------------------------------------------
# STEP 2: Amma remembers 2 more items — add them
# --------------------------------------------------
# She remembered she also needs coriander and green chilli
# append() adds one item at a time to the END of the list

grocery_list.append("coriander")
grocery_list.append("green chilli")

print("\nStep 2: Amma remembered 2 more items")
print("-" * 40)
print("Added: coriander, green chilli")
print("Updated list:", grocery_list)


# --------------------------------------------------
# STEP 3: She found salt at home — remove it
# --------------------------------------------------
# She checked her kitchen and found a full packet of salt
# remove() finds the first match and deletes it

grocery_list.remove("salt")

print("\nStep 3: Found salt at home — removed it!")
print("-" * 40)
print("Removed: salt")
print("Updated list:", grocery_list)


# --------------------------------------------------
# STEP 4: She wants sugar placed BEFORE dal
# --------------------------------------------------
# Amma also decided she needs sugar
# But she wants to see it listed BEFORE dal in the list
# First, find the position (index) of "dal"
# Then use insert() to place "sugar" at that exact position

dal_position = grocery_list.index("dal")    # find where "dal" is
grocery_list.insert(dal_position, "sugar")  # insert "sugar" before "dal"

print("\nStep 4: Insert sugar before dal")
print("-" * 40)
print(f"'dal' is at position {dal_position} — inserting 'sugar' before it")
print("Updated list:", grocery_list)


# --------------------------------------------------
# STEP 5: Show the final numbered shopping list
# --------------------------------------------------
# Display as a neat numbered list, like a proper checklist

print()
print("=" * 55)
print("       AMMA'S FINAL SHOPPING LIST")
print("=" * 55)

for number, item in enumerate(grocery_list, start=1):
    print(f"  {number}. {item.capitalize()}")

print("=" * 55)


# --------------------------------------------------
# STEP 6: Count total items to buy
# --------------------------------------------------
# len() tells us how many items are in the list

total_items = len(grocery_list)
print(f"\nStep 6: Total items to buy → {total_items} items")
print("-" * 40)
print("Amma now knows exactly what to pick up at the market!")


# --------------------------------------------------
# BONUS: Sort alphabetically for easier shopping
# --------------------------------------------------
# Stores are often arranged alphabetically or by aisle
# sorted() creates a new sorted list without changing the original

print()
print("=" * 55)
print("   BONUS: Alphabetically Sorted List (Store-Friendly)")
print("=" * 55)

sorted_list = sorted(grocery_list)  # sorted() returns a new sorted list

print("Sorted list makes it easier to find items in the store:\n")
for number, item in enumerate(sorted_list, start=1):
    print(f"  {number}. {item.capitalize()}")

print("=" * 55)
print("\nHappy shopping, Amma!")


# ======================================================
# REFLECTION — Think and Answer
# ======================================================
# 1. What is the difference between append() and insert()?
#    When would you use insert() instead of append()?
#
# 2. What happens if you try to remove() an item that is
#    NOT in the list? Try it — what error do you get?
#
# 3. Why does sorted() not change the original list but
#    sort() does? Which one is safer to use and why?
#
# 4. How would you write code that lets Amma type the
#    grocery items herself instead of hardcoding them?
#    Think about using input() and a loop.
# ======================================================

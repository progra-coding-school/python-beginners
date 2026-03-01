# Lists Are Mutable
# Mutable means "can be changed after it is created."
# Strings are IMMUTABLE — once created, you cannot change individual characters.
# Lists are MUTABLE   — you can change, add, or remove items at any time.
# IMPORTANT: two variables pointing to the same list BOTH see every change!

# --- Strings are IMMUTABLE (cannot change individual characters) ---
# Trying name[0] = "B" would cause a TypeError — strings do not allow this
print("Strings are immutable:")
name = "Aarav"
print("name:", name)
# name[0] = "B"   ← this would cause TypeError: 'str' object does not support item assignment
print("You cannot do name[0] = 'B' — strings are immutable.")
print()

# --- Lists are MUTABLE (you can change any item by its index) ---
# list[i] = new_value replaces the item at position i with a new value
print("Lists are mutable:")
team = ["Aarav", "Diya", "Kabir"]
print("Before:", team)
team[0] = "Rohan"     # replace the first item
print("After team[0] = 'Rohan':", team)

team[2] = "Meera"     # replace the third item
print("After team[2] = 'Meera':", team)
print()

# --- append and remove also mutate (change) the list ---
# Every method that modifies a list is a mutation
scores = [80, 90, 70]
print("Before mutations:", scores)
scores.append(95)             # adds 95 at the end
print("After append(95):", scores)
scores.remove(70)             # removes the first 70
print("After remove(70):", scores)
print()

# --- Shared reference trap ---
# When you write alias = original, you are NOT making a copy.
# Both variables point to the SAME list in memory.
# Changing one changes the other — this surprises many beginners!
print("Shared reference (important!):")
original = [1, 2, 3]
alias = original          # alias is NOT a copy — it points to the exact same list
alias.append(4)
print("original:", original)   # [1, 2, 3, 4] — original changed too!
print("alias   :", alias)      # [1, 2, 3, 4] — same list, same change

print()

# --- Making a real independent copy ---
# Use .copy() or [:] to create a separate copy that does not affect the original
print("Making a real copy:")
original = [1, 2, 3]
copy1 = original.copy()   # method 1 — explicit copy
copy2 = original[:]       # method 2 — full slice also makes a copy
copy1.append(99)
print("original:", original)   # [1, 2, 3] — unchanged, copy1 is independent
print("copy1   :", copy1)      # [1, 2, 3, 99]
print("copy2   :", copy2)      # [1, 2, 3]

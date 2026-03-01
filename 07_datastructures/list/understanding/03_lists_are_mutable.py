# Lists Are Mutable

# --- Strings are IMMUTABLE (cannot change individual characters) ---
print("Strings are immutable:")
name = "Aarav"
print("name:", name)
# name[0] = "B"   ← this would cause TypeError!
print("You cannot do name[0] = 'B' — strings are immutable.")
print()

# --- Lists are MUTABLE (you can change any item) ---
print("Lists are mutable:")
team = ["Aarav", "Diya", "Kabir"]
print("Before:", team)
team[0] = "Rohan"     # change the first item
print("After team[0] = 'Rohan':", team)

team[2] = "Meera"     # change another item
print("After team[2] = 'Meera':", team)
print()

# --- append, remove also mutate the list ---
scores = [80, 90, 70]
print("Before mutations:", scores)
scores.append(95)
print("After append(95):", scores)
scores.remove(70)
print("After remove(70):", scores)
print()

# --- Shared reference trap ---
print("Shared reference (important!):")
original = [1, 2, 3]
alias = original          # NOT a copy — both point to the same list!
alias.append(4)
print("original:", original)   # [1, 2, 3, 4] — both changed!
print("alias   :", alias)

print()

# --- Making a real copy ---
print("Making a real copy:")
original = [1, 2, 3]
copy1 = original.copy()   # method 1
copy2 = original[:]       # method 2 (slice)
copy1.append(99)
print("original:", original)   # [1, 2, 3] — unchanged
print("copy1   :", copy1)      # [1, 2, 3, 99]
print("copy2   :", copy2)      # [1, 2, 3]

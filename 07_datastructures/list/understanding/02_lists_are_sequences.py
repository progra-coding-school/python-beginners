# Lists Are Sequences
# A sequence means items are stored in a fixed ORDER with index numbers.
# Every item has TWO addresses:
#   Positive index → count from the LEFT, starting at 0
#   Negative index → count from the RIGHT, starting at -1
# Knowing this lets you reach any item precisely.

team = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
#        index 0    1       2        3        4       ← positive (left to right)
#        index -5   -4     -3       -2       -1       ← negative (right to left)

print("List:", team)
print()

# --- Positive indexing (left to right, starts at 0) ---
# Index 0 = first item, index 1 = second item, and so on
print("Positive indexing:")
print("team[0]:", team[0])     # Aarav — first item
print("team[1]:", team[1])     # Diya  — second item
print("team[4]:", team[4])     # Rohan — fifth (last) item

print()

# --- Negative indexing (right to left, starts at -1) ---
# Index -1 always means the LAST item — useful when you don't know the length
print("Negative indexing:")
print("team[-1]:", team[-1])   # Rohan — last item
print("team[-2]:", team[-2])   # Meera — second from last
print("team[-5]:", team[-5])   # Aarav — fifth from last = first item

print()

# --- IndexError: going out of range ---
# A list of 5 items has valid indices 0, 1, 2, 3, 4 (and -1, -2, -3, -4, -5)
# Asking for index 5 or higher → IndexError (that slot does not exist!)
print("Length of team:", len(team))   # 5 items
print("Valid indices: 0 to", len(team) - 1)
# team[5] → IndexError! (index 5 does not exist in a 5-item list)

print()

# --- Index table — shows both positive and negative index for each item ---
print("Index table:")
for i in range(len(team)):
    neg = i - len(team)      # negative index = positive index - length
    print("  index " + str(i) + " : " + team[i] + "  | negative index " + str(neg) + " : " + team[neg])

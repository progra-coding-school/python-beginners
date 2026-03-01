# Program Code: LIST-UN-02
# Title: Lists Are Sequences
# Cognitive Skill: Understanding (Index and order)
# Topic: Lists in Python

team = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
#        index 0    1       2        3        4
#        index -5   -4     -3       -2       -1

print("List:", team)
print()

# --- Positive indexing (left to right, starts at 0) ---
print("Positive indexing:")
print("team[0]:", team[0])     # Aarav
print("team[1]:", team[1])     # Diya
print("team[4]:", team[4])     # Rohan

print()

# --- Negative indexing (right to left, starts at -1) ---
print("Negative indexing:")
print("team[-1]:", team[-1])   # Rohan (last)
print("team[-2]:", team[-2])   # Meera (second last)
print("team[-5]:", team[-5])   # Aarav (first, via negative)

print()

# --- IndexError: going out of range ---
print("Length of team:", len(team))   # 5
print("Valid indices: 0 to", len(team) - 1)
# team[5] → IndexError! (index 5 does not exist in a 5-item list)

print()

# --- Index table ---
print("Index table:")
for i in range(len(team)):
    neg = i - len(team)
    print("  index " + str(i) + " : " + team[i] + "  | negative index " + str(neg) + " : " + team[neg])

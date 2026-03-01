# Spot the Difference – Which List Changed?
# Two lists appear. Spot exactly what changed between List A and List B.

score = 0


# Round 1 — capitalisation
print("Round 1 of 5: Aarav's Fruit Basket")
print("  List A:", ["apple", "banana", "mango"])
print("  List B:", ["apple", "Banana", "mango"])
input("  What changed? Think first, then press Enter... ")
print('  Difference: "banana" became "Banana" — capital B.')
print('  In Python, "banana" != "Banana" — capitalisation matters!')
print()
ans = input("  Did you spot it correctly? (y/n): ").strip().lower()
if ans == "y":
    score += 1
print()

# Round 2 — extra zero
print("Round 2 of 5: Diya's Cricket Score Sheet")
print("  List A:", [10, 20, 30, 40, 50])
print("  List B:", [10, 20, 30, 40, 500])
input("  What changed? Think first, then press Enter... ")
print("  Difference: the last number changed from 50 to 500 — an extra zero!")
print("  A score of 500 in cricket is impossible. Always check if numbers look reasonable.")
print()
ans = input("  Did you spot it correctly? (y/n): ").strip().lower()
if ans == "y":
    score += 1
print()

# Round 3 — extra item added
print("Round 3 of 5: Kabir's Class Register")
print("  List A:", ["Aarav", "Diya", "Kabir"])
print("  List B:", ["Aarav", "Diya", "Kabir", "Meera"])
input("  What changed? Think first, then press Enter... ")
print('  Difference: "Meera" was added at the end. List A has 3 items, List B has 4.')
print("  How to check: use len() — if lengths differ, something was added or removed.")
print()
ans = input("  Did you spot it correctly? (y/n): ").strip().lower()
if ans == "y":
    score += 1
print()

# Round 4 — two items swapped
print("Round 4 of 5: Riya's Colour Palette")
print("  List A:", ["red", "green", "blue"])
print("  List B:", ["red", "blue", "green"])
input("  What changed? Think first, then press Enter... ")
print('  Difference: "green" and "blue" swapped positions.')
print("  Order matters! If your code depends on index position, a swap gives wrong results.")
print()
ans = input("  Did you spot it correctly? (y/n): ").strip().lower()
if ans == "y":
    score += 1
print()

# Round 5 — subtle swap (Boss Round)
print("Round 5 of 5 (Boss Round): Aarav's Number Sequence")
print("  List A:", [1, 2, 3, 4, 5])
print("  List B:", [1, 2, 3, 5, 4])
input("  What changed? Think first, then press Enter... ")
print("  Difference: the last two numbers swapped — 4 and 5 flipped positions.")
print("  Tip: compare lists item by item from left to right, like proofreading a sentence.")
print()
ans = input("  Did you spot it correctly? (y/n): ").strip().lower()
if ans == "y":
    score += 1
print()

print("Score:", score, "/ 5")
if score == 5:
    print("Sharp eyes! You are a List Detective!")
elif score >= 3:
    print("Good focus! Keep training your attention.")
else:
    print("Keep practising — focus takes training!")

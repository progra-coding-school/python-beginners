# Spot the Difference – Which List Changed?
# Two lists appear. Spot exactly what changed between List A and List B.
# This trains your eye to read lists carefully — a critical debugging skill.
# In real code, a single wrong character (capital B vs b, 50 vs 500) causes bugs.

score = 0


# Round 1 — capitalisation
# "banana" and "Banana" look almost identical — but Python treats them as different!
# Case sensitivity is one of the most common beginner bugs.
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
# 50 and 500 differ by one digit — easy to miss when scanning quickly.
# Always check if numbers are in a reasonable range for the context.
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
# The lengths differ — List A has 3 items, List B has 4.
# len() is your first check when you suspect something was added or removed.
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
# All items exist in both lists — but their ORDER is different.
# Order matters! If code depends on index position, a swap gives wrong results.
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
# The swap is at the END of the list — the beginning looks identical.
# Tip: always compare lists item by item from LEFT to RIGHT, like proofreading a sentence.
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

# Which Approach Is Better?
# Good programmers don't just find ONE solution — they compare solutions.
# For each problem below, two approaches are shown. Pick the cleaner one and say WHY.
# KEY RULE: simpler code is better — fewer steps, fewer bugs, easier to read.

score = 0


# --- Problem 1: Remove a player by name ---
# Approach A: first find the index with index(), THEN remove with pop() — two steps
# Approach B: remove() searches by VALUE and deletes in one step
# remove() was designed exactly for this — use the right tool!
print("Problem 1: Remove 'Kabir' from a team list.")
print()
print("  Approach A:")
print("    index = team.index('Kabir')")
print("    team.pop(index)")
print()
print("  Approach B:")
print("    team.remove('Kabir')")
print()
ans = input("  Which is simpler? (A or B): ").strip().upper()
if ans == "B":
    print("  Correct! remove() removes by VALUE in one line. Use pop() only when you know the INDEX.")
    score += 1
else:
    print("  Answer: B — remove('Kabir') does it in one step. pop() needs the index first.")
print()

# --- Problem 2: Add multiple items ---
# Approach A: a loop calling append() once per item — works but is 3 lines instead of 1
# Approach B: extend() adds ALL items from a list at once — built exactly for this job
# Rule: when Python has a built-in method for the job, use it!
print("Problem 2: Add ['oil', 'sugar', 'ghee'] to a shopping cart.")
print()
print("  Approach A:")
print("    for item in new_items:")
print("        cart.append(item)")
print()
print("  Approach B:")
print("    cart.extend(new_items)")
print()
ans = input("  Which is better? (A or B): ").strip().upper()
if ans == "B":
    print("  Correct! extend() adds all items at once. Fewer lines, same result.")
    score += 1
else:
    print("  Answer: B — extend() is built for adding multiple items in one step.")
print()

# --- Problem 3: Check if player exists ---
# Approach A: manually checks every index — breaks the moment the list grows beyond 3!
# Approach B: 'in' keyword scans the entire list automatically, no matter how long it is
# Never hard-code index checks — always use 'in' for existence checks.
print("Problem 3: Check if 'Meera' is in the team.")
print()
print("  Approach A:")
print("    if team[0] == 'Meera' or team[1] == 'Meera' or team[2] == 'Meera':")
print("        print('Found')")
print()
print("  Approach B:")
print("    if 'Meera' in team:")
print("        print('Found')")
print()
ans = input("  Which is better? (A or B): ").strip().upper()
if ans == "B":
    print("  Correct! The 'in' keyword searches the whole list automatically.")
    score += 1
else:
    print("  Answer: B — 'in' works for any size list. Approach A breaks if the list grows.")
print()

print("Score:", score, "/ 3")
print()
# Quick reference: when to use which method
print("Key rules:")
print("  Remove by VALUE  → remove(value)")
print("  Remove by INDEX  → pop(index)")
print("  Add many items   → extend(list)")
print("  Search in list   → item in list")

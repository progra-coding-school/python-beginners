# Program Code: LIST-CT-02
# Title: Which Approach Is Better?
# Cognitive Skill: Critical Thinking (Evaluating solutions)
# Topic: Lists in Python

score = 0

print("=== Which Approach Is Better? ===")
print("Compare two solutions and pick the better one.")
print()

# --- Problem 1: Remove a player by name ---
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
print("Key rules:")
print("  Remove by VALUE  → remove(value)")
print("  Remove by INDEX  → pop(index)")
print("  Add many items   → extend(list)")
print("  Search in list   → item in list")

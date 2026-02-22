# Program Code: VAR-LR-03
# Title: The Swap Challenge
# Cognitive Skill: Logical Reasoning (Sequential reasoning)
# Topic: Variables in Python

# Level 1 — swap two values using a temp variable
print("--- Level 1: Swap the Boxes ---")
aarav_box = "Laddoos"
diya_box = "Jalebis"
print("Before — Aarav:", aarav_box, " Diya:", diya_box)

temp_box = aarav_box       # save Aarav's items
aarav_box = diya_box       # give Aarav what Diya had
diya_box = temp_box        # give Diya what was saved

print("After  — Aarav:", aarav_box, " Diya:", diya_box)

input("Press Enter for Level 2...")

# Level 2 — swap numbers
print("--- Level 2: Swap Two Numbers ---")
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print("Before: a =", a, "  b =", b)

temp = a
a = b
b = temp

print("After:  a =", a, "  b =", b)

input("Press Enter for Level 3...")

# Level 3 — three-way swap
print("--- Level 3: Three-Way Swap ---")
aarav = "Laddoos"
diya = "Jalebis"
priya = "Mysore Pak"
print("Before:", aarav, diya, priya)

temp = aarav
aarav = diya
diya = priya
priya = temp

print("After: ", aarav, diya, priya)

input("Press Enter for Bonus...")

# Bonus — swap without temp using maths
print("--- Bonus: Swap Without Temp ---")
a = 15
b = 27
print("Before: a =", a, "  b =", b)

a = a + b
b = a - b
a = a - b

print("After:  a =", a, "  b =", b)
print("Works without a temp variable!")

# Think:
# 1. What would happen in Level 1 if we did NOT use temp_box?
# 2. Try the bonus trick with a=10, b=7 on paper. Does it work?

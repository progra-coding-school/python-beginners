# Program Code: VAR-ST-02
# Title: Naming Matters
# Cognitive Skill: Structured Thinking (Naming conventions)
# Topic: Variables in Python

# Part 1 — Can you understand this?
print("--- Part 1: Bad names ---")
print("  x = 12")
print("  y = 8")
print("  z = x + y")
print("  a = z / 2")
print("  print(a)")

x = 12
y = 8
z = x + y
a = z / 2
print("Output:", a)

answer = input("What does this calculate? ")

# Reveal with good names
print("Same program with good names:")
print("  aarav_age = 12")
print("  diya_age = 8")
print("  total_age = aarav_age + diya_age")
print("  average_age = total_age / 2")

aarav_age = 12
diya_age = 8
total_age = aarav_age + diya_age
average_age = total_age / 2
print("Output:", average_age)
print("Now you can see it calculates the AVERAGE AGE!")

input("Press Enter for Part 2...")

# Part 2 — decode confusing code
print("--- Part 2: Decode the Confusing Code ---")
print("  p = 250, q = 3, r = 50")
print("  s = p * q")
print("  t = s - r")
print("  print(t)")

p = 250
q = 3
r = 50
s = p * q
t = s - r
print("Output:", t)

input("Guess what it calculates... Press Enter to see answer.")

print("With good names:")
print("  price_per_item = 250")
print("  quantity = 3")
print("  discount = 50")
print("  subtotal = price_per_item * quantity")
print("  final_price = subtotal - discount")

price_per_item = 250
quantity = 3
discount = 50
subtotal = price_per_item * quantity
final_price = subtotal - discount
print("Output:", final_price)
print("It was a shopping bill calculation!")

input("Press Enter for Part 3...")

# Part 3 — you rename
print("--- Part 3: You Rename the Variables ---")
print("  a1=85, a2=90, a3=78, a4=92, a5=88")
print("  t = a1+a2+a3+a4+a5")
print("  p = t / 5")

a1, a2, a3, a4, a5 = 85, 90, 78, 92, 88
t = a1 + a2 + a3 + a4 + a5
p = t / 5
print("Output: total =", t, "  average =", p)

name_a1 = input("Better name for a1 (marks in first subject)? ")
name_t = input("Better name for t (sum of all marks)? ")
name_p = input("Better name for p (average)? ")

print("Good version:")
print("  maths_marks = 85, science_marks = 90 ...")
print("  total_marks = maths_marks + science_marks + ...")
print("  percentage = total_marks / 5")
print("Rule: names should tell WHAT the variable stores.")

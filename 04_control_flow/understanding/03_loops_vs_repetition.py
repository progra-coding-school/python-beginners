# Program Code: CF-UN-03
# Title: Loops vs. Repetition
# Cognitive Skill: Understanding
# Topic: Control Flow in Python

# PROBLEM: print the multiplication table of 7

# WITHOUT a loop — you write every line yourself
print("7 x 1 =", 7 * 1)
print("7 x 2 =", 7 * 2)
print("7 x 3 =", 7 * 3)
print("7 x 4 =", 7 * 4)
print("7 x 5 =", 7 * 5)
print("7 x 6 =", 7 * 6)
print("7 x 7 =", 7 * 7)
print("7 x 8 =", 7 * 8)
print("7 x 9 =", 7 * 9)
print("7 x 10 =", 7 * 10)

# WITH a loop — one pattern handles everything
n = int(input("Enter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Loops also allow ACCUMULATION — collecting results
print("--- Accumulate sum ---")
total = 0
for marks in [88, 92, 74, 85, 79]:
    total = total + marks
average = total / 5
print("Total:", total, "  Average:", average)

# Without a loop — each mark added manually
total = 88 + 92 + 74 + 85 + 79
print("Same total:", total)
# (works for 5 marks, but what about 40 students?)

# Think:
# 1. If you had 500 students, which approach saves more effort?
# 2. Can you change the table program above to print tables of 1 to 10 using a nested loop?

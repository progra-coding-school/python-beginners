# Program Code: OP-UN-02
# Title: How Operator Precedence Works
# Cognitive Skill: Understanding
# Topic: Operators in Python

# Precedence = which operator gets calculated first.
# Python follows BODMAS / PEMDAS:
# Brackets → Exponents → Division/Multiplication → Addition/Subtraction

# --- Example 1 ---
result = 5 + 3 * 4
print("5 + 3 * 4 =", result)
# Step 1: 3 * 4 = 12  (multiplication first!)
# Step 2: 5 + 12 = 17

# --- Example 2 ---
result = (5 + 3) * 4
print("(5 + 3) * 4 =", result)
# Step 1: (5 + 3) = 8  (brackets first!)
# Step 2: 8 * 4 = 32

# --- Example 3 ---
result = 10 + 6 / 2
print("10 + 6 / 2 =", result)
# Step 1: 6 / 2 = 3.0  (division first!)
# Step 2: 10 + 3.0 = 13.0

# --- Example 4 ---
result = 2 ** 3 + 4 * 2
print("2 ** 3 + 4 * 2 =", result)
# Step 1: 2 ** 3 = 8   (exponent first!)
# Step 2: 4 * 2 = 8    (multiplication)
# Step 3: 8 + 8 = 16

# --- Example 5 ---
result = 10 + 6 * 2 - 4 / 2
print("10 + 6 * 2 - 4 / 2 =", result)
# Step 1: 6 * 2 = 12
# Step 2: 4 / 2 = 2.0
# Step 3: 10 + 12 - 2.0 = 20.0

print()
# --- Real-life: Wrong vs Right ---
# Cricket: Total runs from boundaries + singles
fours = 5
sixes = 3
singles = 12

# WRONG (no brackets — precedence causes error in thinking)
wrong = fours * 4 + sixes * 6 + singles
# Actually this is correct by precedence, but let's show when brackets matter:

# WRONG thinking: (fours + sixes) * 10
wrong2 = (fours + sixes) * 10
print("Wrong calculation:", wrong2)   # 80 — treats all as same value

# RIGHT — break it step by step
boundary_runs = (fours * 4) + (sixes * 6)
total_runs = boundary_runs + singles
print("Correct boundary runs:", boundary_runs)
print("Correct total runs:", total_runs)

# Think:
# 1. What is the result of 8 + 2 ** 2 * 3? Solve it step by step.
# 2. Add brackets to make 8 + 2 ** 2 * 3 equal 300.

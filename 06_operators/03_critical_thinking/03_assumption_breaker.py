# Program Code: OP-CT-03
# Title: Assumption Breaker — Operators
# Cognitive Skill: Critical Thinking (Assumption Breaking)
# Topic: Operators in Python

# We often make wrong assumptions about how operators work.
# Let's break those assumptions with examples!

print("=== Assumption Breaker ===")
print()

# --- Assumption 1 ---
print("Assumption 1: 'Division always gives a whole number if divisible'")
result = 10 / 2
print(f"  10 / 2 = {result}  (type: {type(result).__name__})")
print("  WRONG! / ALWAYS returns a float. 10/2 = 5.0, not 5.")
print("  Use // for integer result: 10 // 2 =", 10 // 2)
print()

# --- Assumption 2 ---
print("Assumption 2: 'Bigger number % smaller number = bigger number'")
result1 = 5 % 10
result2 = 3 % 100
print(f"  5 % 10 = {result1}  (not 5, but... actually yes, 5 itself!)")
print(f"  3 % 100 = {result2}")
print("  Surprise: If the dividend < divisor, the remainder IS the dividend!")
print("  5 ÷ 10 = 0 remainder 5. So 5 % 10 = 5.")
print()

# --- Assumption 3 ---
print("Assumption 3: 'and is the same as or — both check conditions'")
age = 15
has_id = False

result_and = age >= 13 and has_id
result_or = age >= 13 or has_id
print(f"  age=15, has_id=False")
print(f"  age >= 13 AND has_id = {result_and}")
print(f"  age >= 13 OR has_id = {result_or}")
print("  WRONG! 'and' requires BOTH true. 'or' needs just ONE true.")
print()

# --- Assumption 4 ---
print("Assumption 4: '** is the same as * 2 (multiplying by 2)'")
x = 3
print(f"  3 ** 2 = {3 ** 2}  (3 to the power 2 = 3 × 3 = 9)")
print(f"  3 * 2  = {3 * 2}   (3 multiplied by 2 = 6)")
print("  WRONG! ** means 'raised to the power', not 'times 2'.")
print(f"  3 ** 3 = {3 ** 3}, but 3 * 3 = {3 * 3}")
print()

# --- Assumption 5 ---
print("Assumption 5: 'not reverses numbers too'")
n = 5
print(f"  not 5 = {not 5}")
print(f"  not 0 = {not 0}")
print("  Surprise: 'not' works on truthiness! 0 is falsy, so not 0 = True.")
print("  not works on booleans. For numbers: 0 → False, everything else → True.")
print()

# Think:
# 1. What is 7 % 7? What about 0 % 5? Test your assumptions!
# 2. What does not not True give? Trace it step by step.

# Program Code: DT-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking (Challenging assumptions)
# Topic: Data Types in Python

# Challenge common assumptions about data types.
print("=== Assumption Breaker ===\n")

# Assumption 1: "If it looks like a number, it IS a number"
print("--- Assumption 1 ---")
print("Assume: x = '42' is a number")
x = '42'
print("Type of x:", type(x))       # str!
print("x + '8' =", x + '8')       # '428', not 50!
print("BROKEN: '42' is text — looks like a number but isn't!")
input("Press Enter to continue...")

# Assumption 2: "int() always rounds properly"
print("\n--- Assumption 2 ---")
print("Assume: int(9.9) = 10")
result = int(9.9)
print("Actual:", result)           # 9
print("BROKEN: int() truncates. Use round() to round.")
input("Press Enter to continue...")

# Assumption 3: "Division gives an integer"
print("\n--- Assumption 3 ---")
print("Assume: 10 / 2 gives int")
result = 10 / 2
print("Type:", type(result))       # float!
print("Value:", result)            # 5.0
print("BROKEN: Division always gives float. Use // for int division.")
input("Press Enter to continue...")

# Assumption 4: "bool is just 0 or 1"
print("\n--- Assumption 4 ---")
print("Assume: bool only compares to True/False")
print("bool('') =", bool(''))      # False — empty string
print("bool('0') =", bool('0'))    # True — '0' is a non-empty string!
print("bool(0) =", bool(0))        # False — zero is False
print("BROKEN: Many values convert to True/False in unexpected ways!")
input("Press Enter to continue...")

# Assumption 5: "str + int works like f-strings"
print("\n--- Assumption 5 ---")
print("Assume: 'Score: ' + 95 works like f'Score: {95}'")
try:
    result = 'Score: ' + 95
except TypeError as e:
    print("ERROR:", e)
print("BROKEN: + requires same type. Use str(95) or an f-string.")

# Think:
# 1. Which assumption surprised you most? Why?
# 2. Can you find another Python type assumption that could trick a beginner?

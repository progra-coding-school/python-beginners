# Types of Output
# Python can display many different types of data using print().
# Text, numbers, calculations, combinations — all shown with the same function.

# --- Type 1: Text (String) ---
# Text must be wrapped in quotes to be treated as a string
print("Hello, I am Diya!")
print('My favourite sport is cricket.')

# --- Type 2: Whole Numbers (Integer) ---
# No quotes needed — Python knows these are numbers
print(42)
print(2024)
print(0)

# --- Type 3: Decimal Numbers (Float) ---
print(3.14)
print(9.99)
print(0.5)

# --- Type 4: Arithmetic Results ---
# Python evaluates the expression first, then prints the result
print(10 + 5)       # Addition → 15
print(20 - 8)       # Subtraction → 12
print(6 * 7)        # Multiplication → 42
print(15 / 4)       # Division → 3.75 (always gives a float!)
print(15 // 4)      # Floor division → 3 (rounds down to integer)
print(15 % 4)       # Remainder → 3 (the leftover after division)
print(2 ** 8)       # Power → 256 (2 to the power of 8)

# --- Type 5: Text + Numbers together (with comma) ---
# Comma automatically adds a space between items — no str() needed
print("Age:", 13)
print("Score:", 95)
print("Pi is approximately", 3.14159)

# --- Type 6: Multiple items (separated by comma) ---
# All items printed on one line with a space between each
print("Name:", "Aarav", "Age:", 13, "Grade:", 7)

# --- Type 7: Repeating text ---
# * with a string repeats it that many times
print("=" * 30)     # prints = thirty times
print("Ha" * 5)     # HaHaHaHaHa

# Think:
# 1. What is the difference between print(5+5) and print("5+5")?
# 2. What does print("*" * 10) display?

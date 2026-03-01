# Strings vs Numbers in Output
# "5" is NOT the same as 5 in Python.
# One is text (str), one is a number (int). Mixing them with + causes errors!

# --- String '5' vs Number 5 ---
# type() shows you what Python thinks something is
print("5")     # string — just the character 5 (text)
print(5)       # integer — the number five (math)
print(type("5"))   # <class 'str'>
print(type(5))     # <class 'int'>

print()

# --- Addition: very different results! ---
# Number + Number = arithmetic (maths)
print(5 + 5)           # 10  (arithmetic)

# String + String = joining (concatenation — text glued together)
print("5" + "5")       # "55"  (joined text — NOT ten!)

print()

# --- You CANNOT mix string and number with + ---
# Python cannot add text and a number — they're different types
# print("5" + 5)   ← TypeError!  Cannot add str and int
# Fix option 1: convert number to string first
print("Score: " + str(85))      # str(85) converts the integer to text "85"

# Fix option 2: use comma (Python handles the conversion automatically)
print("Score:", 85)              # comma adds a space and no str() needed

print()

# --- Arithmetic inside print ---
# Quotes determine whether Python calculates or just shows text
print(100 + 200)        # 300  (math — no quotes around numbers)
print("100" + "200")    # 100200  (text join — quotes make them strings)
print("100 + 200")      # 100 + 200 (just the text, no calculation happens inside quotes)
print("100 + 200 =", 100 + 200)      # 100 + 200 = 300 (text label + result)

print()

# --- Real-life: price display ---
price = 149
quantity = 3

# BAD: mixing types causes error
# total_text = "Total: Rs." + price * quantity   ← TypeError — can't join str and int

# GOOD approaches:
print("Total: Rs." + str(price * quantity))       # str() converts the calculated number
print("Total: Rs.", price * quantity)             # comma lets print handle both types

# Think:
# 1. What does print("3" * 4) display? What about print(3 * 4)?
# 2. Why can't you do "Age: " + 13 directly? What's the fix?

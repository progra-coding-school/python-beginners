# Program Code: OUT-UN-03
# Title: Strings vs Numbers in Output
# Cognitive Skill: Understanding
# Topic: Output in Python

# "5" is NOT the same as 5 in Python.
# Understanding this prevents many common bugs!

print("=== String '5' vs Number 5 ===")
print("5")     # string — just the character 5
print(5)       # integer — the number five
print(type("5"))   # <class 'str'>
print(type(5))     # <class 'int'>

print()

print("=== Addition: very different results! ===")
# Number + Number = math
print(5 + 5)           # 10  (arithmetic)

# String + String = joining (concatenation)
print("5" + "5")       # "55"  (joined text)

print()

print("=== You CANNOT mix string and number with + ===")
# print("5" + 5)   ← TypeError!  Cannot add str and int
# Fix option 1: convert number to string
print("Score: " + str(85))      # "Score: 85"

# Fix option 2: use comma (automatic space added)
print("Score:", 85)              # Score: 85

# Fix option 3: use f-string (best!)
score = 85
print(f"Score: {score}")         # Score: 85

print()

print("=== Arithmetic inside print ===")
print(100 + 200)        # 300  (math)
print("100" + "200")    # 100200  (text join)
print("100 + 200")      # 100 + 200 (just text, no calculation)
print(f"100 + 200 = {100 + 200}")   # 100 + 200 = 300

print()

print("=== Real-life: price display ===")
price = 149
quantity = 3

# BAD: mixing types causes error
# total_text = "Total: Rs." + price * quantity   ← TypeError

# GOOD approaches:
print("Total: Rs." + str(price * quantity))       # str() converts number
print("Total: Rs.", price * quantity)             # comma handles it
print(f"Total: Rs.{price * quantity}")            # f-string (cleanest)

# Think:
# 1. What does print("3" * 4) display? What about print(3 * 4)?
# 2. Why can't you do "Age: " + 13 directly? What's the fix?

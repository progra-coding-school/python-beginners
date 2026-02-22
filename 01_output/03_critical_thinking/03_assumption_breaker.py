# Program Code: OUT-CT-03
# Title: Assumption Breaker — Output
# Cognitive Skill: Critical Thinking (Assumption Breaking)
# Topic: Output in Python

# Common wrong assumptions about print() — let's break them!

print("=== Assumption Breaker — Output ===")
print()

# --- Assumption 1 ---
print("Assumption 1: 'print() always puts items on separate lines'")
print("A", end=" ")
print("B", end=" ")
print("C")
print("WRONG! Default is a new line, but end='' changes that.")
print("       A B C all appeared on ONE line above!")
print()

# --- Assumption 2 ---
print("Assumption 2: '\"5\" + \"5\" = 10'")
result = "5" + "5"
print(f'  "5" + "5" = {result}')
print("WRONG! Both are strings — + joins them. Result is '55', not 10.")
print("       For math: use 5 + 5 (no quotes) → 10")
print()

# --- Assumption 3 ---
print("Assumption 3: 'print() returns the value it prints'")
x = print("Watch this!")
print(f"  print() returned: {x}")
print("WRONG! print() always returns None.")
print("       It shows output on screen, but gives nothing back.")
print()

# --- Assumption 4 ---
print("Assumption 4: 'Single and double quotes are different types'")
a = 'Hello'
b = "Hello"
print(f"  'Hello' == \"Hello\" → {a == b}")
print(f"  type('Hello') → {type(a)}")
print(f"  type(\"Hello\") → {type(b)}")
print("WRONG! Both are exactly the same type (str). Quotes are just style.")
print()

# --- Assumption 5 ---
print("Assumption 5: 'print(5/2) shows 2'")
print(f"  print(5/2) → {5/2}")
print("WRONG! / always gives a float. 5/2 = 2.5, not 2.")
print("       Use 5//2 for integer division → 2")
print()

# --- Assumption 6 ---
print("Assumption 6: 'You can print a variable without defining it first'")
try:
    print(unknown_variable)
except NameError as e:
    print(f"  Error: {e}")
print("WRONG! You must define a variable before using it in print().")
print("       Python reads top to bottom — it must see the assignment first.")
print()

# Think:
# 1. What is printed by: print("10" * 3)? Is it 30 or "101010"?
# 2. What would happen if you did: print() + "hello"?

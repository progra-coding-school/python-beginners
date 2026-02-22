# Program Code: OUT-UN-02
# Title: How print() Works Internally
# Cognitive Skill: Understanding
# Topic: Output in Python

# When Python runs print(), here is what happens step by step:
# 1. Python evaluates the argument(s) inside the ()
# 2. Converts everything to text (string form)
# 3. Sends it to the console (screen)
# 4. Adds a newline at the end (by default)
# 5. Returns None (print gives back nothing)

# --- Step 1: Python evaluates first, then prints ---
print(5 + 3)        # evaluates 5+3=8, then prints 8
print(10 * 4)       # evaluates 10*4=40, then prints 40
print(2 ** 10)      # evaluates 2^10=1024, then prints 1024

print()

# --- Step 2: Everything becomes text to display ---
print(100)          # integer 100 → text "100" on screen
print(3.14)         # float 3.14 → text "3.14" on screen
print(True)         # boolean True → text "True" on screen

print()

# --- Step 3: Each print() sends a new line at the end ---
print("Line A")     # prints Line A, then jumps to next line
print("Line B")     # prints on the NEXT line
print("Line C")

print()

# --- What 'end' really means ---
print("A", end="")  # no newline after A
print("B", end="")  # B appears right after A
print("C")          # C appears right after B, then a newline
# Result: ABC

print()

# --- print() returns None ---
result = print("Watch this!")    # print() shows output but returns nothing
print("Return value of print:", result)    # None

print()

# --- Evaluating expressions INSIDE print ---
a = 10
b = 3
print("Sum:", a + b)            # a+b computed first → 13
print("String:", "a" + "b")     # "a"+"b" = "ab" (joining strings)
print("Repeated:", "-" * 15)    # "-" × 15 → "---------------"

# Think:
# 1. What is printed by: result = print("Hi")  then  print(result)?
# 2. Does print("5" + "3") print 8 or 53? Why?

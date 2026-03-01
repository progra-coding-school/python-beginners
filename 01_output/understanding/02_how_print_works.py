# How print() Works Internally
# When Python runs print(), 5 things happen in order:
# 1. Evaluate the arguments inside (). 2. Convert to text. 3. Send to screen.
# 4. Add a newline at the end. 5. Return None (print gives back nothing).

# --- Step 1: Python evaluates first, then prints ---
# The expression inside () is fully computed BEFORE anything is displayed
print(5 + 3)        # evaluates 5+3=8, then prints 8
print(10 * 4)       # evaluates 10*4=40, then prints 40
print(2 ** 10)      # evaluates 2^10=1024, then prints 1024

print()

# --- Step 2: Everything becomes text to display ---
# Python converts all data types to their text representation before showing them
print(100)          # integer 100 → text "100" on screen
print(3.14)         # float 3.14 → text "3.14" on screen
print(True)         # boolean True → text "True" on screen

print()

# --- Step 3: Each print() sends a new line at the end ---
# After printing, Python moves the cursor to the START of the next line
print("Line A")     # prints Line A, then moves to next line
print("Line B")     # prints on the NEXT line
print("Line C")

print()

# --- What 'end' really means ---
# By default end="\n" (newline). Setting end="" keeps everything on the same line.
print("A", end="")  # no newline after A — cursor stays on same line
print("B", end="")  # B appears right after A
print("C")          # C appears right after B, then a newline
# Result: ABC

print()

# --- print() returns None ---
# print() is a procedure — it does work (shows output) but gives nothing back
result = print("Watch this!")    # print() shows output but returns nothing
print("Return value of print:", result)    # None

print()

# --- Evaluating expressions INSIDE print ---
# Strings join with +; strings repeat with *; numbers compute with arithmetic
a = 10
b = 3
print("Sum:", a + b)            # a+b computed first → 13
print("String:", "a" + "b")     # "a"+"b" = "ab" (joining two strings, not adding numbers)
print("Repeated:", "-" * 15)    # "-" × 15 → "---------------"

# Think:
# 1. What is printed by: result = print("Hi")  then  print(result)?
# 2. Does print("5" + "3") print 8 or 53? Why?

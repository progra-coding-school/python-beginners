# Program Code: LP-CT-03
# Title: Assumption Breaker — Loops
# Cognitive Skill: Critical Thinking (Assumption Breaking)
# Topic: Loops in Python

# Common wrong assumptions about loops — let's break them!

print("=== Assumption Breaker — Loops ===")
print()

# --- Assumption 1 ---
print("Assumption 1: 'range(10) gives 1 to 10'")
print("range(10) actually gives:", list(range(10)))
print("WRONG! range(n) starts at 0 and goes up to n-1.")
print("For 1 to 10 you need: range(1, 11)")
print()

# --- Assumption 2 ---
print("Assumption 2: 'The loop variable keeps its value after the loop ends'")
for i in range(5):
    pass    # do nothing, just loop
print(f"After the loop, i = {i}")
print("Surprise! i = 4 — Python keeps the LAST value of the loop variable.")
print("But don't rely on this — it's unclear and confusing to read.")
print()

# --- Assumption 3 ---
print("Assumption 3: 'break exits the entire program'")
print("Looping:")
for i in range(1, 6):
    if i == 3:
        break
    print(f"  i = {i}")
print("After break, code continues HERE — break only exits the LOOP, not the program.")
print()

# --- Assumption 4 ---
print("Assumption 4: 'continue skips the rest of the program'")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"  i = {i}")
print("continue only skips the REST of the current ITERATION — loop keeps going.")
print()

# --- Assumption 5 ---
print("Assumption 5: 'Changing the list inside a for loop is safe'")
numbers = [1, 2, 3, 4, 5]
# BAD — modifying while looping can skip items or behave unexpectedly
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print("After removing evens (BAD way):", numbers)
print("Surprise! 4 was NOT removed — modifying a list while looping over it skips items!")
print("Safe way: loop over a COPY, or build a new list")
numbers2 = [1, 2, 3, 4, 5]
result = [n for n in numbers2 if n % 2 != 0]
print("Safe result:", result)
print()

# --- Assumption 6 ---
print("Assumption 6: 'A while loop always runs at least once'")
x = 10
while x < 5:
    print("This runs!")
    x += 1
print("Output: (nothing) — while checks the condition BEFORE the first run.")
print("If condition is False from the start → loop body never executes.")

# Think:
# 1. How would you print numbers 1 to 10 using range()? Write the exact call.
# 2. What happens if you write: for i in range(0): print(i)?

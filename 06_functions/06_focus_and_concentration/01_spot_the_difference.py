# Program Code: FN-FC-01
# Title: Spot the Difference — Functions
# Cognitive Skill: Focus and Concentration (Attention to Detail)
# Topic: Functions in Python

# Each pair looks almost the same — but produces DIFFERENT results.
# Look carefully!

score = 0

print("=== Spot the Difference — Functions ===")
print()

# --- Round 1 ---
print("Round 1:")
print("  Code A: def greet(): print('Hello')")
print("  Code B: def greet(): return 'Hello'")
answer = input("What is different? ")
print("Answer: A prints 'Hello' but returns None.")
print("         B returns 'Hello' but prints nothing.")
print("         result = greet()  →  A gives None, B gives 'Hello'")
score += 1
print()

# --- Round 2 ---
print("Round 2:")
print("  Code A: def add(a, b):  return a + b")
print("  Code B: def add(a, b=5): return a + b")
answer = input("What is different? ")
print("Answer: B has a DEFAULT value for b.")
print("         add(3)    → A: Error (missing b). B: 8 (uses b=5)")
print("         add(3, 2) → Both give 5")
score += 1
print()

# --- Round 3 ---
print("Round 3:")
print("  Code A: def multiply(n):")
print("               n = n * 2")
print()
print("  Code B: def multiply(n):")
print("               return n * 2")
answer = input("What does multiply(5) return in each? ")
def multiply_a(n):
    n = n * 2  # changes local n but returns nothing
def multiply_b(n):
    return n * 2
print(f"Answer: A returns {multiply_a(5)} (None — no return!)")
print(f"         B returns {multiply_b(5)}")
score += 1
print()

# --- Round 4 ---
print("Round 4:")
print("  Code A: def show(name, age):")
print("               print(name, age)")
print("  show('Aarav', 13)")
print()
print("  Code B: def show(name, age):")
print("               print(name, age)")
print("  show(13, 'Aarav')")
answer = input("What is different? ")
print("Answer: A prints: Aarav 13  (correct order)")
print("         B prints: 13 Aarav  (wrong order — arguments are positional!)")
score += 1
print()

# --- Round 5 ---
print("Round 5:")
print("  Code A:")
print("    def outer():")
print("        x = 10")
print("        return x")
print("    print(x)         ← after calling outer()")
print()
print("  Code B:")
print("    x = 10")
print("    def outer():")
print("        return x")
print("    print(outer())   ← after calling outer()")
answer = input("What is different? ")
print("Answer: A gives NameError — x is LOCAL to outer(), not accessible outside.")
print("         B works — x is GLOBAL (defined outside), accessible inside the function.")
score += 1
print()

# --- Round 6 ---
print("Round 6:")
print("  Code A: def calc(n): return n * 2 + 1")
print("  Code B: def calc(n): return n * (2 + 1)")
answer = input("calc(5) — what does each return? ")
def calc_a(n): return n * 2 + 1
def calc_b(n): return n * (2 + 1)
print(f"Answer: A = {calc_a(5)} (5*2=10, then +1=11)")
print(f"         B = {calc_b(5)} (2+1=3, then 5*3=15)")
print("         Operator precedence changes everything!")
score += 1
print()

print(f"Score: {score} / 6")

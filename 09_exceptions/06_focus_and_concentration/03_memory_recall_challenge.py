# Program Code: EX-FC-03
# Title: Memory Recall Challenge
# Cognitive Skill: Focus and Concentration
# Topic: Exceptions in Python

# Study the exception reference table for 30 seconds.
# Then answer the questions from memory and verify.

# ─── Memorise this table ─────────────────────────────────────────
exception_table = [
    ("ValueError",        "Right type, wrong value",       "int('abc')"),
    ("TypeError",         "Wrong type for operation",      "'a' + 1"),
    ("ZeroDivisionError", "Divide or mod by zero",         "10 / 0"),
    ("IndexError",        "List index out of range",       "lst[99]"),
    ("KeyError",          "Dict key not found",            "d['x']"),
    ("NameError",         "Variable not defined",          "print(xyz)"),
    ("AttributeError",    "No such method/attribute",      "42.append()"),
    ("RecursionError",    "Stack overflow from recursion", "f() calls f()"),
]

print("=== Exception Reference Table (study for 30 seconds) ===")
print(f"  {'Exception':<22} {'Cause':<35} {'Example'}")
print(f"  {'─'*22} {'─'*35} {'─'*20}")
for name, cause, example in exception_table:
    print(f"  {name:<22} {cause:<35} {example}")

print()
print("─" * 70)
print("Answer from memory — then verify below!")
print("─" * 70)
print()

# --- Q1: What exception does int("abc") raise? ---
try:
    int("abc")
except Exception as e:
    print(f"Q1: int('abc')     → {type(e).__name__}")

# --- Q2: What exception does lst[99] raise? ---
try:
    [1, 2][99]
except Exception as e:
    print(f"Q2: [1,2][99]      → {type(e).__name__}")

# --- Q3: What exception does 'a' + 1 raise? ---
try:
    "a" + 1
except Exception as e:
    print(f"Q3: 'a' + 1        → {type(e).__name__}")

# --- Q4: What exception does d['missing'] raise? ---
try:
    {"a": 1}["b"]
except Exception as e:
    print(f"Q4: d['missing']   → {type(e).__name__}")

# --- Q5: What exception does 10 / 0 raise? ---
try:
    10 / 0
except Exception as e:
    print(f"Q5: 10 / 0         → {type(e).__name__}")

# --- Q6: What exception does 42.append(1) raise? ---
try:
    (42).bit_length()   # exists
    (42).append(1)      # doesn't exist
except Exception as e:
    print(f"Q6: 42.append(1)   → {type(e).__name__}")

# --- Q7: What exception does print(undefined) raise? ---
try:
    exec("print(undefined_xyz)")
except Exception as e:
    print(f"Q7: print(undefined) → {type(e).__name__}")

print()
print("─" * 70)
print("Score yourself:")
print("  7/7 → Exceptional focus!")
print("  5-6 → Great — a couple need review.")
print("  3-4 → Re-read the table, then test again.")
print("  0-2 → Study each row one at a time with an example.")

# Think:
# 1. Which two exception types are most commonly confused with each other?
# 2. If you could only remember 3 exception types for everyday coding, which 3 would you pick?

# Program Code: EX-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking
# Topic: Exceptions in Python

# Common wrong beliefs about exceptions.
# Run each block to BUST or CONFIRM the assumption.

# --- Assumption 1: "try/except slows my whole program down" ---
print("=== Assumption 1: try/except is always slow ===")
print("BUSTED: try blocks have near-zero overhead when no exception occurs.")
print("Python only does extra work WHEN an exception is raised — not every time.")
total = 0
for i in range(100_000):
    try:
        total += i   # no exception — very fast
    except:
        pass
print(f"  Summed 0–99999 = {total} (try block ran 100,000 times, very fast)\n")

# --- Assumption 2: "except catches all exceptions including syntax errors" ---
print("=== Assumption 2: except catches everything including SyntaxError ===")
print("BUSTED: SyntaxError is caught at COMPILE time, before try/except runs.")
print("  You cannot catch a SyntaxError in the same file where it occurs.")
try:
    exec("x = ")      # exec lets us test a syntax error at runtime
except SyntaxError as e:
    print(f"  SyntaxError caught via exec(): {e}")
print("  Note: you CAN catch SyntaxError when executing code dynamically (exec/eval).\n")

# --- Assumption 3: "finally only runs if no exception occurs" ---
print("=== Assumption 3: finally only runs on success ===")
print("BUSTED: finally ALWAYS runs — success or failure.")
for val in ["5", "abc"]:
    try:
        n = int(val)
        print(f"  Success: {n}")
    except ValueError:
        print(f"  Failed: '{val}' is not an int")
    finally:
        print(f"  [finally] always executed for '{val}'")
print()

# --- Assumption 4: "You can only catch one exception type per except" ---
print("=== Assumption 4: One exception type per except ===")
print("BUSTED: Use a tuple to catch multiple types in one block.")
for val in ["hello", None, "0"]:
    try:
        result = 10 / int(val)
        print(f"  Result for {val!r}: {result:.2f}")
    except (ValueError, TypeError, ZeroDivisionError) as e:
        print(f"  Caught for {val!r}: {type(e).__name__}: {e}")
print()

# --- Assumption 5: "return in try block prevents finally from running" ---
print("=== Assumption 5: return skips finally ===")
def test():
    try:
        return "from try"
    finally:
        print("  [finally] runs even before return!")

result = test()
print(f"  Return value: {result}")
print("BUSTED: finally runs BEFORE the function actually returns.\n")

# --- Assumption 6: "Exceptions should be used for all error checking" ---
print("=== Assumption 6: Always use exceptions for errors ===")
print("BUSTED: Use if/else when checking EXPECTED conditions.")
print("  Use exceptions for UNEXPECTED or EXCEPTIONAL situations.")
print("  Example: checking if a list is empty → use 'if not lst'")
print("  Example: parsing unknown user input → use try/except")
print("  Exceptions are for surprises. if/else is for known possibilities.")

# Think:
# 1. Give one example where `if/else` is better than `try/except`.
# 2. Give one example where `try/except` is better than `if/else`.

# Program Code: EX-LR-01
# Title: Trace the Exception
# Cognitive Skill: Logical Reasoning
# Topic: Exceptions in Python

# Read each block carefully.
# PREDICT what will be printed BEFORE running it.
# Trace the flow: which lines run, which are skipped?

# --- Trace 1 ---
print("=== Trace 1 ===")
try:
    print("A")
    x = 1 / 0          # exception here
    print("B")         # skipped?
except ZeroDivisionError:
    print("C")
print("D")
# Predict the output: ?
# Actual: A  C  D   (B is skipped; D runs because it's outside try/except)

print()

# --- Trace 2 ---
print("=== Trace 2 ===")
try:
    print("A")
    x = int("42")       # no exception
    print("B")
except ValueError:
    print("C")         # skipped?
else:
    print("D")
finally:
    print("E")
# Predict: ?
# Actual: A  B  D  E   (C skipped; else runs because no exception; finally always runs)

print()

# --- Trace 3 ---
print("=== Trace 3 ===")
try:
    print("A")
    x = int("bad")      # ValueError raised
    print("B")
except ValueError:
    print("C")
else:
    print("D")         # skipped?
finally:
    print("E")
# Predict: ?
# Actual: A  C  E   (B skipped; D skipped because exception occurred; E always runs)

print()

# --- Trace 4 ---
print("=== Trace 4 ===")
def risky():
    print("  risky: start")
    raise ValueError("oops")
    print("  risky: end")    # never reached

try:
    risky()
    print("after risky()")   # never reached
except ValueError as e:
    print(f"caught: {e}")
# Predict: ?
# Actual: "risky: start"  then  "caught: oops"

print()

# --- Trace 5 (tricky!) ---
print("=== Trace 5 ===")
for i in [2, 0, 4]:
    try:
        print(f"  10 / {i} = {10 / i:.1f}")
    except ZeroDivisionError:
        print(f"  Skip {i}")
print("  Done")
# Predict each iteration: ?
# Actual: 10/2=5.0 | Skip 0 | 10/4=2.5 | Done

# Think:
# 1. In Trace 2, why does the `else` block run but not in Trace 3?
# 2. In Trace 5, does the loop stop when i=0? Why or why not?

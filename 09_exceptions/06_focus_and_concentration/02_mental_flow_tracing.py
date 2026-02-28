# Program Code: EX-FC-02
# Title: Mental Flow Tracing
# Cognitive Skill: Focus and Concentration
# Topic: Exceptions in Python

# For each block, trace the execution path in your head.
# Mark each line as: RUN / SKIP / MAYBE.
# Then run to verify.

print("=== Flow Tracing Exercises ===\n")

# --- Exercise 1 ---
print("Exercise 1: which lines print?")
print("Lines: A, try-open, B, except, C, finally, D")
print()
try:
    print("  A")             # RUN or SKIP?
    x = int("5")             # succeeds
    print("  B")             # RUN or SKIP?
except ValueError:
    print("  C")             # RUN or SKIP?
finally:
    print("  D")             # RUN or SKIP?
# Answer: A, B, D   (no exception so C is skipped; D always runs)

print()

# --- Exercise 2 ---
print("Exercise 2: which lines print?")
try:
    print("  P")
    y = int("oops")          # raises ValueError
    print("  Q")             # RUN or SKIP?
except ValueError:
    print("  R")
except TypeError:
    print("  S")             # RUN or SKIP?
else:
    print("  T")             # RUN or SKIP?
finally:
    print("  U")
# Answer: P, R, U   (Q skipped after error; S skipped, ValueError handled first; T skipped because exception occurred)

print()

# --- Exercise 3 ---
print("Exercise 3: loop with exceptions")
results = []
for val in [2, 0, "x", 4]:
    try:
        results.append(10 // int(val))
    except (ZeroDivisionError, ValueError):
        results.append(None)
print("  results:", results)
# Trace:
#   val=2 → 10//2=5         → [5]
#   val=0 → ZeroDivisionError → [5, None]
#   val='x' → int('x') ValueError → [5, None, None]
#   val=4 → 10//4=2         → [5, None, None, 2]
# Answer: [5, None, None, 2]

print()

# --- Exercise 4: return inside try ---
print("Exercise 4: does finally run before return?")
def check(val):
    try:
        n = int(val)
        return n * 2         # return here
    except ValueError:
        return -1
    finally:
        print("  [finally] always runs")

result = check("7")
print("  result:", result)
# Answer: finally prints first, then result is 14

print()

# --- Exercise 5: nested try ---
print("Exercise 5: nested try")
try:
    try:
        raise ValueError("inner error")
    except TypeError:
        print("  inner except TypeError")   # RUN or SKIP?
    print("  after inner try")              # RUN or SKIP?
except ValueError as e:
    print(f"  outer except: {e}")
# Answer: inner TypeError is skipped; ValueError bubbles to outer → "outer except: inner error"

# Think:
# 1. In Exercise 5, why does the ValueError reach the outer except?
# 2. In Exercise 4, what would happen if the finally block raised its own exception?

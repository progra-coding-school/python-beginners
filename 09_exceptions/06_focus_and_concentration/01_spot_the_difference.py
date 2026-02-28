# Program Code: EX-FC-01
# Title: Spot the Difference
# Cognitive Skill: Focus and Concentration
# Topic: Exceptions in Python

# Two versions of similar code are shown.
# Find every difference — some are bugs, some are style choices.

# ─── Pair 1 ─────────────────────────────────────────────────────
print("=== Pair 1 ===")

# Version A — catches the right exception
try:
    n = int("hello")
except ValueError as e:
    print("A: ValueError:", e)

# Version B — catches the wrong exception (never triggered)
try:
    n = int("hello")
except TypeError as e:
    print("B: TypeError:", e)
except ValueError as e:
    print("B: ValueError:", e)   # this one will trigger
# Difference: A catches only ValueError. B has both but also tries TypeError first.
# Both catch the error, but B has an unnecessary block.

print()

# ─── Pair 2 ─────────────────────────────────────────────────────
print("=== Pair 2 ===")

# Version A — finally runs
try:
    x = 10 / 2
except ZeroDivisionError:
    print("A: zero!")
finally:
    print("A: finally")

# Version B — no finally
try:
    x = 10 / 2
except ZeroDivisionError:
    print("B: zero!")
print("B: after block")
# Difference: A's "finally" always runs even if exception occurs.
# B's "after block" only runs if the try completes normally OR except handles it.

print()

# ─── Pair 3 ─────────────────────────────────────────────────────
print("=== Pair 3 ===")

data = {"name": "Aarav"}

# Version A — safe with .get()
print("A:", data.get("age", "N/A"))

# Version B — try/except
try:
    print("B:", data["age"])
except KeyError:
    print("B: N/A")
# Difference: A is concise (one line); B is verbose but more explicit.
# Both produce same result. A is preferred for simple dict access.

print()

# ─── Pair 4 ─────────────────────────────────────────────────────
print("=== Pair 4 ===")

# Version A — specific exception
try:
    result = 1 / 0
except ZeroDivisionError:
    print("A: division by zero")

# Version B — bare except (catches everything)
try:
    result = 1 / 0
except:
    print("B: something failed")
# Difference: A names the exception (good). B uses bare except (bad practice).
# Bare except also catches SystemExit, KeyboardInterrupt — can hide serious problems.

print()

# ─── Pair 5 ─────────────────────────────────────────────────────
print("=== Pair 5 ===")

# Version A — else block
try:
    val = int("42")
except ValueError:
    print("A: parse error")
else:
    print("A: parsed OK:", val)

# Version B — result inside try
try:
    val = int("42")
    print("B: parsed OK:", val)    # runs only if int() succeeds
except ValueError:
    print("B: parse error")
# Difference: A uses else (more explicit). B puts success code inside try.
# Both work; A makes the success path clearer.

# Think:
# 1. In Pair 4, why is a bare except considered bad practice?
# 2. In Pair 5, is there any case where A and B behave differently?

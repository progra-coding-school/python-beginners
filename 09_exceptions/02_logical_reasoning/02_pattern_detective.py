# Program Code: EX-LR-02
# Title: Pattern Detective
# Cognitive Skill: Logical Reasoning
# Topic: Exceptions in Python

# Spot the pattern in each exception-handling block.
# Name it, then complete the missing piece.

# --- Pattern 1: Input loop until valid ---
print("=== Pattern 1: Retry until valid ===")
# Simulated inputs
simulated = iter(["abc", "-5", "7"])

value = None
while value is None:
    raw = next(simulated)
    try:
        n = int(raw)
        if n < 1:
            raise ValueError("Must be positive")
        value = n
    except ValueError as e:
        print(f"  '{raw}' rejected: {e} — try again")

print(f"  Accepted: {value}")
print("Pattern: while loop + try/except = keep asking until input is valid")

print()

# --- Pattern 2: Collect valid, skip invalid ---
print("=== Pattern 2: Filter bad data ===")
raw_scores = ["85", "abc", "92", "-1", "78", "200", "60"]
valid_scores = []

for s in raw_scores:
    try:
        n = int(s)
        if not (0 <= n <= 100):
            raise ValueError("Out of range")
        valid_scores.append(n)
    except ValueError:
        pass    # silently skip bad entries

print(f"  Valid scores: {valid_scores}")
print("Pattern: try/except inside a loop skips bad items and collects good ones")

print()

# --- Pattern 3: Default value on failure ---
print("=== Pattern 3: Return a safe default ===")
def safe_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default

tests = ["42", "abc", "", "7", "??"]
for t in tests:
    print(f"  safe_int('{t}') = {safe_int(t, default=-1)}")
print("Pattern: try/except returns a fallback when parsing fails")

print()

# --- Pattern 4: Translate exceptions for the caller ---
print("=== Pattern 4: Wrap and re-raise ===")
class DataError(Exception):
    pass

def load_score(raw):
    try:
        return int(raw)
    except ValueError:
        raise DataError(f"Invalid score data: '{raw}'")   # translate error type

for val in ["88", "oops"]:
    try:
        score = load_score(val)
        print(f"  Loaded: {score}")
    except DataError as e:
        print(f"  DataError: {e}")
print("Pattern: catch low-level error, raise high-level custom exception")

# Think:
# 1. In Pattern 2, why use `pass` instead of printing an error message?
# 2. In Pattern 4, why would you translate a ValueError to a custom DataError?

# Trace the Set
# Read each block carefully. PREDICT the output BEFORE running it. Then verify!
# Tracing builds the muscle of knowing what code will do without running it.

# --- Trace 1 ---
# Start: {1,2,3,4,5}. add(3) → ignored (duplicate). add(6) → grows. discard(2) → removed.
print("Trace 1:")
s = {1, 2, 3, 4, 5}
s.add(3)        # already in set — no change
s.add(6)        # new item added
s.discard(2)    # 2 removed
print(len(s))
# Predicted: ?
# Actual   : 5  (original 5, +6, -2 = 5; 3 ignored as duplicate)

print()

# --- Trace 2 ---
# Trace each operator: & = both, | = either, - = only in left
print("Trace 2:")
a = {"x", "y", "z"}
b = {"y", "z", "w"}
print(a & b)
print(a | b)
print(a - b)
# Predicted (& ): ?   → {'y', 'z'}
# Predicted (| ): ?   → {'x', 'y', 'z', 'w'}
# Predicted (- ): ?   → {'x'}

print()

# --- Trace 3 ---
# set() strips duplicates; sorted() gives alphabetical order for clean display
print("Trace 3:")
items = ["pen", "book", "pen", "ruler", "book", "pen"]
unique = set(items)
print(len(unique))
print(sorted(unique))
# Predicted len    : ?   → 3
# Predicted sorted : ?   → ['book', 'pen', 'ruler']

print()

# --- Trace 4 ---
# Set comprehension {expr for var in set if condition} — builds a new set from an old one
print("Trace 4:")
nums = {10, 20, 30, 40, 50}
result = {n for n in nums if n > 25}
print(result)
# Predicted: ?
# Actual   : {30, 40, 50}

print()

# --- Trace 5 ---
# Union first joins both sets; then discard("Diya") removes from the result
print("Trace 5:")
class_a = {"Aarav", "Diya", "Karthik"}
class_b = {"Diya", "Riya"}
class_c = class_a | class_b     # union → {"Aarav", "Diya", "Karthik", "Riya"}
class_c.discard("Diya")         # remove Diya from the result
print(sorted(class_c))
# Predicted: ?
# Actual   : ['Aarav', 'Karthik', 'Riya']

# Think:
# 1. In Trace 1, why didn't adding 3 increase the length?
# 2. In Trace 4, what is this called — set comprehension. Can you write one for even numbers?

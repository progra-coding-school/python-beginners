# Program Code: TU-UN-02
# Title: How Tuples Work Internally
# Cognitive Skill: Understanding
# Topic: Tuples in Python

# --- Immutability means the REFERENCE is fixed ---
print("=== Immutability — the container is locked ===")
t = (1, 2, 3)
print("Tuple:", t)

# Cannot change, add, or remove elements
try:
    t[0] = 99
except TypeError as e:
    print("Change element  → TypeError:", e)

try:
    t.append(4)
except AttributeError as e:
    print("append()        → AttributeError:", e)

print()

# --- But a mutable object INSIDE a tuple CAN change ---
print("=== Mutable items inside a tuple can still change! ===")
# The tuple reference to the list is fixed — but the LIST itself is mutable
mixed = (1, [10, 20, 30], "hello")
print("Before:", mixed)
mixed[1].append(40)         # modifying the LIST inside the tuple — allowed!
mixed[1][0] = 99            # also allowed
print("After :", mixed)
# The tuple didn't change — the LIST inside it did.
print("Why? The tuple still holds the SAME list object. The list changed, not the tuple.")

print()

# --- Tuples are hashable (if all items are hashable) ---
print("=== Tuples as dictionary keys ===")
t1 = (1, 2)
print("hash((1, 2)) =", hash(t1))    # works!

t2 = (1, [2, 3])                     # contains a list — not hashable
try:
    print(hash(t2))
except TypeError as e:
    print("hash of tuple with list → TypeError:", e)

print()

# --- Memory: tuples use less memory than lists ---
print("=== Memory comparison ===")
import sys
a_list  = [1, 2, 3, 4, 5]
a_tuple = (1, 2, 3, 4, 5)
print(f"List  size: {sys.getsizeof(a_list)} bytes")
print(f"Tuple size: {sys.getsizeof(a_tuple)} bytes")
print("Tuples are more memory-efficient than lists!")

print()

# --- Tuples are iterable just like lists ---
print("=== Looping over a tuple ===")
rgb = (255, 128, 0)
channels = ("Red", "Green", "Blue")
for name, value in zip(channels, rgb):
    print(f"  {name}: {value}")

# Think:
# 1. If a list INSIDE a tuple can change, is the tuple truly immutable? Explain.
# 2. Why does saving memory matter in programs that handle millions of records?

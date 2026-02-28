# Program Code: TU-CT-03
# Title: Assumption Breaker
# Cognitive Skill: Critical Thinking
# Topic: Tuples in Python

# Common wrong beliefs about tuples.
# Run each block to BUST or CONFIRM it.

# --- Assumption 1: "(42) creates a tuple" ---
print("=== Assumption 1: (42) is a tuple ===")
t1 = (42)
print("type((42))  :", type(t1))     # int!
t2 = (42,)
print("type((42,)) :", type(t2))     # tuple
print("BUSTED: Parentheses alone don't make a tuple. The COMMA does!\n")

# --- Assumption 2: "Tuples are completely immutable — nothing inside can change" ---
print("=== Assumption 2: Nothing inside a tuple can ever change ===")
t = ([1, 2], [3, 4])
print("Before:", t)
t[0].append(99)     # modifying the LIST inside the tuple
print("After :", t)
print("BUSTED: The tuple's references are fixed, but mutable objects inside CAN change.\n")

# --- Assumption 3: "You can't sort a tuple" ---
print("=== Assumption 3: Can't sort a tuple ===")
t = (3, 1, 4, 1, 5, 9)
result = sorted(t)
print("sorted(tuple) returns:", result, "| type:", type(result))
print("CONFIRMED WRONG: sorted() works on tuples — it returns a new LIST.\n")

# --- Assumption 4: "Tuples are just slower lists" ---
print("=== Assumption 4: Tuples are just slower lists ===")
import sys
a_list  = [1, 2, 3, 4, 5]
a_tuple = (1, 2, 3, 4, 5)
print(f"List  size: {sys.getsizeof(a_list)} bytes")
print(f"Tuple size: {sys.getsizeof(a_tuple)} bytes")
print("BUSTED: Tuples use LESS memory and can be faster to iterate.")
print("  They also have semantic meaning — 'this is fixed data'.\n")

# --- Assumption 5: "Empty tuple and single-item tuple are the same" ---
print("=== Assumption 5: () and (x,) behave the same ===")
empty  = ()
single = (42,)
print("Empty  ()   len:", len(empty),  "| type:", type(empty))
print("Single (42,) len:", len(single), "| type:", type(single))
print("BUSTED: () is empty (len 0). (42,) has one item (len 1). Very different!\n")

# --- Assumption 6: "Tuples can't be used in a for loop" ---
print("=== Assumption 6: Can't iterate over a tuple ===")
colours = ("red", "green", "blue")
for colour in colours:
    print(" ", colour)
print("BUSTED: Tuples are fully iterable — for loops work perfectly.\n")

# Think:
# 1. Which assumption surprised you most? Why?
# 2. If a list inside a tuple can change, how does that affect using the tuple as a dict key?

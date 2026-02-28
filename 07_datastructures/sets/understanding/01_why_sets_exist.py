# Program Code: SE-UN-01
# Title: Why Sets Exist
# Cognitive Skill: Understanding
# Topic: Sets in Python

# WITHOUT a set: duplicates pile up. Checking membership is slow.
# WITH a set: duplicates are impossible. Membership check is instant.

# --- Problem 1: Finding unique visitors to a website ---
print("=== WITHOUT a set — tracking unique visitors ===")

visitors_log = ["Aarav", "Diya", "Aarav", "Karthik", "Diya", "Riya", "Aarav"]

unique_visitors_list = []
for name in visitors_log:
    if name not in unique_visitors_list:    # must scan the whole list every time
        unique_visitors_list.append(name)

print("Log         :", visitors_log)
print("Unique (list):", unique_visitors_list)
print("Total visits :", len(visitors_log), " | Unique:", len(unique_visitors_list))

print()

print("=== WITH a set — unique visitors instantly ===")
unique_visitors_set = set(visitors_log)     # duplicates gone automatically
print("Unique (set) :", unique_visitors_set)
print("Unique count :", len(unique_visitors_set))
print("One line. No loop. No manual check!")

print()

# --- Problem 2: Checking if an item exists ---
print("=== Membership check — list vs set ===")
import time

big_list = list(range(100_000))
big_set  = set(range(100_000))

target = 99_999

# List — scans from the beginning
start = time.perf_counter()
_ = target in big_list
list_time = time.perf_counter() - start

# Set — direct lookup (hash-based)
start = time.perf_counter()
_ = target in big_set
set_time = time.perf_counter() - start

print(f"List lookup time : {list_time:.6f} seconds")
print(f"Set  lookup time : {set_time:.6f} seconds")
print("Sets are MUCH faster for membership checks on large data!")

print()

# --- 3 reasons sets exist ---
print("=== 3 Reasons Sets Exist ===")
print("1. UNIQUE data — duplicates are impossible by design")
print("2. FAST lookup — checking 'in' is near-instant (hashing)")
print("3. MATH operations — union, intersection, difference built-in")

# Think:
# 1. Name two real apps that need to track unique items (no duplicates).
# 2. Why is set lookup faster than list lookup?

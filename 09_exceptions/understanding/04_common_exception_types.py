# Program Code: EX-UN-04
# Title: Common Exception Types — Deep Dive
# Cognitive Skill: Understanding
# Topic: Exceptions in Python

# Know your exceptions: what causes them and how to handle each.

# --- 1. ValueError — right type, wrong value ---
print("=== 1. ValueError ===")
print("Cause: right type but value makes no sense")
tests = ["42", "3.14", "hello", "", "99"]
for s in tests:
    try:
        n = int(s)
        print(f"  int('{s}') = {n}")
    except ValueError:
        print(f"  int('{s}') → ValueError")

print()

# --- 2. TypeError — wrong type entirely ---
print("=== 2. TypeError ===")
print("Cause: operation not supported for the given types")
operations = [
    lambda: "age" + 13,
    lambda: len(42),
    lambda: "hi" * "3",
    lambda: [1, 2] + (3, 4),
]
for op in operations:
    try:
        op()
    except TypeError as e:
        print(f"  TypeError: {e}")

print()

# --- 3. IndexError — list position out of range ---
print("=== 3. IndexError ===")
fruits = ["mango", "banana", "apple"]
for i in [0, 2, 5, -1, -10]:
    try:
        print(f"  fruits[{i}] = {fruits[i]}")
    except IndexError as e:
        print(f"  fruits[{i}] → IndexError: {e}")

print()

# --- 4. KeyError — dict key missing ---
print("=== 4. KeyError ===")
student = {"name": "Aarav", "grade": 7}
for key in ["name", "grade", "age", "city"]:
    try:
        print(f"  student['{key}'] = {student[key]}")
    except KeyError:
        print(f"  student['{key}'] → KeyError (use .get() to avoid this)")

print()

# --- 5. AttributeError — object has no such attribute ---
print("=== 5. AttributeError ===")
try:
    num = 42
    num.append(1)       # integers don't have .append()
except AttributeError as e:
    print(f"  AttributeError: {e}")

print()

# --- 6. NameError — variable not defined ---
print("=== 6. NameError ===")
try:
    print(undefined_var)
except NameError as e:
    print(f"  NameError: {e}")

print()

# --- 7. RecursionError — too deep ---
print("=== 7. RecursionError ===")
def count_forever(n):
    return count_forever(n + 1)     # never stops

try:
    count_forever(0)
except RecursionError as e:
    print(f"  RecursionError: {str(e)[:50]}")

print()
print("=== Quick Reference ===")
print("  ValueError       → valid type, invalid value  (int('abc'))")
print("  TypeError        → wrong type                 ('a' + 1)")
print("  IndexError       → list index out of range    (lst[99])")
print("  KeyError         → dict key missing           (d['x'])")
print("  AttributeError   → no such method/attribute   (42.append())")
print("  NameError        → variable not defined")
print("  ZeroDivisionError→ divide by zero")
print("  RecursionError   → too many nested calls")

# Think:
# 1. What exception would you get from: {1: "a"}[2]?
# 2. What exception would you get from: "hello"[100]?

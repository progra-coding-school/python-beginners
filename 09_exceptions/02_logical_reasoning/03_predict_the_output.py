# Program Code: EX-LR-03
# Title: Predict the Output
# Cognitive Skill: Logical Reasoning
# Topic: Exceptions in Python

# Write your prediction on paper FIRST.
# Then run to verify.

# --- Challenge 1 ---
print("=== Challenge 1 ===")
try:
    print(10 / 2)
    print(10 / 0)
    print(10 / 5)
except ZeroDivisionError:
    print("zero!")
# Predict: ?
# Answer : 5.0  →  zero!   (third print never runs)

print()

# --- Challenge 2 ---
print("=== Challenge 2 ===")
x = "hello"
try:
    print(x.upper())
    print(x[100])
except IndexError:
    print("index out of range")
except AttributeError:
    print("no such method")
# Predict: ?
# Answer : HELLO  →  index out of range

print()

# --- Challenge 3 ---
print("=== Challenge 3 ===")
try:
    result = int("5") + int("3")
except ValueError:
    print("parse error")
else:
    print("result:", result)
finally:
    print("done")
# Predict: ?
# Answer : result: 8  →  done  (else runs; no exception)

print()

# --- Challenge 4 ---
print("=== Challenge 4 ===")
items = [1, 2, 3]
try:
    for i in range(5):
        print(items[i])
except IndexError:
    print("ran out of items")
# Predict: ?
# Answer : 1  2  3  →  ran out of items

print()

# --- Challenge 5 (tricky!) ---
print("=== Challenge 5 ===")
def f():
    try:
        return "try"
    finally:
        print("finally ran")

result = f()
print("result:", result)
# Predict: ?
# Answer : "finally ran"  then  "result: try"
# TRICKY: finally runs even when return is in the try block!

print()

# --- Challenge 6 ---
print("=== Challenge 6 ===")
for val in ["10", "x", "5", "y", "2"]:
    try:
        print(int(val) * 2, end="  ")
    except ValueError:
        print("?", end="  ")
print()
# Predict: ?
# Answer : 20  ?  10  ?  4

# Think:
# 1. In Challenge 5, does the `return` in the try block prevent finally from running?
# 2. In Challenge 4, after the IndexError is caught, does the loop continue?

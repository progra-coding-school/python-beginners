"""1. Creating a Simple Tuple
A tuple is created by putting elements inside round brackets ( ),
separated by commas."""

# A simple tuple with numbers
numbers = (1, 2, 3, 4, 5)

print(numbers)

"""2. Accessing Elements
Tuples are ordered, so you can access elements using
 an index (starting from 0):"""

numbers = (10, 20, 30, 40)

print(numbers[0])   # First element → 10
print(numbers[2])   # Third element → 30
print(numbers[-1])  # Last element → 40

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation
print(tuple1 + tuple2)   # (1, 2, 3, 4, 5, 6)

# Repetition
print(tuple1 * 3)    # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership
print(2 in tuple1)   # True
print(9 not in tuple1)  # True

# Length
print(len(tuple1))   # 3
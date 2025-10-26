A = {1, 2, 3}
A.pop()
print(A)


B = {4, 5, 6}
B.pop()
print(B)


# pop() removes a random element from the set, so the output will have any two of {1,2,3} left.

The discard() method removes an element if it exists, but does not raise an error if the element is missing.


The clear() method empties a set completely, leaving it as an empty set.


Adding 2 again has no effect because sets store only unique values. The output remains {1, 2, 3}.




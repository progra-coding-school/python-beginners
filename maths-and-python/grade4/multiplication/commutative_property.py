'''Changing the order does not change the product
Math:
7 × 8 = 8 × 7
'''

a = 7
b = 8

result1 = a * b
result2 = b * a

print("a × b =", result1)
print("b × a =", result2)

if result1 == result2:
    print("Commutative property verified")

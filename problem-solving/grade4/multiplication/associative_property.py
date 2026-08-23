'''Changing the grouping does not change the product
Math:
(6 × 7) × 5 = 6 × (7 × 5)
'''

a = 6
b = 7
c = 5

result1 = (a * b) * c
result2 = a * (b * c)

print("(a × b) × c =", result1)
print("a × (b × c) =", result2)

if result1 == result2:
    print("Associative property verified")

# Program Code:06-01
# Exercise:operators_precedence.py
# Instructions:

result=5+3*4
print(result)

# Explanation:
# Python follows operator precedence.
# * (multiplication) has higher precedence than + (addition).
# So, Python first calculates 3 * 4 = 12.
# Then it adds 5 + 12 = 17.

result=(5+3)*4
print(result)

# Explanation:
# Parentheses () have highest precedence.
# Inside the parentheses: 5 + 3 = 8.
# Then multiplication: 8 * 4 = 32.


result=((5+3)*4)+8-20+15
print(result)


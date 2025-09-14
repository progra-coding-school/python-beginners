result = 10 + 20 / 5
print(result)

# / (division) has higher precedence than + (addition).
# So in 10 + 20 / 5:
# First, 20 / 5 is calculated → 4.0 (division in Python always returns a float)
# Then, 10 + 4.0 → 14.0

result = (10 + 20) / 5
print(result)

# Parentheses are evaluated first: (10 + 20) → 30
# Then, 30 / 5 → 6.0
# Output:6

result = 10+(6*2)+50/2-8
print(result)

result = (5+6)*2+70*2-8+12/2
print(result)

result=8+8/4/2-3
print(result)
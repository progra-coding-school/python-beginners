# Find LCM of denominators
# Convert fractions
# Subtract numerators
# Keep denominator same
# Simplify if possible
# Example 1/2 - 1/6
# LCM of 2 and 6 = 6
# 3/6-1/6=2/6

a, b = 1, 2
c, d = 1, 6

lcm = b * d  # Grade 4 shortcut

new_a = a * d
new_c = c * b

sum_num = new_a - new_c

print("Sum =", sum_num, "/", lcm)

# Simplifying Fractions
# Simplest form → numerator & denominator have no common factor
# Divide both by HCF
# Example:
# 18/54 → divide by 18 → 1/3

num = 18
den = 54

for i in range(min(num, den), 1, -1):
    if num % i == 0 and den % i == 0:
        num //= i
        den //= i
        break

print("Simplified fraction:", num, "/", den)

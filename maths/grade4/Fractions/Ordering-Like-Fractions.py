# Ordering means arranging
# from:
# smallest → largest
# largest → smallest
# For same denominator → order numerators

fractions = [1, 3, 2]  # numerators
denominator = 4

fractions.sort()
print("Ordered fractions:")
for n in fractions:
    print(n, "/", denominator)

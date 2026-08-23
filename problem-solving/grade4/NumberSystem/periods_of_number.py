'''
Separate Periods (Ones, Thousands, Millions)
'''

number = 893450243
ones = number % 1000
thousands = (number // 1000) % 1000
millions = (number // 1000000) % 1000

print("Number:", number)
print("Millions period:", millions)
print("Thousands period:", thousands)
print("Ones period:", ones)

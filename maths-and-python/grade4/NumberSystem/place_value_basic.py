'''
Find Place Value of Each Digit
'''

number = 1456

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10

print("Number:", number)
print("Thousands:", thousands)
print("Hundreds:", hundreds)
print("Tens:", tens)
print("Ones:", ones)

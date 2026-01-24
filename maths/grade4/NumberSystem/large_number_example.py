'''
Large Number Example
'''

number = 100000000000000

digits = len(str(number))
periods = digits // 3

print("Number:", format(number, ","))
print("Number of digits:", digits)
print("Number of periods:", periods)

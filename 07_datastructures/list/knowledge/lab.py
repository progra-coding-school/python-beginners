
from operator import index

players = ["Aarav", "Diya", "Kabir", "Meera", "Rohan","Messiah","Diya"]
scores  = [88, 45, 92, 67, 78,45,45]

#in
# print("'Kabir' in players:", "Messiah" in players)
# print("'88' in scores:", 88 in scores)

#Index
# print(" Index of any item  players list:", players.index("Messiah"))
# print(" Index of any item in scores list :", scores.index(78))

#Count
# print(" Count of any item in scores list :", scores.count(45))
# print(" Count of any item in players list :", players.count('Diya'))

#Sorting
numbers = [5, 2, 8,6, 1, 9,7, 3,4]
# smallest to largest (ascending)
numbers.sort()                                             # smallest to largest (ascending)
print("Sorted ascending:", numbers)

# largest to smallest  (descending)
numbers.sort(reverse=True)
print("Sorted descending:", numbers )
# File Name: 02_remaining_chocolates.py

# Title: Remaining Chocolates
# Problem Statement:
# Kumar has some chocolates. He wants to distribute them equally
# among his friends.
# Write a program to find how many chocolates are left after distribution.





# Solution:

chocolates = int(input("Enter total chocolates: "))
friends = int(input("Enter number of friends: "))

remaining = chocolates % friends

print("Chocolates left:", remaining)

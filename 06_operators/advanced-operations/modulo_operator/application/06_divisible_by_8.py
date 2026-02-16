# File Name: 06_divisible_by_8.py

# Title: Divisible by 8 Checker
# Problem Statement:
# Write a Python program to check whether a given number is divisible by 8
# using the modulo (%) operator.

# Solution:

number = int(input("Enter a number: "))

if number % 8 == 0:
    print(number, "is divisible by 8.")
else:
    print(number, "is NOT divisible by 8.")

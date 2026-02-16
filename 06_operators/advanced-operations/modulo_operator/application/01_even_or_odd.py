# File Name: 01_even_or_odd.py

# Title: Even or Odd Checker
# Problem Statement:
# Write a Python program to check whether a given number is even or odd
# using the modulo (%) operator.

# Solution:

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("It is an Even number.")
else:
    print("It is an Odd number.")

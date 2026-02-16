# File Name: 07_divisibility_checker.py

# Title: Divisibility Checker
# Problem Statement:
# Write a Python program to check whether a given number is divisible
# by another number using the modulo (%) operator.

# Solution:

number = int(input("Enter the number: "))
divisor = int(input("Enter the divisor: "))

if number % divisor == 0:
    print(number, "is divisible by", divisor)
else:
    print(number, "is NOT divisible by", divisor)

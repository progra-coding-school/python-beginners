'''Assignment 4: Mini Calculator Program

Write a Python program for a mini calculator using:

input()
variables
print()

The program should perform:

Addition
Subtraction
Multiplication
Division '''

#Solution:

# Mini Calculator Program

# Getting input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Performing calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Displaying results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
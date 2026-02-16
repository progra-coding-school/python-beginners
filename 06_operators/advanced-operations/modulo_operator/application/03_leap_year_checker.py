# File Name: 03_leap_year_checker.py

# Title: Leap Year Checker
# Problem Statement:
# Write a Python program to check whether a given year is a leap year.
# A year is a leap year if it is divisible by 4.

# Solution:

year = int(input("Enter a year: "))

if year % 4 == 0:
    print("It is a Leap Year.")
else:
    print("It is NOT a Leap Year.")

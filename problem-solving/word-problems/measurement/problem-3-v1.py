'''
Imagine you are designing a robot.
Your robot starts with *80% battery. Every step
the robot takes uses **2% battery*.
Write a Python program to calculate the battery remaining
 after the robot walks *25 steps*.
Think like an engineer and solve the problem using Python!
'''

battery = 80
steps = 25
battery_used_per_step = 2

battery_remaining = battery - (steps * battery_used_per_step)

print("Battery Remaining:", battery_remaining, "%")


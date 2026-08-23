'''
Imagine you are designing a robot.
Your robot starts with *80% battery. Every step
the robot takes uses **2% battery*.
Write a Python program to calculate the battery remaining
 after the robot walks *25 steps*.
Think like an engineer and solve the problem using Python!
'''

total_charge=input("Please enter the total charge remaining: ")
charge_each_step=input("Please enter the charge required for each step: ")
steps_robot_walked=input("Please enter the number of steps the robot walked: ")

charges_used_by_robot=int(steps_robot_walked)*int(charge_each_step)
charge_remaining=int(total_charge)-charges_used_by_robot
print('charge_remaining',charge_remaining)





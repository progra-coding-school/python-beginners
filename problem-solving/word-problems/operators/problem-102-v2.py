'''
Problem:
Smart Traffic Light (Comparison + Logical)

A smart traffic light turns green only if: There are more than
10 cars, or An ambulance is waiting. Task: Write a program to
decide whether the light should turn green. Use: >, or
'''

cars=int(input("Please enter the number of cars waiting"))
is_ambulance_waiting=bool(input("Please enter True if ambulance is waiting else enter as False"))

if cars > 10 or is_ambulance_waiting==True:
    print("Turn the traffic light GREEN.")
else:
    print("Keep the traffic light RED.")


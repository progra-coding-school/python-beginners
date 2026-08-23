'''
Problem:
Smart Traffic Light (Comparison + Logical)

A smart traffic light turns green only if: There are more than
10 cars, or An ambulance is waiting. Task: Write a program to
decide whether the light should turn green. Use: >, or
'''

cars=8
is_ambulance_waiting=True

if cars > 10 or is_ambulance_waiting==True:
    print("Turn the traffic light GREEN.")
else:
    print("Keep the traffic light RED.")


'''
A room checks its brightness level. Above 80 →
Turn Lights Off 40–80 → Keep Lights As They Are
Below 40 → Turn Lights On
'''

brightness = int(input("Enter the room brightness level (0-100): "))

if brightness > 80:
    print("Turn Lights Off")
elif brightness >= 40:
    print("Keep Lights As They Are")
else:
    print("Turn Lights On")
'''
Space Rocket Launch

Problem:
 A rocket can launch only if the fuel is at least 95% and
 the wind speed is below 20 km/h.
'''

fuel = 98
wind_speed = 15

if fuel >= 95 and wind_speed < 20:
    print("Rocket is ready for launch!")
else:
    print("Launch aborted.")
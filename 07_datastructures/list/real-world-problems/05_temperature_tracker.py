# Program Code: 07-realworld-05
# Title: Weekly Temperature Tracker

# Problem:
# Track the temperature of a city for 7 days.
# Find the hottest day, coolest day, and average temperature.

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperatures = [32, 35, 33, 38, 36, 30, 31]

print("--- Weekly Temperature Report ---")
for i in range(len(days)):
    print(days[i], ":", temperatures[i], "°C")

# Hottest day
hottest = max(temperatures)
hottest_day = days[temperatures.index(hottest)]
print("\nHottest day:", hottest_day, "at", hottest, "°C")

# Coolest day
coolest = min(temperatures)
coolest_day = days[temperatures.index(coolest)]
print("Coolest day:", coolest_day, "at", coolest, "°C")

# Average temperature
average = sum(temperatures) / len(temperatures)
print("Average temperature:", round(average, 1), "°C")

# Days above average
print("\nDays above average:")
for i in range(len(days)):
    if temperatures[i] > average:
        print(" -", days[i], "(", temperatures[i], "°C )")

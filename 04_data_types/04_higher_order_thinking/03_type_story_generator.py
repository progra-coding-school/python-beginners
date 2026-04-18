# Program Code: DT-HOT-03
# Title: Type Story Generator
# Cognitive Skill: Higher Order Thinking (Creative application)
# Topic: Data Types in Python

# Create a mini story using all four data types: int, float, str, bool
print("--- Type Story Generator ---\n")

# Collect story ingredients
character = input("Enter a character name: ")                                      # str
age = int(input("Enter their age: "))                                              # int
speed_kmph = float(input("Enter their speed (kmph): "))                           # float
has_superpower = input("Do they have a superpower? (yes/no): ").lower() == "yes"  # bool
item = input("Enter a magical item they carry: ")                                  # str
distance_km = float(input("Enter a distance to travel (km): "))                   # float

# Calculate story details
travel_hours = round(distance_km / speed_kmph, 1)
double_age = age * 2

# Generate the story
print("\n--- The Story of " + character + " ---\n")
print("Once upon a time, there was a " + str(age) + "-year-old adventurer named " + character + ".")
if has_superpower:
    print(character + " had an incredible superpower and carried a " + item + ".")
else:
    print(character + " had no special powers, only a " + item + " by their side.")

print("One day, " + character + " set out on a " + str(distance_km) + " km journey,")
print("travelling at", speed_kmph, "kmph. The trip took", travel_hours, "hours.")
print("When " + character + " finally returned, they were " + str(double_age) + " years wiser.")
print("\nThe End.")

# Think:
# 1. Which variables were int? Which were float? Why?
# 2. How did the bool 'has_superpower' change the story?
# 3. Can you add more story branches using other bool variables?

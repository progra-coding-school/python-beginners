# Program Code: DT-PS-01
# Title: Temperature Converter
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Data Types in Python

# Big question: Convert temperature between Celsius and Fahrenheit.
# Break it down — identify the types needed first.

# Step 1: Get temperature from user (input → convert to float)
celsius = float(input("Enter temperature in Celsius: "))

# Step 2: Apply the formula
fahrenheit = (celsius * 9 / 5) + 32

# Step 3: Display result
print(f"{celsius}°C = {fahrenheit}°F")

# Step 4: Describe the weather
if celsius < 10:
    description = "Very cold!"
elif celsius < 20:
    description = "Cool."
elif celsius < 30:
    description = "Pleasant."
else:
    description = "Hot!"

print("Weather:", description)

# Think:
# 1. Why must celsius be float and not int?
# 2. What type is 'description'? Could it be any other type?
# 3. Can you add a Kelvin conversion? (K = °C + 273.15)

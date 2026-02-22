# Program Code: DT-PS-02
# Title: BMI Calculator
# Cognitive Skill: Problem Solving (Decomposition)
# Topic: Data Types in Python

# Big question: Calculate BMI and classify health category.
# Body Mass Index = weight (kg) / height (m) ^ 2

# Step 1: Collect inputs — convert to appropriate types
name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))

# Step 2: Convert height to metres
height_m = height_cm / 100

# Step 3: Calculate BMI
bmi = weight / (height_m ** 2)
bmi_rounded = round(bmi, 1)

# Step 4: Classify
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Step 5: Display
print(f"\nName: {name}")
print(f"BMI: {bmi_rounded}")
print(f"Category: {category}")

# Think:
# 1. Why is float better than int for weight and height?
# 2. What type is 'category'? What type is 'bmi_rounded'?
# 3. What would happen if height_cm was stored as str instead of float?

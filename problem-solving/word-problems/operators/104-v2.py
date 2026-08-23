max_capacity = int(input("Enter the robot's maximum carrying capacity (kg): "))
box_weight = int(input("Enter the weight of the box (kg): "))
medical_kit_weight = int(input("Enter the weight of the medical kit (kg): "))

total_weight = box_weight + medical_kit_weight

print("Total Weight:", total_weight, "kg")

if total_weight <= max_capacity:
    print("The rescue robot can carry both items.")
else:
    print("The rescue robot cannot carry both items.")
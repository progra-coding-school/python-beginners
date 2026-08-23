'''
Rescue Robot
Problem:
 A rescue robot can carry a maximum of 40 kg. A box weighs 18 kg,
and a medical kit weighs 15 kg. Check whether the robot can
carry both items.
'''

max_capacity = 40
box_weight = 18
medical_kit_weight = 15

total_weight = box_weight + medical_kit_weight

print("Total Weight:", total_weight, "kg")
if total_weight <= max_capacity:
    print("The rescue robot can carry both items.")
else:
    print("The rescue robot cannot carry both items.")
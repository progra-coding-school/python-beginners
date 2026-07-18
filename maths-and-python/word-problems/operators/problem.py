'''
Problem:
A bridge can safely hold 2500 kg. A truck weighs 1800 kg,
and its cargo weighs 900 kg. Check if the bridge can
 safely support the truck and cargo.
'''





bridge_limit = 2500
truck_weight = 1800
cargo_weight = 900

total_weight = truck_weight + cargo_weight

print("Total Weight:", total_weight)
print("Bridge Safe?", total_weight <= bridge_limit)
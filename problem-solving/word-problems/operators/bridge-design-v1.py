'''Problem: Design a 100-Meter Bridge
You are designing a bridge that is 100 meters long.
Each bridge slab is 5 meters long.
Challenge:
How many slabs do you need to build the entire bridge?
If each slab costs ₹2,000, what is the total cost?
'''

bridge_length = int(input("Enter bridge length: "))
slab_length = int(input("Enter slab length: "))
slab_cost=int(input("Enter slab costs: "))

slabs = bridge_length / slab_length

print("Slabs required:", slabs)
total_costs=slabs *slab_cost
print("Slabs costs:", total_costs)
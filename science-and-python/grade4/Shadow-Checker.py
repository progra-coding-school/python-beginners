# Concept: Objects that block light (opaque) form shadows.
# Opaque → clear shadow
# Translucent → faint shadow
# Transparent → no shadow

object_type = input("Enter object type (opaque / transparent / translucent): ")

if object_type == "opaque":
    print("This object forms a dark shadow.")
elif object_type == "translucent":
    print("This object forms a faint shadow.")
else:
    print("This object does not form a shadow.")

object_name = input("Enter object name: ").lower()

if object_name in ["dice", "ice cube"]:
    print("Shape: Cube")

elif object_name in ["box", "book"]:
    print("Shape: Cuboid")

elif object_name in ["ball", "orange"]:
    print("Shape: Sphere")

elif object_name in ["can", "bottle"]:
    print("Shape: Cylinder")

elif object_name in ["ice cream"]:
    print("Shape: Cone")

else:
    print("Shape not found")

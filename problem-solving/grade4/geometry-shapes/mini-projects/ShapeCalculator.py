shape = input("Enter the 3D shape (cube,cuboid,cylinder,cone,sphere): ").lower()

if shape == "cube":
    print("Faces: 6")
    print("Edges: 12")
    print("Vertices: 8")

elif shape == "cuboid":
    print("Faces: 6")
    print("Edges: 12")
    print("Vertices: 8")

elif shape == "cylinder":
    print("Faces: 3")
    print("Edges: 2")
    print("Vertices: 0")

elif shape == "cone":
    print("Faces: 2")
    print("Edges: 1")
    print("Vertices: 1")

elif shape == "sphere":
    print("Faces: 1")
    print("Edges: 0")
    print("Vertices: 0")

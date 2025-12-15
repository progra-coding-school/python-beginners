shape = input("Enter shape (rectangle/square/triangle/circle): ").lower()

if shape == "rectangle":
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    print("Sides: 4")
    print("Corners: 4")
    print("Perimeter:", 2 * (l + b))
    print("Area:", l * b)

elif shape == "square":
    s = int(input("Enter Side length : "))
    print("Sides: 4")
    print("Corners: 4")
    print("Perimeter:", 4 * s)
    print("Area:", s * s)

elif shape == "triangle":
    a = int(input("Enter Side 1 length: "))
    b = int(input("Enter Side 2 length: "))
    c = int(input("Enter Side 3 length: "))
    h = int(input("Enter Height length: "))
    print("Sides: 3")
    print("Corners: 3")
    print("Perimeter:", a + b + c)
    print("Area:", (b * h) / 2)

elif shape == "circle":
    r = int(input("Enter Radius length: "))
    print("Sides: 0")
    print("Corners: 0")
    print("Circumference:", 2 * 3.14 * r)
    print("Area:", 3.14 * r * r)

else:
    print("Invalid shape")

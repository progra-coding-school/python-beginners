# Concept: Closer to light → bigger shadow

distance = int(input("Enter distance from light source (cm): "))

if distance < 20:
    print("Shadow is very big.")
elif distance < 40:
    print("Shadow is medium.")
else:
    print("Shadow is small.")
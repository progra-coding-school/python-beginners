# Concept: Shadow position shows time.

shadow_length = int(input("Enter shadow length: "))

if shadow_length > 50:
    print("It is morning or evening.")
elif shadow_length > 20:
    print("It is afternoon.")
else:
    print("It is noon.")

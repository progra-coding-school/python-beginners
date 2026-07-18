'''
A ribbon is 24.6 meters long.
It is cut into 6 equal pieces.
What is the length of each piece?
'''

# Get input from the user
length = float(input("Enter the ribbon length (meters): "))
pieces = int(input("Enter the number of pieces: "))

# Calculate the length of each piece
each = length / pieces

# Display the result
print("Length of each piece:", each, "meters")
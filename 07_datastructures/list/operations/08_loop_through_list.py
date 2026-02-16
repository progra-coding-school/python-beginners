# Program Code: 07-operations-08
# Title: Looping Through a List

friends = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]

# Method 1: Simple for loop
print("--- Using for loop ---")
for friend in friends:
    print("Hello", friend)

# Method 2: Using index with range and len
print("\n--- Using index ---")
for i in range(len(friends)):
    print("Friend", i + 1, "is", friends[i])

# Method 3: Using enumerate (gives both index and value)
print("\n--- Using enumerate ---")
for index, friend in enumerate(friends):
    print(index, "->", friend)

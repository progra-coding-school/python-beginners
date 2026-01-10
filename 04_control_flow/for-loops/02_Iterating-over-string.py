# Iterating Over a String

name = "Python"
for char in name:
    print(char)

for char in ['P', 'y', 't', 'h', 'o', 'n']:
    print(char)


# Step-by-Step Explanation:
# The value "Python" is stored in memory.
# Internally, Python stores it as a sequence of characters:
# ['P', 'y', 't', 'h', 'o', 'n']
# Line number 2 begins a for loop that will run once for each character in the string name.
# Each time the loop runs:
# The next character from name is assigned to the variable char.
# The loop body (print(char)) is executed.
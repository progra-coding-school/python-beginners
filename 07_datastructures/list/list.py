# List of school subjects
subjects = ["Math", "Science", "English", "History", "Art", "Geography", "Computer"]

# Print the original list
print("Subjects:", subjects)

# Accessing elements
print("First subject:", subjects[0])
print("Last subject:", subjects[-1])

# Adding a subject
subjects.append("Physical Education")
print("After adding a subject:", subjects)

# Removing a subject
subjects.remove("Art")
print("After removing 'Art':", subjects)

# Updating a subject
subjects[2] = "Literature"
print("After updating a subject:", subjects)

# Slicing the list
print("First three subjects:", subjects[:3])



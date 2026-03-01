# Program Code: LIST-PS-02
# Title: Class Topper Finder
# Cognitive Skill: Problem Solving (Parallel lists, max, index)
# Topic: Lists in Python

# Parallel lists — names and marks share the same index
student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
student_marks = [88, 95, 76, 91, 83]

print("=== Class Marks Report ===")
print()

# Display marks
print("Student           Marks")
print("-" * 25)
for i in range(len(student_names)):
    print("  " + student_names[i].ljust(14) + str(student_marks[i]))
print()

# Find topper
highest = max(student_marks)
topper_index = student_marks.index(highest)
topper_name  = student_names[topper_index]

print("Highest marks:", highest)
print("Class topper:", topper_name)
print()

# Find lowest
lowest = min(student_marks)
lowest_index = student_marks.index(lowest)
print("Lowest marks:", lowest)
print("Needs support:", student_names[lowest_index])
print()

# Class average
average = sum(student_marks) / len(student_marks)
print("Class average:", round(average, 1))
print()

# Sort by marks (highest first) using zip + sort
paired = list(zip(student_marks, student_names))
paired.sort(reverse=True)

print("Rank  Name          Marks")
print("-" * 30)
for rank, (marks, name) in enumerate(paired, start=1):
    label = " (Topper)" if rank == 1 else ""
    print("  " + str(rank) + "     " + name.ljust(12) + str(marks) + label)

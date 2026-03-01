# Class Topper Finder
# KEY IDEA: Parallel lists — student_names[i] and student_marks[i] always belong to the same student.
# We link two lists by keeping them the same length and in the same order.
# This lets us find the topper, lowest scorer, class average, and a ranked table.

# names[0] = "Aarav" → marks[0] = 88 (Aarav scored 88)
# names[1] = "Diya"  → marks[1] = 95 (Diya scored 95)  ← same index links them
student_names = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
student_marks = [88, 95, 76, 91, 83]

# Display all students and their marks using the shared index
print("Student           Marks")
print("-" * 25)
for i in range(len(student_names)):
    print("  " + student_names[i].ljust(14) + str(student_marks[i]))
print()

# Find the topper — max() gives the highest mark, index() finds its position
# The same position in student_names gives us the topper's name
highest = max(student_marks)
topper_index = student_marks.index(highest)   # find WHERE the max mark is
topper_name  = student_names[topper_index]    # same index in names = topper's name

print("Highest marks:", highest)
print("Class topper:", topper_name)
print()

# Find who needs the most support — same trick with min()
lowest = min(student_marks)
lowest_index = student_marks.index(lowest)
print("Lowest marks:", lowest)
print("Needs support:", student_names[lowest_index])
print()

# Class average — sum() adds all marks, len() counts students
average = sum(student_marks) / len(student_marks)
print("Class average:", round(average, 1))
print()

# Sort by marks (highest first) using zip() + sort()
# zip() pairs each mark with its name: [(88, "Aarav"), (95, "Diya"), ...]
# Sorting the pairs keeps names and marks linked — they move together
paired = list(zip(student_marks, student_names))
paired.sort(reverse=True)                        # highest mark first

print("Rank  Name          Marks")
print("-" * 30)
for rank, (marks, name) in enumerate(paired, start=1):
    label = " (Topper)" if rank == 1 else ""
    print("  " + str(rank) + "     " + name.ljust(12) + str(marks) + label)

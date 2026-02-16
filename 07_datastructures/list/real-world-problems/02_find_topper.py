# Program Code: 07-realworld-02
# Title: Find the Class Topper

# Problem:
# A teacher has marks of 5 students.
# Find who got the highest marks and who got the lowest marks.

students = ["Aarav", "Diya", "Kabir", "Meera", "Rohan"]
marks = [78, 92, 65, 88, 95]

print("Students:", students)
print("Marks:", marks)

# Find the highest marks
highest = max(marks)
topper_index = marks.index(highest)
print("\nClass Topper:", students[topper_index], "with", highest, "marks")

# Find the lowest marks
lowest = min(marks)
lowest_index = marks.index(lowest)
print("Lowest marks:", students[lowest_index], "with", lowest, "marks")

# Average marks
total = sum(marks)
average = total / len(marks)
print("Class average:", average)

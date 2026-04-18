# Program Code: FN-UN-04
# Title: Reusing Functions — The Real Power
# Cognitive Skill: Understanding
# Topic: Functions in Python

# The same function can be called with different inputs each time.
# This is what makes functions so powerful!

# --- One function, many uses ---
def calculate_area(length, width):
    return length * width

# Use it for many different rooms
bedroom_area = calculate_area(12, 10)
hall_area = calculate_area(20, 15)
kitchen_area = calculate_area(8, 6)

print("Bedroom:", bedroom_area, "sq.ft")
print("Hall:   ", hall_area, "sq.ft")
print("Kitchen:", kitchen_area, "sq.ft")
print("Total house area:", bedroom_area + hall_area + kitchen_area, "sq.ft")

print()

# --- Functions calling functions (reuse inside reuse!) ---
def calculate_perimeter(length, width):
    return 2 * (length + width)

def room_summary(name, length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    print(name + ": Area=" + str(area) + " sq.ft, Perimeter=" + str(perimeter) + " ft")

room_summary("Bedroom", 12, 10)
room_summary("Hall", 20, 15)
room_summary("Kitchen", 8, 6)

print()

# --- Building a mini report card using reusable functions ---
def get_total(m, s, e):
    return m + s + e

def get_average(total):
    return total / 3

def get_grade(average):
    if average >= 90: return "A+"
    elif average >= 80: return "A"
    elif average >= 60: return "B"
    else: return "C"

def print_report(name, maths, science, english):
    total = get_total(maths, science, english)
    average = get_average(total)
    grade = get_grade(average)
    print(name + " | Total: " + str(total) + " | Avg: " + str(round(average, 1)) + " | Grade: " + grade)

print("--- Report Card ---")
print("Name       | Total | Avg   | Grade")
print("-" * 40)
print_report("Aarav",  88, 92, 85)
print_report("Diya",   70, 65, 78)
print_report("Karthik", 55, 48, 60)
print_report("Riya",   95, 98, 91)

# Think:
# 1. How many times was get_grade() called in the report above?
# 2. What would happen if we needed to change the grade boundary to 85 for A?
#    How many places would we fix?

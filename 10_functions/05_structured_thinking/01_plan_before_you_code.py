# Program Code: FN-ST-01
# Title: Plan Before You Code — Library Book System
# Cognitive Skill: Structured Thinking (Planning)
# Topic: Functions in Python

# Always plan your functions BEFORE writing code:
# - What is the function's NAME? (describes its job)
# - What are the PARAMETERS? (what info does it need?)
# - What does it RETURN? (what does it give back?)
# - What TYPE is the return? (str, int, bool?)

# PROBLEM: Build a library book lending system.
#
# PLAN:
#
# Function 1: is_book_available(book_title, library)
#   - Parameters: book_title (str), library (dict)
#   - Returns: True if available, False if not (bool)
#
# Function 2: borrow_book(book_title, student_name, library)
#   - Parameters: book_title (str), student_name (str), library (dict)
#   - Returns: success message (str)
#
# Function 3: return_book(book_title, library)
#   - Parameters: book_title (str), library (dict)
#   - Returns: success message (str)
#
# Function 4: show_available_books(library)
#   - Parameters: library (dict)
#   - Returns: nothing (just displays)
#
# Function 5: get_total_books(library)
#   - Parameters: library (dict)
#   - Returns: count of available books (int)

# ---- CODE FOLLOWS THE PLAN ----

# Library: book title → True (available), False (borrowed)
library = {
    "Python for Kids":     True,
    "Maths Made Easy":     True,
    "Science Explorer":    False,
    "Story of Pi":         True,
    "Code Your World":     False,
}

def is_book_available(book_title, library):
    if book_title in library:
        return library[book_title]
    return False  # book not found

def borrow_book(book_title, student_name, library):
    if book_title not in library:
        return f"'{book_title}' is not in our library."
    if not is_book_available(book_title, library):
        return f"'{book_title}' is currently borrowed by someone else."
    library[book_title] = False
    return f"'{book_title}' borrowed successfully by {student_name}!"

def return_book(book_title, library):
    if book_title not in library:
        return f"'{book_title}' is not our library's book."
    if library[book_title]:
        return f"'{book_title}' was not borrowed. No action needed."
    library[book_title] = True
    return f"'{book_title}' returned. Thank you!"

def show_available_books(library):
    print("\n=== Available Books ===")
    found = False
    for title, available in library.items():
        if available:
            print(f"  ✓ {title}")
            found = True
    if not found:
        print("  No books available right now.")

def get_total_books(library):
    return sum(1 for available in library.values() if available)

# --- Run the system ---
show_available_books(library)
print(f"Total available: {get_total_books(library)} books\n")

print(borrow_book("Python for Kids", "Aarav", library))
print(borrow_book("Science Explorer", "Diya", library))
print(borrow_book("Story of Pi", "Karthik", library))

show_available_books(library)

print()
print(return_book("Story of Pi", library))
show_available_books(library)

# Think:
# 1. What new function would you add to show WHO borrowed a book?
# 2. How would you plan a function to search for books by keyword?

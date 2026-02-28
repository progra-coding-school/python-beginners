# Program Code: CL-HOT-02
# Title: Mini Library System
# Cognitive Skill: Higher Order Thinking
# Topic: Classes and Objects in Python

# Design challenge:
# Build a library system with two classes: Book and Library.
# Support: add books, issue to members, return, search, report.

class Book:
    def __init__(self, title, author, copies=1):
        self.title      = title
        self.author     = author
        self.copies     = copies
        self.issued_to  = []    # list of member names who borrowed it

    def is_available(self):
        return self.copies > len(self.issued_to)

    def issue(self, member):
        if not self.is_available():
            print(f"  '{self.title}' is not available right now.")
            return False
        self.issued_to.append(member)
        print(f"  '{self.title}' issued to {member}.")
        return True

    def return_book(self, member):
        if member in self.issued_to:
            self.issued_to.remove(member)
            print(f"  {member} returned '{self.title}'.")
            return True
        print(f"  {member} has no record of borrowing '{self.title}'.")
        return False

    def __str__(self):
        available = self.copies - len(self.issued_to)
        return f"'{self.title}' by {self.author} [{available}/{self.copies} available]"


class Library:
    def __init__(self, name):
        self.name  = name
        self.books = {}    # title → Book object

    def add_book(self, title, author, copies=1):
        if title in self.books:
            self.books[title].copies += copies
            print(f"  Added {copies} more copies of '{title}'.")
        else:
            self.books[title] = Book(title, author, copies)
            print(f"  New book added: {title}")

    def search(self, keyword):
        keyword = keyword.lower()
        results = [b for b in self.books.values()
                   if keyword in b.title.lower() or keyword in b.author.lower()]
        return results

    def issue(self, title, member):
        if title not in self.books:
            print(f"  '{title}' not found in library.")
            return
        self.books[title].issue(member)

    def return_book(self, title, member):
        if title not in self.books:
            print(f"  '{title}' not found in library.")
            return
        self.books[title].return_book(member)

    def report(self):
        print(f"\n=== {self.name} — Book Report ===")
        print(f"  Total books: {len(self.books)}")
        print()
        for book in self.books.values():
            print(f"  {book}")
            if book.issued_to:
                print(f"    Issued to: {', '.join(book.issued_to)}")

# --- Demo ---
lib = Library("Progra School Library")
print()

lib.add_book("Python Basics",    "Progra Team", copies=3)
lib.add_book("The Cricket Code", "Aarav Singh",  copies=2)
lib.add_book("Maths Magic",      "Diya Sharma",  copies=1)

print()
lib.issue("Python Basics",    "Aarav")
lib.issue("Python Basics",    "Diya")
lib.issue("Maths Magic",      "Karthik")
lib.issue("Maths Magic",      "Riya")    # only 1 copy — should fail

print()
lib.return_book("Python Basics", "Aarav")
lib.issue("Python Basics", "Ananya")    # now available again

print()
print("Search 'python':")
for b in lib.search("python"):
    print(f"  Found: {b}")

lib.report()

# Think:
# 1. Why use a dictionary (self.books) instead of a list to store books in Library?
# 2. How would you add a feature to track HOW MANY times each book has been borrowed?

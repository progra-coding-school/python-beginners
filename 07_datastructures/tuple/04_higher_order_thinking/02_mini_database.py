# Program Code: TU-HOT-02
# Title: Mini Database with Tuple Records
# Cognitive Skill: Higher Order Thinking
# Topic: Tuples in Python

# Design challenge:
# Build a read-only "database" of student records using tuples.
# Each record: (id, name, grade, city, score)
# Support: search, filter, sort, summarise.

# --- Database ---
FIELDS  = ("id", "name", "grade", "city", "score")
records = (
    (101, "Aarav",   7, "Chennai",    85),
    (102, "Diya",    6, "Madurai",    92),
    (103, "Karthik", 8, "Coimbatore", 78),
    (104, "Riya",    7, "Chennai",    88),
    (105, "Ananya",  6, "Trichy",     95),
    (106, "Vivek",   8, "Madurai",    72),
    (107, "Priya",   7, "Chennai",    90),
)

def display(rows, title="Records"):
    print(f"\n=== {title} ===")
    print(f"  {'ID':>4}  {'Name':<12} {'Grade':>5} {'City':<12} {'Score':>5}")
    print(f"  {'─'*4}  {'─'*12} {'─'*5} {'─'*12} {'─'*5}")
    for row in rows:
        print(f"  {row[0]:>4}  {row[1]:<12} {row[2]:>5} {row[3]:<12} {row[4]:>5}")

# --- Search by name ---
def search(name):
    return [r for r in records if r[1].lower() == name.lower()]

# --- Filter by grade ---
def filter_grade(grade):
    return [r for r in records if r[2] == grade]

# --- Filter by city ---
def filter_city(city):
    return [r for r in records if r[3].lower() == city.lower()]

# --- Sort by any field ---
def sort_by(field, descending=False):
    idx = FIELDS.index(field)
    return sorted(records, key=lambda r: r[idx], reverse=descending)

# --- Summary statistics ---
def summarise():
    scores = [r[4] for r in records]
    print("\n=== Summary ===")
    print(f"  Total students : {len(records)}")
    print(f"  Average score  : {sum(scores)/len(scores):.1f}")
    print(f"  Highest score  : {max(scores)}")
    print(f"  Lowest score   : {min(scores)}")

# --- Demo ---
display(records, "Full Database")

display(filter_grade(7), "Grade 7 Students")

display(filter_city("Chennai"), "Chennai Students")

result = search("Diya")
display(result, "Search: Diya")

display(sort_by("score", descending=True), "Sorted by Score (High → Low)")

summarise()

# Think:
# 1. Why are the records stored as tuples instead of lists?
# 2. How would you add a new student without "changing" the existing tuple database?

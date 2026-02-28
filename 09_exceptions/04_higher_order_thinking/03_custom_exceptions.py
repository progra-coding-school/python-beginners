# Program Code: EX-HOT-03
# Title: Designing Custom Exceptions
# Cognitive Skill: Higher Order Thinking
# Topic: Exceptions in Python

# Custom exceptions make error messages meaningful and allow
# callers to handle specific error types precisely.

# --- Step 1: Define a hierarchy of custom exceptions ---

class ProgratError(Exception):
    """Base exception for all Progra app errors."""
    pass

class InvalidScoreError(ProgratError):
    """Raised when a score is outside the valid 0–100 range."""
    def __init__(self, score):
        self.score = score
        super().__init__(f"Score {score} is invalid. Must be 0–100.")

class StudentNotFoundError(ProgratError):
    """Raised when a student ID does not exist in the database."""
    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__(f"Student ID {student_id} not found.")

class DuplicateStudentError(ProgratError):
    """Raised when trying to add a student that already exists."""
    def __init__(self, name):
        self.name = name
        super().__init__(f"Student '{name}' already exists.")

# --- Step 2: Mini student database using custom exceptions ---

class StudentDatabase:
    def __init__(self):
        self._records = {}      # id → {name, scores}
        self._next_id = 101

    def add_student(self, name):
        for rec in self._records.values():
            if rec["name"].lower() == name.lower():
                raise DuplicateStudentError(name)
        sid = self._next_id
        self._records[sid] = {"name": name, "scores": []}
        self._next_id += 1
        return sid

    def add_score(self, student_id, score):
        if student_id not in self._records:
            raise StudentNotFoundError(student_id)
        if not isinstance(score, (int, float)) or not (0 <= score <= 100):
            raise InvalidScoreError(score)
        self._records[student_id]["scores"].append(score)

    def average(self, student_id):
        if student_id not in self._records:
            raise StudentNotFoundError(student_id)
        scores = self._records[student_id]["scores"]
        if not scores:
            return 0
        return sum(scores) / len(scores)

    def report(self):
        print(f"  {'ID':>4}  {'Name':<12} {'Scores':<20} {'Avg':>5}")
        for sid, data in self._records.items():
            scores = data["scores"]
            avg    = sum(scores)/len(scores) if scores else 0
            print(f"  {sid:>4}  {data['name']:<12} {str(scores):<20} {avg:>5.1f}")

# --- Step 3: Demo ---
print("=== Custom Exception Demo ===\n")
db = StudentDatabase()

# Add students
for name in ["Aarav", "Diya", "Karthik"]:
    sid = db.add_student(name)
    print(f"Added {name} with ID {sid}")

# Duplicate
try:
    db.add_student("Aarav")
except DuplicateStudentError as e:
    print(f"DuplicateStudentError: {e}")

print()

# Add scores
operations = [(101, 85), (101, 92), (102, 78), (103, 110), (999, 80)]
for sid, score in operations:
    try:
        db.add_score(sid, score)
        print(f"Added score {score} for ID {sid}")
    except InvalidScoreError as e:
        print(f"InvalidScoreError: {e}")
    except StudentNotFoundError as e:
        print(f"StudentNotFoundError: {e}")

print()

print("=== Report ===")
db.report()

# Think:
# 1. Why inherit from a common base (ProgratError) instead of directly from Exception?
# 2. How does a custom exception give the caller more information than a plain ValueError?

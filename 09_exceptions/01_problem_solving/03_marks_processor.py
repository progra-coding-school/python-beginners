# Program Code: EX-PS-03
# Title: Marks Processor with Error Handling
# Cognitive Skill: Problem Solving
# Topic: Exceptions in Python

# Problem:
# A list of student mark entries arrives as raw strings.
# Some entries are malformed (missing data, wrong type, out of range).
# Process valid entries, skip bad ones with a clear reason.

# --- Raw data (name:score format, some are broken) ---
raw_entries = [
    "Aarav:85",
    "Diya:92",
    "Karthik:abc",        # score is not a number
    "Riya:105",           # score > 100
    "Ananya:-10",         # score < 0
    "Vivek:78",
    "Priya",              # missing colon separator
    ":88",                # missing name
    "Arjun:0",            # valid — zero is allowed
    "Meera:60.5",         # float score — handle gracefully
]

# --- Processor ---
valid_records   = {}
skipped_records = []

for entry in raw_entries:
    try:
        # Step 1: split on ':'
        parts = entry.split(":")
        if len(parts) != 2:
            raise ValueError("Expected format 'Name:Score'")

        name, score_str = parts[0].strip(), parts[1].strip()

        # Step 2: validate name
        if not name:
            raise ValueError("Name is empty")

        # Step 3: parse score
        score = float(score_str)
        score = round(score)    # round floats to int

        # Step 4: range check
        if not (0 <= score <= 100):
            raise ValueError(f"Score {score} is out of range (0–100)")

        # Step 5: all good!
        valid_records[name] = score

    except ValueError as e:
        skipped_records.append((entry, str(e)))

# --- Display results ---
print("=== Valid Records ===")
print(f"  {'Name':<12} {'Score':>5}")
print(f"  {'─'*12} {'─'*5}")
for name, score in valid_records.items():
    grade = "A+" if score >= 90 else "A" if score >= 80 else "B" if score >= 70 else "C"
    print(f"  {name:<12} {score:>5}  ({grade})")

print()

print("=== Skipped Entries ===")
for entry, reason in skipped_records:
    print(f"  '{entry}' → {reason}")

print()

print("=== Summary ===")
if valid_records:
    scores = list(valid_records.values())
    print(f"  Processed : {len(valid_records)} valid records")
    print(f"  Skipped   : {len(skipped_records)} invalid records")
    print(f"  Average   : {sum(scores)/len(scores):.1f}")
    print(f"  Top scorer: {max(valid_records, key=valid_records.get)} ({max(scores)})")

# Think:
# 1. Why did we use float() first and then round(), instead of int() directly?
# 2. How would you log the skipped records to a separate file for the teacher to review?

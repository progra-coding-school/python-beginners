# Which Approach Is Better?
# Side-by-side comparison: parallel lists vs dictionary, manual loop vs built-in.
# The better approach is always simpler to read, write, and extend.
# KEY LESSON: when Python has a built-in tool for the job, use it!

# Problem 1: Find a student's phone number by name
# Approach A uses two lists — must find index first, then use it on the second list
# Approach B uses a dictionary — one direct lookup with the name as key
print("Approach A: Parallel Lists")
names  = ["Aarav", "Diya", "Karthik", "Riya"]
phones = ["9876543210", "9123456780", "9988776655", "9876001122"]

search = "Karthik"
if search in names:
    idx = names.index(search)          # find index in one list...
    print(search + "'s phone:", phones[idx])   # ...use same index on the other list
else:
    print("Not found.")

print()

print("Approach B: Dictionary")
contacts = {
    "Aarav":   "9876543210",
    "Diya":    "9123456780",
    "Karthik": "9988776655",
    "Riya":    "9876001122",
}
# .get() does the lookup in one step — no index needed
phone = contacts.get(search, "Not found.")
print(search + "'s phone:", phone)

print()
print("Verdict:")
print("  Approach B (dictionary) is better because:")
print("  1. Lookup is direct — no need to find an index first.")
print("  2. Adding a contact keeps everything in one place.")
print("  3. Parallel lists can go out of sync if someone adds to one but forgets the other.")
print()

# Problem 2: Count how many times each item appears
# Approach A: manual search through a nested list — slow and hard to read
# Approach B: dictionary counter — one clean line per item
print("Approach A: Manual search with a list")
items   = ["pen", "book", "pen", "eraser", "pen", "book"]
counted = []

for item in items:
    found = False
    for entry in counted:       # search through all counted entries every time
        if entry[0] == item:
            entry[1] += 1
            found = True
            break
    if not found:
        counted.append([item, 1])

for entry in counted:
    print("  " + entry[0] + ":", entry[1])

print()

print("Approach B: Dictionary counter")
freq = {}
for item in items:
    freq[item] = freq.get(item, 0) + 1   # get current count (0 if new) + 1

for item, count in freq.items():
    print("  " + item + ":", count)

print()
print("Verdict:")
print("  Approach B is shorter, clearer, and faster to read and write.")
print("  Approach A uses nested loops — harder to understand and maintain.")

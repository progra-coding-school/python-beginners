# Program Code: CL-HOT-01
# Title: Reverse Engineer the Class
# Cognitive Skill: Higher Order Thinking
# Topic: Classes and Objects in Python

# Study the OUTPUT. Write the class that produced it.
# Then compare with the reference.

# --- Challenge 1 ---
# Output:
#   Tommy is a Labrador.
#   Bruno is a Poodle.
#   Tommy says: Woof!

print("=== Challenge 1 ===")
print("Target output:")
print("  Tommy is a Labrador.")
print("  Bruno is a Poodle.")
print("  Tommy says: Woof!")
print()

class Dog:
    def __init__(self, name, breed):
        self.name  = name
        self.breed = breed

    def describe(self):
        print(f"  {self.name} is a {self.breed}.")

    def bark(self):
        print(f"  {self.name} says: Woof!")

d1 = Dog("Tommy", "Labrador")
d2 = Dog("Bruno", "Poodle")
d1.describe()
d2.describe()
d1.bark()

print()

# --- Challenge 2 ---
# Output:
#   Lamp is OFF
#   Lamp is ON
#   Lamp is OFF

print("=== Challenge 2 ===")
print("Target: toggle lamp ON/OFF")
print()

class Lamp:
    def __init__(self):
        self.on = False

    def toggle(self):
        self.on = not self.on

    def status(self):
        print(f"  Lamp is {'ON' if self.on else 'OFF'}")

l = Lamp()
l.status()
l.toggle()
l.status()
l.toggle()
l.status()

print()

# --- Challenge 3 ---
# Output:
#   Wallet: Rs.1000
#   After buy: Rs.700
#   After buy: Rs.400
#   Not enough money!
#   Final: Rs.400

print("=== Challenge 3 ===")
print("Target: wallet spending")
print()

class Wallet:
    def __init__(self, balance):
        self.balance = balance
        print(f"  Wallet: Rs.{self.balance}")

    def spend(self, amount):
        if amount > self.balance:
            print("  Not enough money!")
            return
        self.balance -= amount
        print(f"  After buy: Rs.{self.balance}")

    def show(self):
        print(f"  Final: Rs.{self.balance}")

w = Wallet(1000)
w.spend(300)
w.spend(300)
w.spend(800)
w.show()

# Think:
# 1. In Challenge 2, what does `not self.on` do when `self.on` is False?
# 2. In Challenge 3, how would you add a `top_up(amount)` method?

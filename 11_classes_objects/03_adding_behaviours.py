# Adding Properties (What it has)

class Dog:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour

    def barks(self):
        print("Dog Barks---->")

my_dog=Dog("Jimmy","Brown")
print(my_dog.name)
print(my_dog.colour)
my_dog.barks()


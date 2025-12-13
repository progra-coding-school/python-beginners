#Create a class for Car and add attributes and Behaviours

class Car:
    def __init__(self, brand, colour):
        self.brand = brand
        self.colour = colour

    def start(self):
        print(self.brand, "car is starting...")

    def stop(self):
        print(self.brand, "car is stopping...")


my_car = Car("Kia", "White")
my_car.start()
my_car.stop()

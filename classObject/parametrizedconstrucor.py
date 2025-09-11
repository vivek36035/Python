class Car:
    def __init__(self, name, model, colour):
        self.name = name
        self.model = model
        self.colour = colour

    def display(self):
        print("Name:", self.name)
        print("Model:", self.model)
        print("Colour:", self.colour)
        print("************")

obj1 = Car("Range-Rover", "Defender", "White")
obj1.display()

obj2 = Car("Toyota","Fortuner","Black")
obj2.display()

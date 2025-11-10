class Car:
    def __init__(self, name):
        self.name = name
        print(self.name, "created")

    def __del__(self):
        print(self.name, "destroyed")

obj1 = Car("BMW")
obj2 = Car("Audi")

del obj1   # explicitly destroying
print("Program running...")

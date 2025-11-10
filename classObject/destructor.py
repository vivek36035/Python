class Car:
    def __init__(self, name):
        self.name = name
        print(self.name, "is created")

    def __del__(self):
        print(self.name, "is destroyed")

# Create object
obj = Car("Range Rover")

# Delete object manually
del obj

print("Program End")

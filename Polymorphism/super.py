class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person constructor called")

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll
        print("Student constructor called")

    def show(self):
        super().show()
        print("Roll Number:", self.roll)

s = Student("Vivek", 20, 101)
s.show()

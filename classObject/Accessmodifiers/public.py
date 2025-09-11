class Student:
    def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public

obj = Student("Vivek", 21)
print(obj.name)
print(obj.age)
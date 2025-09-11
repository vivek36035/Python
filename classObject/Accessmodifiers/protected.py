class Student:
    def __init__(self, name, age):
        self._name = name      # protected
        self._age = age        # protected
    
    def show(self):
        print("Name:", self._name, "Age:", self._age)

obj = Student("Rohit", 22)
print(obj._name)   # Accessible, but should be treated as protected

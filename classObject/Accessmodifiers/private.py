class Student:
    def __init__(self, name, age):
        self.__name = name     # private
        self.__age = age       # private
    
    def show(self):
        print("Name:", self.__name, "Age:", self.__age)

obj = Student("Ankit", 23)
# print(obj.__name)  # Error: not directly accessible
obj.show()

# But can still access using name mangling:
print(obj._Student__name)   # Works, but not recommended

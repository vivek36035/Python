class Grandparent:
    def greet(self):
        print("Hello from Grandparent")

class Parent(Grandparent):
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")


c = Child()
c.greet()
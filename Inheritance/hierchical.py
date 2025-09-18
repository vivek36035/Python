class Parent:
    def greet(self):
        print("Hello from Parent")

class Child1(Parent):
    def c1(self):
        print("Child1 here")

class Child2(Parent):
    def c2(self):
        print("Child2 here")

c1 = Child1()
c1.greet()
c1.c1()

c2 = Child2()
c2.greet()
c2.c2()

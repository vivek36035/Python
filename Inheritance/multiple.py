class Father:
    def skills(self):
        print("I can drive")

class Mother:
    def skills(self):
        print("I can cook")

class Child(Father, Mother):
    def skills(self):
        print("I can code")

c = Child()
c.skills() 

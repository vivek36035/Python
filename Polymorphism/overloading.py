class Calculator:
    # Method with variable arguments
    def add(self, *args):
        total = 0
        print("Numbers received:", args)
        for num in args:
            total += num
        print("Addition is:", total)

c = Calculator()

c.add(10, 20)
c.add(5, 15, 25)
c.add(2, 4, 6, 8)

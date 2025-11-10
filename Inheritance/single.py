class base:
    def __init__(self):
        print("Hello from base")
        
class child(base):
    def __init__(self):
        base.__init__(self)
        print("Hello from child")

obj = child()
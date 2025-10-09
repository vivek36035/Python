class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("You must be at least 18 years old.")
    else:
        print("You are eligible to vote!")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Custom Exception:", e)
finally:
    print("Program finished.")

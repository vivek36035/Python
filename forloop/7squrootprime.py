import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter number: "))
sqrt_n = math.sqrt(n)

if sqrt_n == int(sqrt_n):
    if is_prime(int(sqrt_n)):
        print("Square root is prime.")
    else:
        print("Square root is not prime.")
else:
    print("Square root is not a whole number.")

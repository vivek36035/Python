a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a <= b and a <= c:
    print("Smallest:", a)
elif b <= a and b <= c:
    print("Smallest:", b)
else:
    print("Smallest:", c)

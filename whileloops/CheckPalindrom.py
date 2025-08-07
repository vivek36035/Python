n = int(input("Enter a number: "))
original = n
reverse = 0
while n > 0:
    reverse = reverse * 10 + n % 10
    n //= 10
if reverse == original:
    print("Palindrome")
else:
    print("Not Palindrome")

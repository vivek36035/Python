n = int(input("Enter a number: "))
i = 2
is_prime = True
while i <= n // 2:
    if n % i == 0:
        is_prime = False
        break
    i += 1
if is_prime and n > 1:
    print("Prime")
else:
    print("Not Prime")

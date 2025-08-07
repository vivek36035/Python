import math

n = int(input("Enter n: "))
sum_series = 0
for i in range(0, n+1):
    sum_series += 1 / math.factorial(i)
print("Sum =", sum_series)

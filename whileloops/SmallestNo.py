n = int(input("Enter count of numbers: "))
i = 1
min_num = float('inf')
while i <= n:
    num = int(input(f"Enter number {i}: "))
    if num < min_num:
        min_num = num
    i += 1
print("Smallest number:", min_num)

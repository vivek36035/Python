n = int(input("Enter count of numbers: "))
i = 1
max_num = float('-inf')
while i <= n:
    num = int(input(f"Enter number {i}: "))
    if num > max_num:
        max_num = num
    i += 1
print("Largest number:", max_num)

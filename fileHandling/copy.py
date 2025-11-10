with open("example1.txt", "r") as f1, open("copy.txt", "w") as f2:
    for line in f1:
        f2.write(line)
print("File copied successfully.")

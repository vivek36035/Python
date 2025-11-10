# create/write (overwrite if exists)
with open("example1.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("This is another line.")
print("File created & written successfully.")

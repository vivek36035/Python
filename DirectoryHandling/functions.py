import os
import shutil

# 1. Get current working directory
print("1. Current Directory:", os.getcwd())

# 2. Change current working directory (use an existing path)
# os.chdir("C:/Users/Vivek/Desktop")

# 3. List files and directories
print("3. Contents:", os.listdir("."))

# 4. Create a single directory
os.mkdir("my_folder2")

# 5. Create nested directories
os.makedirs("parent/child/grandchild")

# 6. Remove an empty directory
# os.mkdir("empty_folder")
# os.rmdir("empty_folder")

# 8. Rename a directory
os.rename("my_folder2", "new_name")

# 9. Delete a directory with all files inside
# os.makedirs("folder_with_files")
# with open("folder_with_files/file.txt", "w") as f:
#     f.write("Hello")
# shutil.rmtree("folder_with_files")

# # 10. Copy an entire directory
# os.makedirs("source_dir")
# with open("source_dir/file.txt", "w") as f:
#     f.write("Hello Backup")
# shutil.copytree("source_dir", "backup_dir")



# write a python  program to print the content of a directory using the os models , Searching online for the function which does that
import os

# Replace with your target directory or leave empty for current directory
directory_path = "java"

try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except (FileNotFoundError, NotADirectoryError, PermissionError) as error:
    print(f"Error: {error}")


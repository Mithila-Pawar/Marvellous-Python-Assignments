import os

file_name = input("Enter the file name: ")

if os.path.exists(file_name):
    print(f"The file {file_name} exists.")
else:
    print(f"The file {file_name} does not exist")
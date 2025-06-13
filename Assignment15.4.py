import sys

file1_name = sys.argv[1]
file2_name = sys.argv[2]

try:
    with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
        if file1.read() == file2.read():
            print("Success: Files have identical contents.")
        else:
            print("Failure: Files have different contents.")
except FileNotFoundError:
    print("Error: One or more files not found")
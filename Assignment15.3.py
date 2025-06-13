import sys

source_file_name = sys.argv[1]  
new_file_name = "Demo.txt"

try:
    with open(source_file_name, 'r') as source_file:
        with open(new_file_name, 'w') as new_file:
            new_file.write(source_file.read())
    print(f"Contents of {source_file_name} copied to {new_file_name}")
except FileNotFoundError:
    print(f"Error: Source file '{source_file_name}' not found")
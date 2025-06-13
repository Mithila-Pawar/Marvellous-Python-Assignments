import sys

file_name = sys.argv[1]
search_string = sys.argv[2]

try:
    with open(file_name, 'r') as file:
        content = file.read()
        count = content.count(search_string)
        print(f"The string '{search_string}' appears {count} times in the file.")
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found")
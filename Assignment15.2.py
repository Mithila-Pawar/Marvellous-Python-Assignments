file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        file_content = file.read()
        print(file_content)
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found")
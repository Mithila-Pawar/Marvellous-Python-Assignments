def read_and_display_file(filename="data.txt"):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
read_and_display_file()
def copy_file(source_filename="source.txt", destination_filename="destination.txt"):
    try:
        with open(source_filename, 'r') as source, open(destination_filename, 'w') as destination:
            contents = source.read()
            destination.write(contents)
        print(f"File '{source_filename}' copied to '{destination_filename}'")
    except FileNotFoundError:
        print(f"Error: File '{source_filename}' not found")

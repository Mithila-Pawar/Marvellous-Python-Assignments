def display_long_lines(filename="sample.txt"):
    try:
        with open(filename, 'r') as file:
            for line in file:
                words = line.split()
                if len(words) > 5:
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

display_long_lines()
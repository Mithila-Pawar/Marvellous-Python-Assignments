def count_file_stats(filename="sample.txt"):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = 0
            num_chars = 0
            for line in lines:
                words = line.split()
                num_words += len(words)
                num_chars += len(line)
            print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

count_file_stats()
def remove_blank_lines(input_filename="input.txt", output_filename="output.txt"):
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                if line.strip():
                    outfile.write(line)
        print(f"Blank lines removed. Output saved to '{output_filename}'")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found")

remove_blank_lines()
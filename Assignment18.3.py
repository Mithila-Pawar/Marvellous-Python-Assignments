import os
import sys

def copy_file_contents(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            with open(destination_filename, 'w') as dest_file:
                dest_file.write(source_file.read())
        print(f"Successfully copied contents of '{source_filename}' to '{destination_filename}'")
    except FileNotFoundError:
        print(f"Error: Source file '{source_filename}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) > 1:
      source_file_name = sys.argv[1]
      copy_file_contents(source_file_name, "Demo.txt")
    else:
      print("Error: Please provide source filename as a command line argument")
    
if __name__ == "__main__":
    main()
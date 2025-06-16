import os
import sys

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")

def main():
    filename_to_display = input("Enter filename to display: ")
    
if __name__ == "__main__":
    main()
import os
import sys

def count_string_occurrences(filename, search_string):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            count = content.count(search_string)
            print(f"The string '{search_string}' appears {count} times")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    filename_to_search = input("Enter filename for string search: ")
    search_string = input("Enter string to search: ")
    count_string_occurrences(filename_to_search, search_string)
        
if __name__ == "__main__":
    main()
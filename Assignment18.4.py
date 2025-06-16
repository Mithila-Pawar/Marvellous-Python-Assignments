import os
import sys

def compare_file_contents(file1_name, file2_name):
    try:
        with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
            if file1.read() == file2.read():
                print("Success: Files contain the same content")
            else:
                print("Failure: Files contain different content")
    except FileNotFoundError:
        print("Error: One or both files not found")
    except Exception as e:
         print(f"An error occurred: {e}")

def main():
    if len(sys.argv) > 2:
        file1_name = sys.argv[1]
        file2_name = sys.argv[2]
        compare_file_contents(file1_name, file2_name)
    else:
        print("Error: Please provide two filenames as command line arguments")
        
if __name__ == "__main__":
    main()
import os
import sys

def check_file_exists(Demo.txt):
    if os.path.exists(Demo.txt):
        print(f"File'{Demo.txt}'exists")
    else:
        print(f"File'{Demo.txt}'does not exist")
def main():
    filename_to_check = input("Enter filename to check for existence: ")

if __name__ == "__main__":
    main()
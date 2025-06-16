import os
import logging
import sys

logging.basicConfig(filename='Demo.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def list_files_by_extension(directory, extension):
    """Lists files with the specified extension in a directory"""
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"Directory '{directory}' does not exist")

        if not extension.startswith('.'):
            extension = '.' + extension

        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        if not files:
            logging.info(f"No files with extension '{extension}' found in '{directory}'")
        else:
            for file in files:
                logging.info(f"File found: {os.path.join(directory, file)}")
    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryFileSearch.py <directory> <extension>")
        sys.exit(1)
    directory = sys.argv[1]
    extension = sys.argv[2]
    list_files_by_extension(directory, extension)

if __name__ == "_main_":
    main()
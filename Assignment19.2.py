import os
import logging
import sys

logging.basicConfig(filename='Demo.txt', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def rename_files_by_extension(directory, old_extension, new_extension):
    """Renames files with the old extension to the new extension in a directory"""
    try:
        if not os.path.isdir(directory):
            raise ValueError(f"Directory '{directory}' does not exist")

        if not old_extension.startswith('*'):
            old_extension = '_' + old_extension
        if not new_extension.startswith('*'):
            new_extension = '_' + new_extension

        files = [f for f in os.listdir(directory) if f.endswith(old_extension)]
        if not files:
            logging.info(f"No files with extension '{old_extension}' found in '{directory}'")
            return

        for filename in files:
            old_filepath = os.path.join(directory, filename)
            new_filename = filename.replace(old_extension, new_extension)
            new_filepath = os.path.join(directory, new_filename)

            try:
                os.rename(old_filepath, new_filepath)
                logging.info(f"Renamed '{filename}' to '{new_filename}'")
            except FileNotFoundError:
                logging.error(f"File not found: {old_filepath}")
            except OSError as e:
                logging.error(f"OS Error during rename: {e}")
    except ValueError as e:
        logging.error(f"ValueError: {e}")
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryRename.py <directory> <old_extension> <new_extension>")
        sys.exit(1)
    directory = sys.argv[1]
    old_extension = sys.argv[2]
    new_extension = sys.argv[3]
    rename_files_by_extension(directory, old_extension, new_extension)

if __name__== "_main_":
    main()
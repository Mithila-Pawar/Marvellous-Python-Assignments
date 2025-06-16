import DirectoryUtils
import os
import logging
import sys


def main():
    "Displays checksums of all files in a directory"
    try:
        if len(sys.argv) > 1:
            directory_name = sys.argv[1]
        else:
           directory_name = None
        directory_path = DirectoryUtils.get_directory_path(directory_name)
    except (FileNotFoundError, NotADirectoryError) as e:
        logging.error(e)
        return

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            checksum = DirectoryUtils.calculate_checksum(filepath)
            if checksum:
                logging.info(f"Checksum for {filename}: {checksum}")

if __name__ == "_main_":
    main()
import os
import shutil
import sys

def copy_files_by_extension(source_dir, destination_dir, extension):
    """Copies files with the specified extension from source_dir to destination_dir,
    creating the latter"""
    try:
        os.makedirs(destination_dir, exist_ok=True)
        for item in os.listdir(source_dir):
            if item.endswith(extension):
                source_item = os.path.join(source_dir, item)
                destination_item = os.path.join(destination_dir, item)
                if os.path.isfile(source_item):
                    shutil.copy2(source_item, destination_item)
    except FileNotFoundError:
        print(f"Error: Source directory '{source_dir}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryCopyExt.py <source_directory> <destination_directory> <extension>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]
    file_extension = sys.argv[3]
    copy_files_by_extension(source_directory, destination_directory, file_extension)

if __name__ == "_main_":
    main()
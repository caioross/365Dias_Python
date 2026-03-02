import os
import shutil
from datetime import datetime

def move_files_by_creation_date(source_dir, target_base_dir):
    """
    Move files from the source directory to target directories based on their creation date.

    Args:
        source_dir (str): The path to the source directory containing the files.
        target_base_dir (str): The base path to the target directories.
    """
    if not os.path.exists(target_base_dir):
        os.makedirs(target_base_dir)

    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            try:
                # Get the creation time of the file
                creation_time = datetime.fromtimestamp(os.path.getctime(file_path))
                # Create the target directory based on the creation date
                target_dir = os.path.join(target_base_dir, creation_time.strftime('%Y-%m'))
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)
                # Move the file to the target directory
                shutil.move(file_path, os.path.join(target_dir, filename))
                print(f"Moved '{filename}' to '{target_dir}'")
            except Exception as e:
                print(f"Failed to move '{filename}': {e}")

def main():
    source_directory = '/path/to/downloads'
    target_base_directory = '/path/to/organized_downloads'
    move_files_by_creation_date(source_directory, target_base_directory)

if __name__ == '__main__':
    main()
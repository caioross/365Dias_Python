import os
import shutil

def move_large_files(source_dir, target_dir, size_threshold=1024*1024*1024):
    """
    Moves files larger than the specified size threshold from the source directory to the target directory.

    :param source_dir: The directory to search for large files.
    :param target_dir: The directory to move large files to.
    :param size_threshold: The size threshold in bytes (default is 1GB).
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getsize(file_path) > size_threshold:
                shutil.move(file_path, os.path.join(target_dir, file))
                print(f"Moved: {file_path} to {target_dir}")

def main():
    source_directory = input("Enter the source directory path: ")
    target_directory = input("Enter the target directory path: ")
    move_large_files(source_directory, target_directory)

if __name__ == '__main__':
    main()
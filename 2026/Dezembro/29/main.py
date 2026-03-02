import os
import shutil
from datetime import datetime, timedelta

def find_large_caches(directory, size_threshold_mb=100):
    """
    Finds large cache files in the specified directory.

    :param directory: The directory to search for cache files.
    :param size_threshold_mb: The size threshold in megabytes to consider a file as large.
    :return: A list of tuples containing the file path and its size in bytes.
    """
    large_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > size_threshold_mb * 1024 * 1024:
                large_files.append((file_path, file_size))
    return large_files

def delete_files(file_paths):
    """
    Deletes the specified files.

    :param file_paths: A list of file paths to delete.
    """
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"Deleted file: {file_path}")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

def main():
    """
    Main function to find and delete large cache files.
    """
    cache_directories = [
        '/var/cache',
        '/tmp',
        # Add other directories where caches are stored
    ]
    for directory in cache_directories:
        if os.path.exists(directory):
            large_caches = find_large_caches(directory)
            if large_caches:
                print(f"Large cache files found in {directory}:")
                for file_path, size in large_caches:
                    print(f"File: {file_path}, Size: {size / (1024 * 1024):.2f} MB")
                delete_files([file_path for file_path, _ in large_caches])
            else:
                print(f"No large cache files found in {directory}.")
        else:
            print(f"Directory {directory} does not exist.")

if __name__ == '__main__':
    main()
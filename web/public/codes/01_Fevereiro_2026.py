import os
import shutil

def organize_files_by_extension(source_directory, target_directory):
    """
    Organizes files in the source directory into subdirectories based on their file extensions.

    Args:
    source_directory (str): The path to the directory containing the files to be organized.
    target_directory (str): The path to the directory where the files will be organized.
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)
        if os.path.isfile(file_path):
            _, file_extension = os.path.splitext(filename)
            extension_directory = os.path.join(target_directory, file_extension[1:])  # Remove the dot

            if not os.path.exists(extension_directory):
                os.makedirs(extension_directory)

            shutil.move(file_path, os.path.join(extension_directory, filename))

def main():
    source_dir = input("Enter the source directory path: ")
    target_dir = input("Enter the target directory path: ")
    organize_files_by_extension(source_dir, target_dir)
    print("Files have been organized successfully.")

if __name__ == '__main__':
    main()
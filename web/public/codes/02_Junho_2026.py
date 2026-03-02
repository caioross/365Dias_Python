import os
import re
from typing import Set

def extract_emails_from_file(file_path: str) -> Set[str]:
    """
    Extracts unique email addresses from a given text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        Set[str]: A set of unique email addresses found in the file.
    """
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    emails = set()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            emails.update(email_pattern.findall(line))

    return emails

def extract_emails_from_directory(directory_path: str) -> Set[str]:
    """
    Extracts unique email addresses from all text files in a given directory.

    Args:
        directory_path (str): The path to the directory containing text files.

    Returns:
        Set[str]: A set of unique email addresses found in all text files.
    """
    all_emails = set()

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                all_emails.update(extract_emails_from_file(file_path))

    return all_emails

def main():
    """
    Main function to execute the script.
    """
    directory_path = input("Enter the directory path to search for text files: ")
    emails = extract_emails_from_directory(directory_path)
    print(f"Unique email addresses found: {emails}")

if __name__ == '__main__':
    main()
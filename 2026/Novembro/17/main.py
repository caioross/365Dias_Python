import hashlib
import os

def generate_hash(file_path):
    """
    Generates a SHA-256 hash for a given file.

    Args:
        file_path (str): The path to the file to hash.

    Returns:
        str: The hexadecimal SHA-256 hash of the file.
    """
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def verify_hash(file_path, expected_hash):
    """
    Verifies the SHA-256 hash of a file against an expected hash.

    Args:
        file_path (str): The path to the file to verify.
        expected_hash (str): The expected SHA-256 hash of the file.

    Returns:
        bool: True if the hash matches, False otherwise.
    """
    actual_hash = generate_hash(file_path)
    if actual_hash is None:
        return False
    return actual_hash == expected_hash

def main():
    """
    Main function to demonstrate generating and verifying a file hash.
    """
    file_path = 'example.txt'
    if not os.path.exists(file_path):
        print(f"Creating a sample file at {file_path}...")
        with open(file_path, 'w') as file:
            file.write("This is a sample file for hash generation.")

    # Generate hash
    file_hash = generate_hash(file_path)
    if file_hash:
        print(f"Generated SHA-256 hash: {file_hash}")

        # Verify hash
        if verify_hash(file_path, file_hash):
            print("Hash verification successful: The file has not been tampered with.")
        else:
            print("Hash verification failed: The file may have been tampered with.")

if __name__ == '__main__':
    main()
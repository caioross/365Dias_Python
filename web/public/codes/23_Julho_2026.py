import os
import hashlib

def calculate_sha256(file_path):
    """Calculate the SHA-256 hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The SHA-256 hash of the file.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def generate_hashes(directory):
    """Generate SHA-256 hashes for all files in a directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        dict: A dictionary with file paths as keys and their SHA-256 hashes as values.
    """
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_sha256(file_path)
            if file_hash:
                hashes[file_path] = file_hash
    return hashes

def write_hashes_to_file(hashes, output_file):
    """Write hashes to an output file.

    Args:
        hashes (dict): A dictionary with file paths as keys and their SHA-256 hashes as values.
        output_file (str): The path to the output file.
    """
    try:
        with open(output_file, 'w') as f:
            for file_path, file_hash in hashes.items():
                f.write(f"{file_hash}  {file_path}\n")
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def main():
    """Main function to generate hashes for all files in a directory and write them to a file."""
    directory = input("Enter the directory path: ")
    output_file = input("Enter the output file path: ")
    
    hashes = generate_hashes(directory)
    write_hashes_to_file(hashes, output_file)
    print(f"Hashes written to {output_file}")

if __name__ == '__main__':
    main()
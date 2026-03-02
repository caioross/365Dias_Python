import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from getpass import getpass

class PasswordManager:
    """
    PasswordManager class to handle saving and retrieving passwords securely.
    """

    def __init__(self, key_file='master.key'):
        """
        Initialize the PasswordManager with a key file.
        :param key_file: Path to the file where the master key is stored.
        """
        self.key_file = key_file
        self.fernet = None
        self.load_key()

    def load_key(self):
        """
        Load the master key from the key file or generate a new one if it doesn't exist.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as key_file:
                key = key_file.read()
        else:
            key = self.generate_key()
            with open(self.key_file, 'wb') as key_file:
                key_file.write(key)
        self.fernet = Fernet(key)

    def generate_key(self):
        """
        Generate a new master key using a password.
        :return: The generated key.
        """
        password = getpass("Enter a master password to generate a key: ").encode()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

    def encrypt_password(self, password):
        """
        Encrypt a password using the master key.
        :param password: The password to encrypt.
        :return: The encrypted password.
        """
        return self.fernet.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        """
        Decrypt a password using the master key.
        :param encrypted_password: The encrypted password to decrypt.
        :return: The decrypted password.
        """
        return self.fernet.decrypt(encrypted_password).decode()

    def save_password(self, service, username, password, password_file='passwords.txt'):
        """
        Save a password to a file.
        :param service: The service name.
        :param username: The username.
        :param password: The password to save.
        :param password_file: The file where passwords are stored.
        """
        encrypted_password = self.encrypt_password(password)
        with open(password_file, 'a') as file:
            file.write(f"{service},{username},{encrypted_password}\n")

    def get_password(self, service, username, password_file='passwords.txt'):
        """
        Retrieve a password from the file.
        :param service: The service name.
        :param username: The username.
        :param password_file: The file where passwords are stored.
        :return: The decrypted password.
        """
        with open(password_file, 'r') as file:
            for line in file:
                service_stored, username_stored, encrypted_password = line.strip().split(',')
                if service_stored == service and username_stored == username:
                    return self.decrypt_password(encrypted_password)
        return None

def main():
    """
    Main function to interact with the PasswordManager.
    """
    pm = PasswordManager()
    while True:
        print("\nOptions: save, get, exit")
        option = input("Choose an option: ").strip().lower()
        if option == 'save':
            service = input("Enter the service name: ").strip()
            username = input("Enter the username: ").strip()
            password = getpass("Enter the password: ").strip()
            pm.save_password(service, username, password)
            print("Password saved successfully.")
        elif option == 'get':
            service = input("Enter the service name: ").strip()
            username = input("Enter the username: ").strip()
            password = pm.get_password(service, username)
            if password:
                print(f"Password for {service} ({username}): {password}")
            else:
                print("Password not found.")
        elif option == 'exit':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
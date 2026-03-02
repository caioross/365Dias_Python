def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a given text using the Caesar Cipher.

    :param text: The input string to be encrypted or decrypted.
    :param shift: The number of positions each character in the text is shifted.
    :param mode: The operation mode, either 'encrypt' or 'decrypt'.
    :return: The resulting encrypted or decrypted string.
    """
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)


def main():
    """
    Main function to execute the Caesar Cipher simulation.
    Prompts the user for input and displays the encrypted or decrypted text.
    """
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(text, shift, mode)
    print(f"Result: {result}")


if __name__ == '__main__':
    main()
import random
import math

def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime():
    """Generate a random prime number."""
    while True:
        num = random.randint(100, 1000)
        if is_prime(num):
            return num

def gcd(a, b):
    """Compute the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Compute the modular inverse of e modulo phi."""
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa_keygen():
    """Generate RSA public and private keys."""
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def rsa_encrypt(message, public_key):
    """Encrypt a message using RSA."""
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def rsa_decrypt(encrypted_message, private_key):
    """Decrypt a message using RSA."""
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

def main():
    """Main function to demonstrate RSA encryption and decryption."""
    public_key, private_key = rsa_keygen()
    message = "Hello, RSA!"
    print(f"Original Message: {message}")
    
    encrypted_message = rsa_encrypt(message, public_key)
    print(f"Encrypted Message: {encrypted_message}")
    
    decrypted_message = rsa_decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == '__main__':
    main()
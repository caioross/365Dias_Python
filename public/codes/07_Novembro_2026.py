import json
import random
import string

def generate_random_name():
    """Generate a random name."""
    first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_email():
    """Generate a random email address."""
    letters = string.ascii_lowercase
    domain = "@example.com"
    username = ''.join(random.choice(letters) for i in range(8))
    return username + domain

def generate_random_phone():
    """Generate a random phone number."""
    return ''.join(random.choice(string.digits) for i in range(10))

def generate_random_user():
    """Generate a random user profile."""
    return {
        "name": generate_random_name(),
        "email": generate_random_email(),
        "phone": generate_random_phone()
    }

def generate_users(num_users):
    """Generate a list of random user profiles."""
    return [generate_random_user() for _ in range(num_users)]

def save_users_to_json(users, filename):
    """Save the list of users to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(users, file, indent=4)

def main():
    """Main function to generate and save user profiles."""
    num_users = 500
    users = generate_users(num_users)
    save_users_to_json(users, 'massa_usuarios.json')
    print(f"Generated {num_users} user profiles and saved to 'massa_usuarios.json'.")

if __name__ == '__main__':
    main()
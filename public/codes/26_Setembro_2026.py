import hashlib
import random

def generate_color():
    """Generate a random hex color."""
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))

def generate_shape(name):
    """Generate a geometric shape based on the hash of the name."""
    # Create a hash of the name to ensure reproducibility
    hash_object = hashlib.sha256(name.encode())
    hex_dig = hash_object.hexdigest()
    
    # Use the hash to determine the shape
    shape_index = int(hex_dig, 16) % 3  # 0: Circle, 1: Square, 2: Triangle
    
    if shape_index == 0:
        return "Circle"
    elif shape_index == 1:
        return "Square"
    else:
        return "Triangle"

def generate_avatar(name):
    """Generate an avatar description based on the user's name."""
    shape = generate_shape(name)
    color = generate_color()
    return f"Avatar: {shape} colored {color}"

def main():
    """Main function to execute the avatar generation."""
    user_name = input("Enter your name to generate an avatar: ")
    avatar = generate_avatar(user_name)
    print(avatar)

if __name__ == '__main__':
    main()
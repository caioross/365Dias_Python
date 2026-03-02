import random
import string
from faker import Faker

def generate_random_name():
    """
    Generates a random full name using the Faker library.
    
    Returns:
        str: A full name consisting of a first and last name.
    """
    fake = Faker()
    return fake.name()

def generate_random_address():
    """
    Generates a random address using the Faker library.
    
    Returns:
        str: A full address consisting of street address, city, state, and zip code.
    """
    fake = Faker()
    return fake.address().replace('\n', ', ')

def generate_random_cpf():
    """
    Generates a random CPF (Brazilian individual taxpayer registry) number.
    
    Returns:
        str: A CPF number in the format 'xxx.xxx.xxx-xx'.
    """
    def _generate_digits():
        return ''.join(random.choices(string.digits, k=9))
    
    def _calculate_first_digit(digit_string):
        total = sum((i + 1) * int(digit) for i, digit in enumerate(reversed(digit_string)))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)
    
    def _calculate_second_digit(digit_string):
        total = sum((i + 2) * int(digit) for i, digit in enumerate(reversed(digit_string)))
        remainder = total % 11
        return '0' if remainder < 2 else str(11 - remainder)
    
    digits = _generate_digits()
    first_digit = _calculate_first_digit(digits)
    second_digit = _calculate_second_digit(digits + first_digit)
    return f'{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{first_digit}{second_digit}'

def generate_user_data(num_users=1):
    """
    Generates a list of dictionaries containing random user data.
    
    Args:
        num_users (int): The number of user data entries to generate.
        
    Returns:
        list: A list of dictionaries, each containing 'name', 'address', and 'cpf' keys.
    """
    user_data_list = []
    for _ in range(num_users):
        user_data = {
            'name': generate_random_name(),
            'address': generate_random_address(),
            'cpf': generate_random_cpf()
        }
        user_data_list.append(user_data)
    return user_data_list

def main():
    """
    Main function to execute the script. Generates and prints random user data.
    """
    num_users = 5  # Number of users to generate
    users = generate_user_data(num_users)
    for user in users:
        print(user)

if __name__ == '__main__':
    main()
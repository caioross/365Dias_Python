import csv
import random
import string
from datetime import datetime, timedelta

def generate_random_string(length):
    """Generate a random string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_date(start_date, end_date):
    """Generate a random date between start_date and end_date."""
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def generate_random_data(num_records):
    """Generate a list of dictionaries with random data."""
    data = []
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2023, 1, 1)
    
    for _ in range(num_records):
        record = {
            'id': random.randint(1, 1000000),
            'name': generate_random_string(10),
            'email': f"{generate_random_string(8)}@{generate_random_string(5)}.com",
            'date': generate_random_date(start_date, end_date).strftime('%Y-%m-%d'),
            'amount': round(random.uniform(100.0, 10000.0), 2)
        }
        data.append(record)
    
    return data

def write_data_to_csv(data, filename):
    """Write data to a CSV file."""
    fieldnames = ['id', 'name', 'email', 'date', 'amount']
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    """Main function to generate and write random data to a CSV file."""
    num_records = 1000000  # Number of records to generate
    filename = 'massa_dados.csv'
    
    print(f"Generating {num_records} records...")
    data = generate_random_data(num_records)
    print("Data generation complete.")
    
    print(f"Writing data to {filename}...")
    write_data_to_csv(data, filename)
    print("Data writing complete.")

if __name__ == '__main__':
    main()
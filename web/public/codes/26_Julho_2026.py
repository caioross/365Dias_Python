import random
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_customer_data(num_customers):
    """
    Generate a list of fake customer data.

    :param num_customers: Number of customers to generate
    :return: List of dictionaries containing customer data
    """
    customers = []
    for _ in range(num_customers):
        customer = {
            'customer_id': fake.uuid4(),
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address().replace('\n', ', '),
            'phone_number': fake.phone_number()
        }
        customers.append(customer)
    return customers

def generate_product_data(num_products):
    """
    Generate a list of fake product data.

    :param num_products: Number of products to generate
    :return: List of dictionaries containing product data
    """
    products = []
    for _ in range(num_products):
        product = {
            'product_id': fake.uuid4(),
            'name': fake.word(),
            'description': fake.sentence(nb_words=6),
            'price': round(random.uniform(10.0, 1000.0), 2),
            'stock': random.randint(0, 100)
        }
        products.append(product)
    return products

def generate_order_data(customers, products, num_orders):
    """
    Generate a list of fake order data.

    :param customers: List of customer dictionaries
    :param products: List of product dictionaries
    :param num_orders: Number of orders to generate
    :return: List of dictionaries containing order data
    """
    orders = []
    for _ in range(num_orders):
        customer = random.choice(customers)
        product = random.choice(products)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        quantity = random.randint(1, min(10, product['stock']))

        order = {
            'order_id': fake.uuid4(),
            'customer_id': customer['customer_id'],
            'product_id': product['product_id'],
            'order_date': order_date.strftime('%Y-%m-%d'),
            'quantity': quantity,
            'total_price': round(quantity * product['price'], 2)
        }
        orders.append(order)
    return orders

def main():
    num_customers = 100
    num_products = 500
    num_orders = 1000

    customers = generate_customer_data(num_customers)
    products = generate_product_data(num_products)
    orders = generate_order_data(customers, products, num_orders)

    # Print generated data
    print("Customers:")
    for customer in customers:
        print(customer)

    print("\nProducts:")
    for product in products:
        print(product)

    print("\nOrders:")
    for order in orders:
        print(order)

if __name__ == '__main__':
    main()
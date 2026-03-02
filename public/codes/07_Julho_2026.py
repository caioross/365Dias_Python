import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def fetch_product_price(url):
    """
    Fetches the product price from the given URL.
    
    Args:
    url (str): The URL of the product page.
    
    Returns:
    float: The price of the product.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Assuming the price is in a <span> with class 'price'
    price_element = soup.find('span', class_='price')
    if price_element:
        price = float(price_element.text.replace('R$', '').replace(',', '.').strip())
        return price
    return None

def send_email(subject, body, to_email):
    """
    Sends an email with the given subject and body to the specified email address.
    
    Args:
    subject (str): The subject of the email.
    body (str): The body of the email.
    to_email (str): The recipient's email address.
    """
    from_email = "your_email@example.com"
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(from_email, "your_password")
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    """
    Main function to monitor the price of a product and send an email notification if the price drops.
    """
    product_url = "http://example.com/product"
    target_price = 100.00  # Target price to monitor
    recipient_email = "recipient@example.com"
    
    current_price = fetch_product_price(product_url)
    if current_price is not None and current_price < target_price:
        subject = "Price Drop Alert!"
        body = f"The price of the product has dropped to R${current_price:.2f}."
        send_email(subject, body, recipient_email)
        print("Email sent successfully.")
    else:
        print("Price is above the target or unable to fetch the price.")

if __name__ == '__main__':
    main()
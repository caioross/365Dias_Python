import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import whois
import datetime

def load_sites(file_path):
    """
    Load a list of websites from a file.
    
    Args:
        file_path (str): Path to the file containing the list of websites.
    
    Returns:
        list: List of websites.
    """
    with open(file_path, 'r') as file:
        sites = file.read().splitlines()
    return sites

def check_expiration(site):
    """
    Check the expiration date of a domain.
    
    Args:
        site (str): The domain to check.
    
    Returns:
        datetime: The expiration date of the domain.
    """
    try:
        w = whois.whois(site)
        return w.expiration_date
    except Exception as e:
        print(f"Error checking {site}: {e}")
        return None

def send_email(subject, body, to_email):
    """
    Send an email with the given subject and body to the specified email address.
    
    Args:
        subject (str): The subject of the email.
        body (str): The body of the email.
        to_email (str): The recipient's email address.
    """
    from_email = "your_email@example.com"
    password = "your_password"
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """
    Main function to monitor domain expirations and send emails if necessary.
    """
    sites = load_sites('sites.txt')
    threshold_days = 30  # Number of days before expiration to send a warning
    to_email = "recipient@example.com"
    
    for site in sites:
        expiration_date = check_expiration(site)
        if expiration_date:
            days_until_expiration = (expiration_date - datetime.datetime.now()).days
            if days_until_expiration <= threshold_days:
                subject = f"Domain {site} is expiring soon!"
                body = f"The domain {site} will expire in {days_until_expiration} days."
                send_email(subject, body, to_email)

if __name__ == '__main__':
    main()
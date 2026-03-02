import imaplib
import email
from email.policy import default
import os

def connect_to_email_account(email_address, password, imap_server):
    """
    Connects to an email account using IMAP.

    :param email_address: The email address to connect with.
    :param password: The password for the email account.
    :param imap_server: The IMAP server address.
    :return: An IMAP4_SSL object connected to the email account.
    """
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_address, password)
    mail.select('inbox')
    return mail

def fetch_emails_from_sender(mail, sender_email):
    """
    Fetches all emails from a specific sender.

    :param mail: An IMAP4_SSL object connected to the email account.
    :param sender_email: The email address of the sender.
    :return: A list of email messages from the sender.
    """
    status, messages = mail.search(None, f'FROM "{sender_email}"')
    if status != 'OK':
        raise Exception("Failed to fetch emails")
    
    email_ids = messages[0].split()
    emails = []
    for e_id in email_ids:
        status, msg_data = mail.fetch(e_id, '(RFC822)')
        if status != 'OK':
            raise Exception("Failed to fetch email data")
        emails.append(email.message_from_bytes(msg_data[0][1], policy=default))
    return emails

def save_attachments(email_message, download_directory):
    """
    Saves all attachments from an email message to a specified directory.

    :param email_message: An email message object.
    :param download_directory: The directory to save the attachments.
    """
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    for part in email_message.iter_parts():
        if part.is_attachment():
            filename = part.get_filename()
            if filename:
                filepath = os.path.join(download_directory, filename)
                with open(filepath, 'wb') as f:
                    f.write(part.get_payload(decode=True))
                print(f"Attachment saved: {filepath}")

def main():
    """
    Main function to connect to an email account, fetch emails from a specific sender,
    and save their attachments.
    """
    email_address = 'your_email@example.com'
    password = 'your_password'
    imap_server = 'imap.example.com'
    sender_email = 'sender@example.com'
    download_directory = 'downloaded_attachments'

    try:
        mail = connect_to_email_account(email_address, password, imap_server)
        emails = fetch_emails_from_sender(mail, sender_email)
        for email_message in emails:
            save_attachments(email_message, download_directory)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        mail.logout()

if __name__ == '__main__':
    main()
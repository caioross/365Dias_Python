import requests
from bs4 import BeautifulSoup
import re

def extract_social_links(url):
    """
    Extracts social media links (Instagram, Twitter, LinkedIn) from a given website.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        dict: A dictionary containing the social media links found.
    """
    social_media_links = {
        'instagram': None,
        'twitter': None,
        'linkedin': None
    }

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Regular expressions to find social media links
        patterns = {
            'instagram': r'(https?://(www\.)?instagram\.com/[\w\.]+)',
            'twitter': r'(https?://(www\.)?twitter\.com/[\w\.]+)',
            'linkedin': r'(https?://(www\.)?linkedin\.com/in/[\w\-]+)'
        }

        for platform, pattern in patterns.items():
            match = re.search(pattern, soup.get_text())
            if match:
                social_media_links[platform] = match.group(0)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    return social_media_links

def main():
    """
    Main function to execute the script.
    """
    url = input("Enter the URL of the institutional website: ")
    links = extract_social_links(url)
    print("Extracted Social Media Links:")
    for platform, link in links.items():
        print(f"{platform.capitalize()}: {link}")

if __name__ == '__main__':
    main()
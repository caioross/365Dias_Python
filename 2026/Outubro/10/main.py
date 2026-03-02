import requests
from bs4 import BeautifulSoup
import re

def extract_js_files(url):
    """
    Extracts all external JavaScript files from a given website.

    Args:
        url (str): The URL of the website to analyze.

    Returns:
        list: A list of URLs pointing to external JavaScript files.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    js_files = []

    # Find all script tags with src attribute
    for script in soup.find_all('script', src=True):
        js_files.append(script['src'])

    return js_files

def main():
    """
    Main function to execute the script.
    """
    url = input("Enter the URL of the website to analyze: ")
    js_files = extract_js_files(url)

    if js_files:
        print("External JavaScript files found:")
        for js_file in js_files:
            print(js_file)
    else:
        print("No external JavaScript files found.")

if __name__ == '__main__':
    main()
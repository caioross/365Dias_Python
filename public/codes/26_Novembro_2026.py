import requests
from bs4 import BeautifulSoup

def fetch_url_content(url):
    """
    Fetches the content of a given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

def check_alt_tags(soup):
    """
    Checks if all image tags have an alt attribute.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the HTML content.

    Returns:
        bool: True if all images have an alt attribute, False otherwise.
    """
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            return False
    return True

def check_header_structure(soup):
    """
    Checks if the header structure is sequential (h1, h2, h3, etc.).

    Args:
        soup (BeautifulSoup): The BeautifulSoup object containing the HTML content.

    Returns:
        bool: True if the header structure is sequential, False otherwise.
    """
    headers = [tag.name for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    expected_headers = []
    current_level = 1
    for header in headers:
        while current_level < int(header[1]):
            expected_headers.append(f'h{current_level}')
            current_level += 1
        expected_headers.append(header)
        current_level = int(header[1])
    return headers == expected_headers

def main():
    url = input("Enter the URL to check for accessibility: ")
    content = fetch_url_content(url)
    if content:
        soup = BeautifulSoup(content, 'html.parser')
        alt_tags_check = check_alt_tags(soup)
        header_structure_check = check_header_structure(soup)
        print(f"All images have alt tags: {alt_tags_check}")
        print(f"Header structure is sequential: {header_structure_check}")

if __name__ == '__main__':
    main()
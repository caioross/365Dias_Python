import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_links(url):
    """
    Fetches all links from a given URL.

    :param url: The URL to fetch links from.
    :return: A list of links.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, a.get('href')) for a in soup.find_all('a', href=True)]
        return links
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def check_broken_links(links):
    """
    Checks which links in the list return a 404 status code.

    :param links: A list of URLs to check.
    :return: A list of broken links.
    """
    broken_links = []
    for link in links:
        try:
            response = requests.head(link, allow_redirects=True)
            if response.status_code == 404:
                broken_links.append(link)
        except requests.RequestException as e:
            print(f"Error checking {link}: {e}")
    return broken_links

def main():
    """
    Main function to execute the script.
    """
    url = input("Enter the URL to scan for broken links: ")
    links = fetch_links(url)
    if links:
        print(f"Found {len(links)} links on the page.")
        broken_links = check_broken_links(links)
        if broken_links:
            print(f"Found {len(broken_links)} broken links:")
            for link in broken_links:
                print(link)
        else:
            print("No broken links found.")
    else:
        print("No links found on the page.")

if __name__ == '__main__':
    main()
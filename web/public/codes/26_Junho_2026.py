import requests
from bs4 import BeautifulSoup

def fetch_page_content(url):
    """
    Fetches the content of a web page.

    :param url: The URL of the web page to fetch.
    :return: The content of the web page as a string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def extract_comments(html_content):
    """
    Extracts comments from the HTML content of a blog page.

    :param html_content: The HTML content of the web page.
    :return: A list of comments found on the page.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    comments = []
    # Assuming comments are within <div> tags with class 'comment'
    for comment_div in soup.find_all('div', class_='comment'):
        comment_text = comment_div.get_text(strip=True)
        comments.append(comment_text)
    return comments

def main():
    """
    Main function to execute the script.
    Fetches the blog page content and extracts comments.
    """
    blog_url = 'https://exampleblog.com/posts/1'  # Replace with the actual blog URL
    page_content = fetch_page_content(blog_url)
    if page_content:
        comments = extract_comments(page_content)
        for i, comment in enumerate(comments, start=1):
            print(f"Comment {i}: {comment}")

if __name__ == '__main__':
    main()
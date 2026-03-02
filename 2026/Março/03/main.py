import feedparser

def fetch_rss_titles(url):
    """
    Fetches and returns the titles of the latest news from an RSS feed.

    Args:
        url (str): The URL of the RSS feed.

    Returns:
        list: A list of titles from the RSS feed.
    """
    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries]
    return titles

def main():
    """
    Main function to execute the RSS feed title fetching and display.
    """
    rss_url = 'https://example.com/rss'  # Replace with a valid RSS feed URL
    try:
        titles = fetch_rss_titles(rss_url)
        print("Latest News Titles:")
        for title in titles:
            print(title)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
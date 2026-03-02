import feedparser

def fetch_rss_feed(url):
    """
    Fetches the RSS feed from the given URL.

    Args:
        url (str): The URL of the RSS feed.

    Returns:
        feedparser.FeedParserDict: The parsed RSS feed.
    """
    return feedparser.parse(url)

def display_headlines(feed):
    """
    Displays the headlines from the RSS feed in a clean and readable format.

    Args:
        feed (feedparser.FeedParserDict): The parsed RSS feed.
    """
    print("Latest News Headlines:")
    for entry in feed.entries:
        print(f"- {entry.title}")

def main():
    """
    Main function to execute the RSS feed reader.
    """
    rss_url = 'https://example.com/rss'  # Replace with the actual RSS feed URL
    news_feed = fetch_rss_feed(rss_url)
    display_headlines(news_feed)

if __name__ == '__main__':
    main()
import feedparser
import csv
from datetime import datetime

# Function to fetch and parse RSS feed
def parse_rss_feed(rss_url):
    feed = feedparser.parse(rss_url)
    entries = []
    for entry in feed.entries:
        title = entry.title
        link = entry.link
        published = entry.published_parsed
        published_str = datetime(*published[:6]).strftime('%Y-%m-%d %H:%M:%S')
        if 'description' in entry:
            summary = entry.description
        else:
            summary = ''
        entries.append({'Title': title, 'Link': link, 'Published': published_str, 'Summary': summary})
    return entries

# Function to write RSS data to CSV
def write_to_csv(entries, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Title', 'Link', 'Published', 'Summary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

# Example RSS feed URL
rss_url = 'https://www.investing.com/rss/news_11.rss'
# Parse RSS feed
entries = parse_rss_feed(rss_url)

# Write RSS data to CSV
write_to_csv(entries, 'rss_feed.csv')

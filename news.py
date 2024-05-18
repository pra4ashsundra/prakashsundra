import requests
from bs4 import BeautifulSoup
import csv

def scrape_investing_gold_news(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    # Send a GET request to the specified URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page with status code {response.status_code}")
        return
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the news container
    news_container = soup.find('div', {'class': 'mediumTitle1'})
    if not news_container:
        print("News container not found")
        return
    
    # Find all news articles
    articles = news_container.find_all('div', {'class': 'textDiv'})
    news_data = []

    for article in articles:
        # Extract the title
        title_tag = article.find('a', {'class': 'title'})
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.investing.com" + title_tag['href']
            summary_tag = article.find('p')
            summary = summary_tag.get_text(strip=True) if summary_tag else "No summary"
            date_tag = article.find('span', {'class': 'date'})
            published_date = date_tag.get_text(strip=True) if date_tag else "No date"
            news_data.append([title, link, published_date, summary])
    
    # Save the news data to a CSV file
    with open('gold_news.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link', 'Published Date', 'Summary'])
        writer.writerows(news_data)

    print(f"Scraped {len(news_data)} articles and saved to gold_news.csv")

if __name__ == "__main__":
    investing_gold_news_url = 'https://www.investing.com/commodities/gold-news'
    scrape_investing_gold_news(investing_gold_news_url)

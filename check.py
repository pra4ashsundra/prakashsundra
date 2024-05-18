import requests
from bs4 import BeautifulSoup

def scrape_gold_price():
    # URL of the website where gold prices are listed
    url = "https://www.tradingview.com/symbols/XAUUSD/"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the element containing the gold price
        gold_price_element = soup.find('span', class_='gold-price')
        
        # Check if gold_price_element exists
        if gold_price_element:
            # Extract the text containing the gold price
            gold_price = gold_price_element.text.strip()
            return gold_price
        else:
            print("Failed to find element with class 'gold-price'.")
            return None
    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)
        return None

# Call the function to scrape gold price
gold_price = scrape_gold_price()

# Print the scraped gold price
if gold_price:
    print("Today's gold price is:", gold_price)
else:
    print("Failed to retrieve gold price.")

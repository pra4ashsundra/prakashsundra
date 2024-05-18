import requests
from bs4 import BeautifulSoup

url = "https://www.investing.com/commodities/gold"

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        price_element = soup.find('div', {'class': 'text-5xl/9', 'data-test': 'instrument-price-last'})
        if price_element:
            gold_price = price_element.text.strip()
            print("Real-time Gold Price:", gold_price)
        else:
            print("Failed to find the gold price element on the webpage.")
    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)
except Exception as e:
    print("An error occurred:", e)

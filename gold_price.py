import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.investing.com/commodities/gold"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element containing the gold price
        price_element = soup.find('div', {'class': 'text-5xl/9', 'data-test': 'instrument-price-last'})

        # Check if the price element is found
        if price_element:
            # Extract the gold price text
            gold_price = price_element.text.strip()
            print("Real-time Gold Price:", gold_price)
        else:
            print("Failed to find the gold price element on the webpage.")

    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)

import requests
from bs4 import BeautifulSoup

# Function to update the gold price in the HTML file
def update_html_with_gold_price(price):
    with open('index.html', 'r') as file:
        html_content = file.read()

    # Replace the placeholder with the latest gold price
    updated_html = html_content.replace('<span id="gold-price-placeholder"></span>', str(price))

    # Write the updated HTML content back to the file
    with open('index.html', 'w') as file:
        file.write(updated_html)

# URL of the website to scrape
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
            # Extract the gold price
            gold_price = price_element.text.strip()
            
            # Update the HTML file with the latest gold price
            update_html_with_gold_price(gold_price)
            print("Successfully updated HTML with the latest gold price.")
        else:
            print("Failed to find the gold price element on the webpage.")
    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)
except Exception as e:
    print("An error occurred:", e)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the Investing.com gold news page
driver.get("https://www.investing.com/commodities/gold-news")

# Wait for the page to load
time.sleep(5)

# Perform Ctrl+A to select all content
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'a')

# Perform Ctrl+S to save the page
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 's')

# Wait for the file to download (You may need to adjust this time depending on your internet speed)
time.sleep(5)

# Parse the downloaded HTML file to extract links
html_filename = 'gold_news.html'  # Assuming the downloaded file name is gold_news.html
with open(html_filename, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    links = soup.find_all('a', href=True)

# Extract and sort the URLs by the latest
parsed_links = []
for link in links:
    url = link['href']
    # Exclude internal links and anchors
    if url.startswith('http'):
        parsed_links.append(url)

# Sort the links by the latest
parsed_links.sort(key=lambda x: time.strptime(x, '%Y-%m-%d'))

# Join the links into a single string
links_text = '\n'.join(parsed_links)

# Open ChatGPT and ask for the sorted links
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="Give me only the links sorted from the latest:\n" + links_text,
  temperature=0,
  max_tokens=100
)

# Print the response
print(response.choices[0].text.strip())

# Close the browser
driver.quit()

# First, install these libraries using:
# pip install requests beautifulsoup4

# Import the required libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Download a webpage
url = "https://quotes.toscrape.com"  # This is a practice website for scraping
response = requests.get(url)

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find elements you want
# Let's find all quotes on the page
quotes = soup.find_all('span', class_='text')

# Step 4: Extract and print the data
for quote in quotes:
    print(quote.text)
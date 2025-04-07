import requests
from bs4 import BeautifulSoup

# URL of the site
url = 'https://quotes.toscrape.com/'

# Send a request to the site
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quote containers
quotes = soup.find_all('div', class_='quote')

# Loop through each quote
for quote in quotes:
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

    print(f"Quote: {text}")
    print(f"Author: {author}")
    print(f"Tags: {', '.join(tags)}")
    print('---')

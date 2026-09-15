# Day 32: web scraping with BeautifulSoup
# install: pip install beautifulsoup4 requests

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
for q in quotes[:5]:
    print(q.text)
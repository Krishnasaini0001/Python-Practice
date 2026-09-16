# Day 33: scrape and save structured data

import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes_data = []
for quote_block in soup.find_all("div", class_="quote"):
    text = quote_block.find("span", class_="text").text
    author = quote_block.find("small", class_="author").text
    quotes_data.append({"quote": text, "author": author})

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(quotes_data)

print(f"Saved {len(quotes_data)} quotes to quotes.csv")
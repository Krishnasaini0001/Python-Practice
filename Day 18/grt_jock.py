# Day 18: your first external library
# install first: pip install requests

import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()

print(joke["setup"])
print(joke["punchline"])
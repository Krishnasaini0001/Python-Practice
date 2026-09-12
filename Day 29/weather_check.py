# Day 31: fetching real data from a public API

import requests

city_lat, city_lon = 23.2599, 77.4126  # example coordinates

url = f"https://api.open-meteo.com/v1/forecast?latitude={city_lat}&longitude={city_lon}&current_weather=true"
response = requests.get(url)
data = response.json()

temp = data["current_weather"]["temperature"]
print(f"Current temperature: {temp}°C")
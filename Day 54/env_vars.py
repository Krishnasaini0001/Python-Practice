# Day 54: keeping secrets out of code with environment variables
# install: pip install python-dotenv

import os
from dotenv import load_dotenv

load_dotenv()  # reads from a .env file (never commit that file!)

api_key = os.getenv("API_KEY", "not set")
print(f"API key loaded: {api_key}")
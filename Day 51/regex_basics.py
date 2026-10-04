# Day 51: regular expressions

import re

text = "Contact us at hello@example.com or admin@test.org"

emails = re.findall(r"[\w.-]+@[\w.-]+", text)
print(f"Found emails: {emails}")

phone = "Call 555-123-4567 now"
match = re.search(r"\d{3}-\d{3}-\d{4}", phone)
print(f"Phone found: {match.group() if match else 'none'}")
# Day 13: json module

import json

data = {"name": "Alex", "score": 95, "passed": True}

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)

print(loaded)
import json

with open('links.json') as f:
    r = json.load(f)

print([el.get("link") for el in r])

import requests

URL = "http://localhost:8000/stuinfo/3"

r = requests.get(url = URL)

data = r.json()

print(data)
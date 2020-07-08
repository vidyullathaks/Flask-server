import requests

data = requests.get("http://localhost:8000/test")

print(data.content)
import requests
import json

url = "http://127.0.0.1:5000/translate/english-to-french"
headers = {
    "Content-Type": "application/json"
}
data = {
    "text": "Hello, how are you?"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

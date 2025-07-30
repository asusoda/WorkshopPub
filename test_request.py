import requests

url = "http://127.0.0.1:5000/two_sum"
payload = {
    "nums": [2, 7, 11, 15],
    "target": 9
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "montant": 2500,
    "score_risque_client": 0.78,
    "devise": "EUR",
    "type_transaction": "online",
    "canal": "mobile"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())

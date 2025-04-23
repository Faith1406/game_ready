import requests

response = requests.post(
    "https://gameready-production.up.railway.app/generate",
    json={"prompt": "Give me a startup idea"},
)

print(response.json())

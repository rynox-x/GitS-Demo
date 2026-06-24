import requests

url = "https://example.com"

# SSL verification disabled
requests.get(url, verify=False)

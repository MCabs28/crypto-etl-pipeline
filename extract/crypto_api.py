import requests

URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids=bitcoin,ethereum"
    "&vs_currencies=usd"
    "&include_market_cap=true"
    "&include_24hr_vol=true"
)

def fetch_crypto_data():
    response = requests.get(URL)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"API Error: {response.status_code}")
import requests
from constants import COINS
from logs.logger import logger

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"


def fetch_crypto_data():
    try:
        coin_ids = ",".join(COINS)
        params = {
            "ids": coin_ids,
            "vs_currencies": "usd",
            "include_market_cap": "true",
            "include_24hr_vol": "true",
        }

        response = requests.get(BASE_URL, params=params)

        response.raise_for_status()
        logger.info("Succesfully fetched cryptocurrency data")
        return response.json()

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch cryptocurrency data: {e}")
        raise

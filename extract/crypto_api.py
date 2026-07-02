import requests
from constants import COINS
from logs.logger import logger
from tenacity import retry, stop_after_attempt, wait_exponential, before_sleep_log
import logging

BASE_URL = "https://api.coingecko.com/api/v3/simple/price"


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
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

from logs.logger import logger


def validate_crypto_data(data):
    """
    Validate the cryptocurrency data returned by the API.
    """

    required_fields = ["usd", "usd_market_cap", "usd_24h_vol"]

    for coin, values in data.items():

        for field in required_fields:
            if field not in values:
                raise ValueError(f"{coin}: Missing field '{field}'")
            if values[field] is None:
                raise ValueError(f"{coin}: '{field}' cannot be None")
            if not isinstance(values[field], (int, float)):
                raise ValueError(f"{coin}: '{field}' must be numeric")
            if values[field] < 0:
                raise ValueError(f"{coin}: '{field}' cannot be negative")
            logger.info("Data validation passed.")

import json
from extract.crypto_api import fetch_crypto_data
from load.load_db import insert_crypto
from logs.logger import logger


def main():
    try:
        logger.info("Starting Crypto ETL Pipeline...")

        data = fetch_crypto_data()

        logger.info("Fetching cryptocurrency data...")
        logger.info(json.dumps(data, indent=4))

        rows = insert_crypto(data)

        logger.info(f"Successfully inserted {rows} records.")

        logger.info("Pipeline completed successfully.")

    except Exception:
        logger.exception("Pipeline failed.")


if __name__ == "__main__":
    main()

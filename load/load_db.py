from datetime import datetime

from config.constants import SYMBOLS
from load.db_connection import get_connection
from logs.logger import logger


def insert_crypto(data):
    conn = None

    try:
        logger.info("Connecting to PostgreSQL...")
        conn = get_connection()

        logger.info("Connected successfully.")

        cursor = conn.cursor()

        inserted_rows = 0

        for coin, values in data.items():
            logger.info(f"Inserting {coin}...")

            cursor.execute(
                """
                INSERT INTO crypto_prices
                (coin_name, symbol, price_usd, market_cap, total_volume, fetched_at)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    coin,
                    SYMBOLS[coin],
                    values["usd"],
                    values["usd_market_cap"],
                    values["usd_24h_vol"],
                    datetime.now(),
                ),
            )

            inserted_rows += 1

        conn.commit()

        logger.info("Database transaction committed successfully.")

        return inserted_rows

    except Exception:
        if conn:
            conn.rollback()

        raise

    finally:
        logger.info("Closing database connection.")

        if conn:
            cursor.close()
            conn.close()

from load.db_connection import get_connection
from datetime import datetime

def insert_crypto(data):
    conn = get_connection()
    cursor = conn.cursor()

    SYMBOLS = {
        "bitcoin": "BTC",
        "ethereum": "ETH"
    }
    
    for coin, values in data.items():
        cursor.execute(
                 """ 
                INSERT INTO crypto_prices
                (coin_name,symbol,price_usd,market_cap,total_volume,fetched_at)
                VALUES(%s, %s, %s, %s, %s, %s)
                """, 
                (
                    coin,
                    SYMBOLS[coin],
                    values["usd"],
                    values["usd_market_cap"],
                    values["usd_24h_vol"],
                    datetime.now()
                ),
        )
    conn.commit()
    cursor.close()
    conn.close()
        
SELECT
    coin_name,
    symbol,
    price_usd,
    market_cap,
    total_volume,
    fetched_at
FROM {{ source('crypto_db', 'crypto_prices') }}
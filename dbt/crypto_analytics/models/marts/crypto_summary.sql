SELECT
    coin_name,
    {{ average_price('price_usd') }} AS average_price,
    MAX(price_usd) AS highest_price,
    MIN(price_usd) AS lowest_price,
    COUNT(*) AS total_records
FROM {{ ref('stg_crypto_prices') }}
GROUP BY coin_name
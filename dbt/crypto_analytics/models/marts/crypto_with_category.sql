SELECT
    p.coin_name,
    p.symbol,
    p.price_usd,
    p.market_cap,
    p.total_volume,
    p.fetched_at,
    c.category
FROM {{ ref('stg_crypto_prices') }} AS p
LEFT JOIN {{ ref('coin_categories') }} AS c
    ON LOWER(p.symbol) = LOWER(c.symbol)
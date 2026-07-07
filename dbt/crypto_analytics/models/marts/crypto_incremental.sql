{{ config(
    materialized='incremental'
) }}

SELECT
    coin_name,
    symbol,
    price_usd,
    market_cap,
    total_volume,
    fetched_at
FROM {{ ref('stg_crypto_prices') }}

{% if is_incremental() %}

WHERE fetched_at >
(
    SELECT MAX(fetched_at)
    FROM {{ this }}
)

{% endif %}
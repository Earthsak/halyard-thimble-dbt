

With source as (

   Select * from {{ source('ht_erp', 'products') }}
),

standardize_stg_products as  (

    SELECT
        product_code,
        legacy_code,
        product_name,
        upper(product_line) as product_line,
        cast(list_price_cad as decimal) as list_price_cad,
        cast(standard_cost_cad as decimal) as standard_cost_cad,
        cast(code_migrated_on as date) as code_migrated_on

    FROM source
    
)
Select * from standardize_stg_products


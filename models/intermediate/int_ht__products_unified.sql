

with products as (
    select * from {{ ref('stg_ht__products') }}
),
by_current_code as (
       
        Select
        product_code as lookup_code,
        product_code,
        product_name,
        product_line,
        list_price_cad,
        standard_cost_cad
    from products
), 
by_legacy_code as (

     select
        legacy_code as lookup_code,
        product_code,
        product_name,
        product_line,
        list_price_cad,
        standard_cost_cad
    from products
    where legacy_code is not null
    and legacy_code not in (select product_code from products)
),

unified as (
    select * from by_current_code
    union all
    select * from by_legacy_code
)
select * from unified
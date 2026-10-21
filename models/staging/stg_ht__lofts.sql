

With source as (

   Select * from {{ source('ht_erp', 'lofts') }}
),

standardize_stg_lofts as (

    SELECT
        upper(loft_id) as loft_id,
        loft_name,
        home_water,
        timezone,
        cast(opened_on as date) as opened_on
    FROM source
    
)
Select * from standardize_stg_lofts


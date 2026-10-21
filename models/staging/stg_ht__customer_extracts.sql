

With source as (

   Select * from {{ source('ht_erp', 'customer_extracts') }}
),

standardize_stg_customer_extracts as  (

    SELECT
        cast(extract_date as date) as extract_date, 
        customer_id,
        customer_name,
        upper(customer_kind) as customer_kind,
        upper(berth_class) as berth_class,
        upper(home_water) as home_water,
        cast(created_at AS TIMESTAMP) AS created_at,
        cast(updated_at AS TIMESTAMP) AS updated_at,
        cast(_loaded_at AS TIMESTAMP) AS loaded_at
    FROM source
)
Select * from standardize_stg_customer_extracts


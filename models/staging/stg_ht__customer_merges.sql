

With source as (

   Select * from {{ source('ht_erp', 'customer_merges') }}
),

standardize_stg_customer_merges as  (

    SELECT 
        retired_customer_id,
        surviving_customer_id,
        cast(merged_at AS TIMESTAMP) AS merged_at,
        merge_reason
    FROM source
)
Select * from standardize_stg_customer_merges


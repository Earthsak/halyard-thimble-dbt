

With source as (

   Select * from {{ source('ht_erp', 'tickets') }}
),

standardize_stg_tickets as  (

    SELECT
        ticket_id,
        customer_id,
        channel,
        selling_loft_id,
        fulfilling_loft_id,
        cast(ordered_at AS TIMESTAMP) AS ordered_at,
        order_kind,
        cast(_loaded_at AS TIMESTAMP) AS loaded_at
    FROM source
)
Select * from standardize_stg_tickets


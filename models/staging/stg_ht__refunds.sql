

With source as (

   Select * from {{ source('ht_erp', 'refunds') }}
),

standardize_stg_refunds as  (

    SELECT
        refund_id,
        ticket_id,
        cast(line_no as integer) as line_no,
        cast(refunded_at AS TIMESTAMP) AS refunded_at,
        cast(refund_amount as decimal) as refund_amount,
        refund_reason,
        cast(_loaded_at AS TIMESTAMP) AS loaded_at
    FROM source
    
)
Select * from standardize_stg_refunds


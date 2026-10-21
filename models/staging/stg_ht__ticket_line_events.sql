

With source as (

   Select * from {{ source('ht_erp', 'ticket_line_events') }}
),

fresh_entry as (

        Select * ,
         row_number() over( partition by ticket_id, line_no order by cast(event_id as integer) desc ) as rn
         from source
),

standardize_stg_ticket_line_events as  (

    SELECT
        event_id,
        ticket_id,
        cast(line_no as integer) as line_no,
        product_code,
        cast(quantity as integer) as quantity,
        cast(unit_price as decimal) as unit_price,
        cast(discount_pct as decimal) as discount_pct,
        upper(line_status) as line_status,
        cast(is_deleted as boolean) as is_deleted,
        cast(_loaded_at AS TIMESTAMP) AS loaded_at
    FROM fresh_entry
    where rn = 1
)
Select * from standardize_stg_ticket_line_events



With tickets as (
    select * from {{ ref('stg_ht__tickets') }}
),
ticket_lines as (
    select * from {{ ref('stg_ht__ticket_line_events') }}
    where line_status = 'FULFILLED'
    and is_deleted = false
),
lofts as (
    select * from {{ ref('stg_ht__lofts') }}
),

merged as (
    
 Select tl.event_id,
        tl.ticket_id,
        tl.line_no,
        tl.product_code,
        tl.quantity,
        tl.unit_price,
        tl.discount_pct,
        tl.line_status,
        t.customer_id,
        t.channel,
        t.selling_loft_id,
        t.fulfilling_loft_id,
        t.order_kind,
        l.timezone as selling_loft_timezone,
        (case when t.channel = 'web' then cast(t.ordered_at at time zone 'UTC' at time zone 'America/Toronto' as date)
            else cast(t.ordered_at at time zone l.timezone as date)  end) as booked_date_local,
        {{ cents_revenue('tl.quantity', 'tl.unit_price', 'tl.discount_pct') }} as line_revenue_cad
        from ticket_lines tl
        inner join tickets t on tl.ticket_id = t.ticket_id
        left join lofts l on t.selling_loft_id = l.loft_id
        where t.order_kind != 'dockside'
),
exclude_bosun as (
   
    select * from merged
    where customer_id not like 'Bosun%'

)
select * from exclude_bosun
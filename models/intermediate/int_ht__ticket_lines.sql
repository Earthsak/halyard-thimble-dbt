
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

products as (
    select * from {{ ref('int_ht__products_unified') }}
),

corrected_lines as (
    select
        tl.event_id,
        tl.ticket_id,
        tl.line_no,
        tl.product_code,
        tl.quantity,
        tl.discount_pct,
        tl.line_status,
        tl.is_deleted,
        tl.loaded_at,
        case
            when p.list_price_cad is null and tl.unit_price > 10000 then tl.unit_price / 100
            when p.list_price_cad is not null and tl.unit_price > p.list_price_cad * 50  then tl.unit_price / 100 else tl.unit_price
            end as unit_price_corrected
    from ticket_lines tl
    left join products p on tl.product_code = p.lookup_code
),

merged as (
    
    select
        cl.event_id,
        cl.ticket_id,
        cl.line_no,
        cl.product_code,
        cl.quantity,
        cl.unit_price_corrected,
        cl.discount_pct,
        cl.line_status,
        t.customer_id,
        t.channel,
        t.selling_loft_id,
        t.fulfilling_loft_id,
        t.order_kind,
        l.timezone as selling_loft_timezone,
        (case
            when t.channel = 'web'
            then cast(t.ordered_at at time zone 'UTC' at time zone 'America/Toronto' as date)
            else cast(t.ordered_at at time zone l.timezone as date)
        end) as booked_date_local,
        {{ cents_revenue('cl.quantity', 'cl.unit_price_corrected', 'cl.discount_pct') }} as line_revenue_cad
    from corrected_lines cl
    inner join tickets t on cl.ticket_id = t.ticket_id
    left join lofts l on t.selling_loft_id = l.loft_id
    where t.order_kind != 'dockside'

),
exclude_bosun as (
   
    select * from merged
    where customer_id not like 'Bosun%'

)
select * from exclude_bosun
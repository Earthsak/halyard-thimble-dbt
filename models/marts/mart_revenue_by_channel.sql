{{ config(materialized='table') }}

with revenue as (
    select * from {{ ref('fct_revenue_lines') }}
),
calendar as (
    select distinct calendar_date, fiscal_period, fiscal_quarter
    from {{ ref('int_ht__fiscal_calendar') }}
),
customers as (
    select customer_id, canonical_customer_id, customer_kind, berth_class, home_water
    from {{ ref('int_ht__customers_resolved') }}
)

select
    rev.channel,
    coalesce(rev.selling_loft_id, 'WEB')     as loft_id,
    cal.fiscal_period,
    cal.fiscal_quarter,
    cust.customer_kind,
    cust.berth_class,
    cust.home_water,
    count(distinct rev.ticket_id)            as ticket_count,
    count(*)                                 as line_count,
    round(sum(rev.line_revenue_cad), 2)      as revenue_cad
from revenue rev
inner join calendar cal on rev.booked_date_local = cal.calendar_date
left join customers cust on rev.customer_id = cust.customer_id
group by 1, 2, 3, 4, 5, 6, 7
order by rev.channel, loft_id, cal.fiscal_period
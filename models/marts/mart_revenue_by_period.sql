{{ config(materialized='table') }}

with revenue as (
    select * from {{ ref('fct_revenue_lines') }}
),
calendar as (
    select distinct calendar_date, fiscal_period, fiscal_quarter, period_start, period_end
    from {{ ref('int_ht__fiscal_calendar') }}
),
lofts as (
    select loft_id, loft_name
    from {{ ref('stg_ht__lofts') }}
)

select
    cal.fiscal_period,
    cal.fiscal_quarter,
    cal.period_start,
    cal.period_end,
    coalesce(rev.selling_loft_id, 'WEB')     as loft_id,
    coalesce(l.loft_name, 'Web / Online')    as loft_name,
    rev.channel,
    count(distinct rev.ticket_id)            as ticket_count,
    count(*)                                 as line_count,
    round(sum(rev.line_revenue_cad), 2)      as revenue_cad
from revenue rev
inner join calendar cal on rev.booked_date_local = cal.calendar_date
left join lofts l on rev.selling_loft_id = l.loft_id
group by 1, 2, 3, 4, 5, 6, 7
order by cal.fiscal_period, loft_id
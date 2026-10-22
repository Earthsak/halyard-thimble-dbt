{{ config(materialized='view') }}

with period_definitions as (
    select
        fiscal_period,
        fiscal_quarter,
        period_start,
        period_weeks,
        period_start + (period_weeks * 7 - 1) as period_end
    from (values
        ('P01', 'Q1', date '2024-10-06', 4),
        ('P02', 'Q1', date '2024-11-03', 4),
        ('P03', 'Q1', date '2024-12-01', 5),
        ('P04', 'Q2', date '2025-01-05', 4),
        ('P05', 'Q2', date '2025-02-02', 4),
        ('P06', 'Q2', date '2025-03-02', 5),
        ('P07', 'Q3', date '2025-04-06', 4),
        ('P08', 'Q3', date '2025-05-04', 4),
        ('P09', 'Q3', date '2025-06-01', 5),
        ('P10', 'Q4', date '2025-07-06', 4),
        ('P11', 'Q4', date '2025-08-03', 4),
        ('P12', 'Q4', date '2025-08-31', 5)
    ) as t(fiscal_period, fiscal_quarter, period_start, period_weeks)
),
date_spine as (
    select (date '2024-10-06' + n::integer) as calendar_date
    from range(364) as t(n)
)
select
    d.calendar_date,
    'FY2026'                                                    as fiscal_year,
    p.fiscal_period,
    p.fiscal_quarter,
    p.period_start,
    p.period_end,
    p.period_weeks,
    (cast(d.calendar_date - p.period_start as integer) / 7 + 1) as fiscal_week_of_period,
    (cast(d.calendar_date - date '2024-10-06' as integer) / 7 + 1) as fiscal_week_of_year,
    (d.calendar_date = p.period_end)                            as is_last_day_of_period
from date_spine d
inner join period_definitions p
    on d.calendar_date between p.period_start and p.period_end
order by d.calendar_date
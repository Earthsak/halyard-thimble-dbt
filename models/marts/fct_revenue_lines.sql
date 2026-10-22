

{{ config(materialized='table') }}

with ticket_lines as (
    select * from {{ ref('int_ht__ticket_lines') }}
),
fy2026 as (
    select * from ticket_lines
    where booked_date_local >= '2024-10-06'
      and booked_date_local <= '2025-10-04'
)
select * from fy2026
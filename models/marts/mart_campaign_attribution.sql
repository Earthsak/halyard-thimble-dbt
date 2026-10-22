{{ config(materialized='table') }}

with touches as (
    select * from {{ ref('stg_ht__campaign_touches') }}
),
campaigns as (
    select * from {{ ref('stg_ht__campaigns') }}
),
revenue as (
    select
        ticket_id,
        count(*)                            as line_count,
        round(sum(line_revenue_cad), 2)     as ticket_revenue_cad
    from {{ ref('fct_revenue_lines') }}
    group by ticket_id
),
attributed as (
    select
        c.campaign_id,
        c.campaign_name,
        count(distinct t.ticket_id)             as touched_tickets,
        round(sum(r.ticket_revenue_cad), 2)     as attributed_revenue_cad,
        round(avg(r.ticket_revenue_cad), 2)     as avg_ticket_value_cad
    from touches t
    inner join campaigns c  on t.campaign_id  = c.campaign_id
    inner join revenue r    on t.ticket_id    = r.ticket_id
    group by c.campaign_id, c.campaign_name
)
select * from attributed
order by attributed_revenue_cad desc
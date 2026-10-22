{{ config(materialized='view') }}

with raw as (
    select * from {{ ref('stg_ht__customer_extracts') }}
),
-- Keep most recent snapshot per customer
latest as (
    select
        customer_id,
        customer_name,
        customer_kind,
        berth_class,
        home_water,
        created_at,
        updated_at,
        row_number() over (
            partition by customer_id
            order by extract_date desc
        ) as rn
    from raw
),
customers as (
    select
        customer_id, customer_name, customer_kind,
        berth_class, home_water, created_at, updated_at
    from latest
    where rn = 1
),
merges as (
    select * from {{ ref('stg_ht__customer_merges') }}
),
resolved as (
    select
        c.customer_id,
        c.customer_name,
        c.customer_kind,
        c.berth_class,
        c.home_water,
        c.created_at,
        c.updated_at,
        coalesce(m.surviving_customer_id, c.customer_id) as canonical_customer_id,
        (m.surviving_customer_id is not null)             as is_merged,
        m.merged_at,
        m.merge_reason
    from customers c
    left join merges m on c.customer_id = m.retired_customer_id
)
select * from resolved
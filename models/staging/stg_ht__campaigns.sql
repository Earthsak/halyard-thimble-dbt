

With source as (

   Select * from {{ source('ht_erp', 'campaigns') }}
),

standardize_stg_campaigns as (

    SELECT
        campaign_id,
        campaign_name,
        upper(channel) as channel,
        cast(starts_on as date) as starts_on,
        cast(ends_on as date) as ends_on,
        notes
    FROM source
    
)
Select * from standardize_stg_campaigns


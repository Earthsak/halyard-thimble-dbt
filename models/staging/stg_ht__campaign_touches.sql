

With source as (

   Select * from {{ source('ht_erp', 'campaign_touches') }}
),

standardize_stg_campaign_touches as (

    SELECT
        touch_id,
        ticket_id, 
        campaign_id,
        cast(touched_at AS TIMESTAMP) AS touched_at

    FROM source
    
)
Select * from standardize_stg_campaign_touches


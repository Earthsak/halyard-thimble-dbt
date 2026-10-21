

With source as (

   Select * from {{ source('ht_erp', 'finance_ledger_fy2026') }}
),

standardize_stg_finance_ledger_fy2026 as (

    SELECT
        cast(fiscal_year as integer) as fiscal_year,
        cast(fiscal_period as integer) as fiscal_period,
        account_code,
        journal_ref,
        journal_description,
        cast(amount_cad as decimal) as amount_cad
    FROM source
    
)
Select * from standardize_stg_finance_ledger_fy2026


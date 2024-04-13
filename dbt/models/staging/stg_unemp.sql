{{
    config(
        materialized='view'
    )
}}

with unempdata as 
(
  select *,
  from {{ source('staging','unemp_rate') }}
)

select
   
    cast(date_numeric as date) as unemp_month,
    {{ dbt.safe_cast("unemployment_rate", api.Column.translate_type("float")) }} as unemp_percent,
    
from unempdata

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=false) %}

  limit 100

{% endif %}
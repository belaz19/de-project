{{
    config(
        materialized='view'
    )
}}

with crimedata as 
(
  select *,
  from {{ source('staging','crime_victim') }}
)

select
    -- identifiers
    {{ dbt.safe_cast("dr_no", api.Column.translate_type("integer")) }} as recordid,
    
    -- timestamp
    cast(date_occ as timestamp) as crime_date,
    
    -- vict info
    {{ dbt.safe_cast("vict_age", api.Column.translate_type("integer")) }} as victim_age,
    {{ dbt.safe_cast("vict_sex", api.Column.translate_type("string")) }} as victim_sex,
    {{ get_vict_descent("vict_descent") }} as victim_descent_description,

    -- crime info
    {{ dbt.safe_cast("time_occ", api.Column.translate_type("integer")) }} as crime_time,
    {{ dbt.safe_cast("area_name", api.Column.translate_type("string")) }} as area,
    {{ dbt.safe_cast("crm_cd_desc", api.Column.translate_type("string")) }} as crime_type,
    {{ dbt.safe_cast("weapon_used_cd", api.Column.translate_type("string")) }} as weapon_used
    
from crimedata

-- dbt build --select <model_name> --vars '{'is_test_run': 'false'}'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}
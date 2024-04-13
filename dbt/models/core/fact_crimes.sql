{{ config(
    materialized='table',
    partition_by={
      "field": "crime_date",
      "data_type": "date",
      "granularity": "month"
    },
    cluster_by = "area"
)}}

with crimedata as (
    select * from {{ ref('stg_crime') }}
),

unempdata as (
    select * from {{ ref('stg_unemp') }}
)

select crimedata.recordid,
crimedata.crime_date,
crimedata.crime_time,
crimedata.victim_age,
crimedata.victim_sex,
crimedata.victim_descent,
crimedata.area,
crimedata.crime_type,
crimedata.weapon_used, 
unempdata.unemp_percent

from crimedata
inner join unempdata
on crimedata.crime_month = unempdata.unemp_month
{#
    This macro returns the description of the victim descent 
#}

{% macro get_vict_descent(vict_descent) -%}

    case {{ dbt.safe_cast("vict_descent", api.Column.translate_type("string")) }}  
        when 'H' then 'Latin'
        when 'W' then 'White'
        when 'B' then 'Black'
        else 'Other'
    end

{%- endmacro %}
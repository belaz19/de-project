{#
    This macro returns the description of the victim descent 
#}

{% macro get_vict_sex(vict_sex) -%}

    case {{ dbt.safe_cast("vict_sex", api.Column.translate_type("string")) }}  
        when 'M' then 'Male'
        when 'F' then 'Female'
        else 'Other'
    end

{%- endmacro %}
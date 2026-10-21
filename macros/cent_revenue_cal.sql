


{% macro cents_revenue(quantity, unit_price, discount_pct) %}
    ROUND(
        CAST({{ quantity }} AS DECIMAL) 
        * CAST({{ unit_price }} AS DECIMAL) 
        * (1 - CAST({{ discount_pct }} AS DECIMAL)),
        2
    )
{% endmacro %}
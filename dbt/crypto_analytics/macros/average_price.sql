{% macro average_price(column_name) %}

ROUND(AVG({{ column_name }}), 2)

{% endmacro %}
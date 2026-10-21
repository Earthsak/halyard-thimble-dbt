


{% test assert_no_duplicate_line_events(model, ticket_id_col, line_no_col) %}
SELECT
    {{ ticket_id_col }},
    {{ line_no_col }},
    COUNT(*) AS cnt
FROM {{ model }}
GROUP BY 1, 2
HAVING COUNT(*) > 1
{% endtest %}
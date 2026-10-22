

{% test assert_no_duplicate_line_events(model, column_name, ticket_id_col, line_no_col) %}
select
    {{ ticket_id_col }},
    {{ line_no_col }},
    count(*) as cnt
from {{ model }}
group by 1, 2
having count(*) > 1
{% endtest %}
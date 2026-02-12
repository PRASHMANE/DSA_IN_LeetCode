SELECT
    m.employee_id AS employee_id,
    m.name,
    COUNT(e.reports_to) AS reports_count,
    ROUND(AVG(e.age))::int AS average_age
FROM employees AS e 
JOIN employees AS m ON e.reports_to = m.employee_id
GROUP BY
    m.employee_id, m.name
ORDER BY
    m.employee_id
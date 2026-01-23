# Write your MySQL query statement below
WITH a AS (
    SELECT managerId
    FROM employee
    GROUP BY managerId
    HAVING COUNT(1) > 4)
SELECT e.name
FROM employee e
INNER JOIN a
    ON e.id = a.managerId;
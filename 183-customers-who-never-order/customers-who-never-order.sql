# Write your MySQL query statement below
select c.name as Customers
from Customers as c
where c.id not in
(select c.id
from Customers as c
INNER JOIN Orders as o
on c.id = o.customerId);
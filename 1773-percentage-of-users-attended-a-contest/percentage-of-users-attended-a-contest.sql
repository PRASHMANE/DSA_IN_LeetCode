# Write your MySQL query statement below
# Write your MySQL query statement below
select r.contest_id,
ROUND(
    count(r.user_id)/(SELECT count(*) FROM Users)*100,2
) as percentage
from Users u 
left join Register r 
on u.user_id = r.user_id
WHERE r.contest_id is not null
group by r.contest_id
order by percentage DESC, r.contest_id ASC ;
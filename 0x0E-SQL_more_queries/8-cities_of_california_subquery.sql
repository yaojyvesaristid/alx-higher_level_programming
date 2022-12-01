-- lists all the cities of California
-- results must be sorted in ascending order by cities.id
-- not allowed to user JOIN
USE hbtn_0d_usa;
SELECT * FROM cities c
WHERE c.state_id = (SELECT states.id FROM states s WHERE s.name = 'California')
ORDER BY c.id ASC;

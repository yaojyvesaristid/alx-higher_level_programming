-- lists all the cities of California
-- results must be sorted in ascending order by cities.id
-- not allowed to user JOIN
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities c, states s
WHERE c.state_id = s.id AND s.name = 'California'
ORDER BY c.id ASC;

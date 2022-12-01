-- lists all the cities of California
-- results must be sorted in ascending order by cities.id
-- not allowed to user JOIN
USE hbtn_0d_usa;
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;

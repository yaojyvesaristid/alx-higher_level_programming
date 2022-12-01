-- lists all the cities of California
-- results must be sorted in ascending order by cities.id
-- not allowed to user JOIN
USE hbtn_0d_usa;
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
    AND states.name = 'California'
ORDER BY cities.id ASC;

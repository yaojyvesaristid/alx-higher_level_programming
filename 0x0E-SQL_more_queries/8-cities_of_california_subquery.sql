-- lists all the cities of California
-- results must be sorted in ascending order by cities.id
-- not allowed to use JOIN
SELECT cities.id, cities.name
FROM cities, states
WHERE cities.state_id = states.id
    AND states.name = 'California'
ORDER BY cities.id ASC;

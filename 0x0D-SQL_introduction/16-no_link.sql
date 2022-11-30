-- lists all records of second_table
-- +don't list row without a name value
-- +results should display the score and the name
-- +records should be listed bu descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC

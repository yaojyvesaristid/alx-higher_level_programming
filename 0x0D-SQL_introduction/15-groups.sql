-- lists the number of records with the same score
-- +result should display score
-- +number of records for this score with the label number
-- +should be sorted by the number of records desc
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC

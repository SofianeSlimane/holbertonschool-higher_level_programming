-- Lists all scores, group them by the amount of times they appear
-- in records, and sort them in descending order
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
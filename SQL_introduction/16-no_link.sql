-- Lists records of table in descending order except empty name fields
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
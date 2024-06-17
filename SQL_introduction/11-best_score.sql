-- List all records with a score >= 10 and sort by ascending score
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
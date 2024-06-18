-- Returns all records that exist in two tables
-- that match the ON condition
SELECT cities.id, cities.name, states.name
FROM cities INNER JOIN states
ON cities.state_id = states.id 
ORDER BY cities.id ASC;

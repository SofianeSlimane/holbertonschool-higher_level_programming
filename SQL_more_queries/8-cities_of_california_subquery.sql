-- lists columns with specific foreign key value
SELECT id, name FROM cities WHERE state_id = 1
ORDER BY cities.id ASC;

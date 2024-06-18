-- Creates a table with id and name columns
-- values in name field cannot be NULL (constaint)
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

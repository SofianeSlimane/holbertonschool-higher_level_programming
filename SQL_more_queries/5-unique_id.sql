-- Creates a table with id and name columns
-- values in id field are 1 by default and must be unique (constraints)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

-- Creates a table with id and name columns
-- values in id field are 1 by default (constraint)
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

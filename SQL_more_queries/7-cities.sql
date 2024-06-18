-- Creates a database, a table with three fields in that database
-- all field have constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY UNIQUE AUTO_INCREMENT,
    state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);

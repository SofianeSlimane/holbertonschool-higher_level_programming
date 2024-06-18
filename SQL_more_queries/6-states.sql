-- Creates a database, a table with two fields in that database
-- Both field have constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT PRIMARY KEY UNIQUE AUTO_INCREMENT ,
    name VARCHAR(256) NOT NULL
);

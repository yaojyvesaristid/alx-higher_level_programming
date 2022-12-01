-- create the table unique_id
-- +id int with the default value 1 and must be unique
-- +name varchar(256)
CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));

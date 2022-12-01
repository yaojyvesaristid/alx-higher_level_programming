-- creates the database hbtn_0d_usa and the table cities
-- +id int unique, ai,not null, pk
-- +state_id int, not null, fk(id of states table)
-- +name varchar(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));

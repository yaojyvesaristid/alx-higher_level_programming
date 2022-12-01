-- create database hbtn_0d_usa and the table states
-- +id int unique, auto generated, can't be null and pk
-- +name varchar(256) not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);

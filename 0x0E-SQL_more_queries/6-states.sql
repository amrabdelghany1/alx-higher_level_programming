-- creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

CREATE DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT PRIMARY, name VARCHAR(256) NOT NULL);

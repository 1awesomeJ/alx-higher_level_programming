-- This script creates a table in a database.

CREATE TABLE IF NOT EXISTS unique_id(
id INT DEFAULT 1 PRIMARY KEY,
name VARCHAR(256) NOT NULL);

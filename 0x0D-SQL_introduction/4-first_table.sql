-- This script creates a table in a database, and it doesn't fail even if the databse exists
CREATE TABLE IF NOT EXISTS first_table (
id INT,
name VARCHAR(256)
);

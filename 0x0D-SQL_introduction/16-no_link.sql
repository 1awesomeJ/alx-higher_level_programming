-- This script lists all the rows with the same score  in a table in a database, and it doesn't fail even if the databse exists

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

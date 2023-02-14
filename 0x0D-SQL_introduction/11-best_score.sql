-- This script lists all the rows in a table in a database, and it doesn't fail even if the databse exists

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;

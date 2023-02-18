-- This script lists all the rows with the same score  in a table in a database, and it doesn't fail even if the databse exists

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;

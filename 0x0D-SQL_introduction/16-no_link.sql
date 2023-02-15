-- list all records of the table second_table
-- don't list rows without a name value
-- display the score and name
-- order by score (descending)
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;

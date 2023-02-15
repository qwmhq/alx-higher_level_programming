-- list the number of records with the same score in the table second_table
-- display the score and the number of records for each score with label number
-- order by number (descending)
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;

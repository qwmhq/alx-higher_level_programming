-- list all the cities of California
-- sort in ascending order by cities.id
SELECT id, name
FROM cities
WHERE state_id =
	(SELECT id
	 FROM states
	 WHERE name = "California");

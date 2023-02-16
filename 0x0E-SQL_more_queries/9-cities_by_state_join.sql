-- list all cities
-- display: cities.id - cities.name - states.name
-- order by cities.id (ascending)
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;

-- lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.id = states.id;

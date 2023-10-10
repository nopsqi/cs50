SELECT *
FROM people p1
INNER JOIN stars s1 ON s1.person_id = p1.id
INNER JOIN movies m ON m.id = s1.movie_id
INNER JOIN stars s2 ON s2.movie_id = m.id
LIMIT 20;
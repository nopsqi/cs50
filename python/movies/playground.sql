SELECT *
FROM people p1
INNER JOIN stars s1 ON s1.person_id = p1.id
INNER JOIN movies m ON m.id = s1.movie_id
INNER JOIN stars s2 ON s2.movie_id = m.id
INNER JOIN peopl p2 ON p2.
LIMIT 20;